import cv2
import numpy as np

# switch statement for color
def switch(item):
    if item == 0:
        square_color = (255,255,255)
    elif item == 1:
        square_color = (0,255,0)
    elif item == 2:
        square_color = (0,0,255)
    elif item == 3:
        square_color = (255,0,0)
    elif item == 4:
        square_color = (0,128,255)
    elif item == 5:
        square_color = (0,255,255)
    return square_color

# global variables
bounds = np.array([ # boundary array for hsv values 
    np.array([50, 0, 150]), np.array([100, 100, 255]), # white boundaries
    np.array([60, 100, 0]), np.array([80, 255, 255]), # green boundaries
    np.array([170, 160, 0]), np.array([190, 255, 255]), # red boundaries
    np.array([75, 100, 0]), np.array([120, 255, 255]), # blue boundaries
    np.array([0, 130, 0]), np.array([20, 255, 255]), # orange boundaries
    np.array([20, 140, 0]), np.array([50, 255, 255]) # yellow boundaries
])
solved = [ # solved representation of cube
    [[0,0,0],[0,0,0],[0,0,0]],
    [[1,1,1],[1,1,1],[1,1,1]],
    [[2,2,2],[2,2,2],[2,2,2]],
    [[3,3,3],[3,3,3],[3,3,3]],
    [[4,4,4],[4,4,4],[4,4,4]],
    [[5,5,5],[5,5,5],[5,5,5]],
]
unsolved = [ # holder for the initial state of the unsolved cube
    [[-1,-1,-1],[-1,0,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,1,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,2,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,3,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,4,-1],[-1,-1,-1]],
    [[-1,-1,-1],[-1,5,-1],[-1,-1,-1]]
]
SIGMA_BLUR = 5.0 # blur constant for gaussian blur
key = 0 # holder for key pressed
face = 0 # current face the user is on

def processImage(bgr_img):
    # take in image details
    img_width = bgr_img.shape[1] # width
    img_height = bgr_img.shape[0] # height
    global face # allow face to be updated
    global unsolved # allow unsolved to be updated
    centers = [] # holder for valid centers
    # draw boundaries on live feed
    bgr_img = cv2.line(bgr_img, (int(img_width * (4/9)), int(img_height * (4/5))), (int(img_width * (4/9)), int(img_height * (1/5))), (255, 255, 255), 5)
    bgr_img = cv2.line(bgr_img, (int(img_width * (5/9)), int(img_height * (4/5))), (int(img_width * (5/9)), int(img_height * (1/5))), (255, 255, 255), 5)
    bgr_img = cv2.line(bgr_img, (int(img_width * (1/3)), int(img_height * (6/15))), (int(img_width * (2/3)), int(img_height * (6/15))), (255, 255, 255), 5)
    bgr_img = cv2.line(bgr_img, (int(img_width * (1/3)), int(img_height * (9/15))), (int(img_width * (2/3)), int(img_height * (9/15))), (255, 255, 255), 5)
    # draw face number in top corner
    bgr_img = cv2.putText(bgr_img, "Face: " + str(face), (img_width - 300, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 20, cv2.LINE_AA)
    # convert to grayscale
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    # blur image
    gauss_img = cv2.GaussianBlur(src=gray_img, ksize=(17, 17), sigmaX=SIGMA_BLUR, sigmaY=SIGMA_BLUR)
    thresh_canny = 5 # threshold for canny edge
    # grab edges with canny
    edge_img = cv2.Canny(image=gauss_img, apertureSize=3, threshold1=thresh_canny, threshold2=3*thresh_canny, L2gradient=True)
    # find contours in canny image
    contours, hierarchy = cv2.findContours(gray_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # draw thick contours on image
    edge_img = cv2.drawContours(edge_img, contours, -1, (255, 255, 255), 10, lineType=cv2.LINE_AA)
    # set up color processing
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV) # convert to hsv
    hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=cv2.bitwise_not(edge_img)) # and with not'd edge img to remove edges from img
    for i in range(6): # loop through for all 6 colors
        square_color = switch(i) # grab the bgr value of the color we are on
        mask = cv2.inRange(hsv_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 5)) # kernel to clean up horizontal divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 50)) # kernel to clean up vertical divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20)) # kernel for centering masses
        mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel) # morphological erosion
        num_labels, labels_img, stats, centroids = cv2.connectedComponentsWithStats(mask) # grab connected components in the mask
        # for every center in centroids
        for n in range(num_labels):
            xc, yc = centroids[n]
            # if its too close to a center value, skip
            if xc >= 959.5 - 5 and xc <= 959.5 + 5 and yc >= 539.5 - 5 and yc <= 539.5 + 5: 
                continue 
            # else, append the center and its color number to an accessible function
            centers.append((xc, yc, i))
            # draw the colored circle in the center of the component
            bgr_img = cv2.circle(bgr_img, (int(xc), int(yc)), 25, (0, 0, 0), -1) # black outline
            bgr_img = cv2.circle(bgr_img, (int(xc), int(yc)), 20, square_color, -1) # colored center
    # user presses space (ready to take in face)
    if key == ord(' '):
        # for all the centers in centers
        for n in range(len(centers)):
            xc, yc, col = centers[n]
            # find which portion of the cube the center lies in, and save that value in the unsolved array
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
        face+=1 # add 1 to the face
        if face < 6:
            print('Now on face ' + str(face))
    centers = []
    return bgr_img # return processed image

def main():
    # announce face
    print('On face ' + str(face))
    # open live video
    feed = cv2.VideoCapture(0)
    # loop through live feed
    while True:
        # grab frame
        success, bgr_img = feed.read()
        # exit initial loop once faces have been set
        if face > 5:
            runAlgo(unsolved)
            break
        # simplify and label image of cube
        processed_img = processImage(bgr_img)
        # display video
        cv2.imshow('Live Feed', processed_img)
        # exit condition for video
        global key # make key updateable
        key = cv2.waitKey(1)
        if key == 27: # if key is ESC
            break
    # end of while loop
    feed.release() # release resources
    cv2.destroyAllWindows() # close windows

def runAlgo(unsolved):
    # open live video
    feed = cv2.VideoCapture(0)
    # loop through live feed
    while True:
        # grab frame
        success, bgr_img = feed.read()
        # display video
        cv2.imshow('Live Feed', bgr_img)
        # exit condition for video
        global key # make key updateable
        key = cv2.waitKey(1)
        if key == 27: # if key is ESC
            break

if __name__ == "__main__":
    main()