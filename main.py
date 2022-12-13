import cv2
import numpy as np

def switch(item):
    if item == 0:
        square_color = ((255,255,255), 0)
    elif item == 1:
        square_color = ((0,255,0), 1)
    elif item == 2:
        square_color = ((0,0,255), 2)
    elif item == 3:
        square_color = ((255,0,0), 3)
    elif item == 4:
        square_color = ((0,128,255), 4)
    elif item == 5:
        square_color = ((0,255,255), 5)
    return square_color

# array of boundaries
bounds = np.array([
    np.array([50, 0, 150]), np.array([100, 100, 255]), # white boundaries
    np.array([60, 100, 0]), np.array([80, 255, 255]), # green boundaries
    np.array([170, 160, 0]), np.array([190, 255, 255]), # red boundaries
    np.array([75, 100, 0]), np.array([120, 255, 255]), # blue boundaries
    np.array([0, 130, 0]), np.array([20, 255, 255]), # orange boundaries
    np.array([20, 140, 0]), np.array([50, 255, 255]) # yellow boundaries
])
# solved cube
solved = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[1,1,1],[1,1,1],[1,1,1]],
    [[2,2,2],[2,2,2],[2,2,2]],
    [[3,3,3],[3,3,3],[3,3,3]],
    [[4,4,4],[4,4,4],[4,4,4]],
    [[5,5,5],[5,5,5],[5,5,5]],
]

unsolved = [
    [[-1,-1,-1],[-1,0,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,1,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,2,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,3,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,4,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,5,-1],[-1,-1,-1]]
]

SIGMA_BLUR = 5.0
key = 0
face = 0

def processImage(bgr_img):
    # take in image details
    img_width = bgr_img.shape[1]
    img_height = bgr_img.shape[0]
    global face
    global unsolved
    centers = []
    # draw boundaries on live feed
    bgr_img = cv2.line( # left
        bgr_img, 
        (int(img_width * (4/9)), int(img_height * (4/5))), 
        (int(img_width * (4/9)), int(img_height * (1/5))), 
        (255, 255, 255),
        5
    )
    bgr_img = cv2.line( # right
        bgr_img, 
        (int(img_width * (5/9)), int(img_height * (4/5))), 
        (int(img_width * (5/9)), int(img_height * (1/5))), 
        (255, 255, 255),
        5
    )
    bgr_img = cv2.line( # top
        bgr_img, 
        (int(img_width * (1/3)), int(img_height * (6/15))), 
        (int(img_width * (2/3)), int(img_height * (6/15))), 
        (255, 255, 255),
        5
    )
    bgr_img = cv2.line( # bottom
        bgr_img, 
        (int(img_width * (1/3)), int(img_height * (9/15))), 
        (int(img_width * (2/3)), int(img_height * (9/15))), 
        (255, 255, 255),
        5
    )
    # draw face no.
    bgr_img = cv2.putText(bgr_img, str(face), (img_width - 100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5, cv2.LINE_AA)
    # convert to grayscale
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    # blur image
    gauss_img = cv2.GaussianBlur(
        src=gray_img,
        ksize=(17, 17),  # kernel size (should be odd numbers; if 0, compute it from sigma)
        sigmaX=SIGMA_BLUR, sigmaY=SIGMA_BLUR
    )
    thresh_canny = 5
    edge_img = cv2.Canny(
        image=gauss_img,
        apertureSize=3,  # size of Sobel operator
        threshold1=thresh_canny,  # lower threshold
        threshold2=3*thresh_canny,  # upper threshold
        L2gradient=True # use more accurate L2 norm
    )
    contours, hierarchy = cv2.findContours(gray_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    edge_img = cv2.drawContours(edge_img, contours, -1, (255, 255, 255), 10, lineType=cv2.LINE_AA)
    processed_img = np.zeros((bgr_img.shape[0], bgr_img.shape[1], 3), dtype="uint8") # value to return
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
    hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=cv2.bitwise_not(edge_img))
    for i in range(6): # loop through for all 6 colors
        square_color = switch(i)
        mask = cv2.inRange(hsv_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 5)) # kernel to clean up divisions divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 50)) # kernel to clean up divisions divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
        mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
        num_labels, labels_img, stats, centroids = cv2.connectedComponentsWithStats(mask)
        color_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=mask) # get color of mask in image
        processed_img = cv2.bitwise_or(processed_img, color_mask) # add to or'ed image
        for n in range(num_labels):
            xc, yc = centroids[n]
            if xc >= 959.5 - 5 and xc <= 959.5 + 5 and yc >= 539.5 - 5 and yc <= 539.5 + 5:
                continue 
            #print(i, xc, yc)
            centers.append((xc, yc, square_color[1]))
            bgr_img = cv2.circle(bgr_img, (int(xc), int(yc)), 25, (0, 0, 0), -1)
            bgr_img = cv2.circle(bgr_img, (int(xc), int(yc)), 20, square_color[0], -1)
    if key == ord(' '):
        for n in range(len(centers)):
            xc, yc, col = centers[n]
            if xc < img_width * (4/9) and yc < img_height * (6/15):# if tl
                unsolved[face][0][0] = col
            elif xc > img_width * (4/9) and xc < img_width * (5/9) and yc < img_height * (6/15): # if t
                unsolved[face][0][1] = col
            elif xc > img_width * (5/9) and yc < img_height * (6/15):# if tr
                unsolved[face][0][2] = col
            elif xc < img_width * (4/9) and yc > img_height * (6/15) and yc < img_height * (9/15):# if ml
                unsolved[face][1][0] = col
            elif xc > img_width * (5/9) and yc > img_height * (6/15) and yc < img_height * (9/15):# if mr
                unsolved[face][1][2] = col
            elif xc < img_width * (4/9) and yc > img_height * (9/15):# if bl
                unsolved[face][2][0] = col
            elif xc > img_width * (4/9) and xc < img_width * (5/9) and yc > img_height * (9/15):# if b 
                unsolved[face][2][1] = col
            elif xc > img_width * (5/9) and yc > img_height * (9/15):# if br
                unsolved[face][2][2] = col
        face+=1
        print('Now on face ' + str(face))
    centers = []
    return bgr_img # return processed image

def main():
    # open live video
    feed = cv2.VideoCapture(0)
    # loop through live feed
    while True:
        # grab frame
        success, bgr_img = feed.read()
        # simplify and label image of cube
        processed_img = processImage(bgr_img)
        # display video
        cv2.imshow('Live Feed', processed_img)
        # exit condition for video
        global key 
        key = cv2.waitKey(1)
        if key == 27: # if key is ESC
            print(unsolved)
            break
    # end of while loop
    feed.release() # release resources
    cv2.destroyAllWindows() # close windows

if __name__ == "__main__":
    main()