import cv2
import numpy as np

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

def processImage(bgr_img):
    processed_img = np.zeros((bgr_img.shape[0], bgr_img.shape[1], 3), dtype="uint8") # value to return
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
    for i in range(6): # loop through for all 6 colors
        square_color = switch(i)
        mask = cv2.inRange(hsv_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
        mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 150)) # kernel to clean up vertical divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (150, 2)) # kernel to clean up horizontal divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        num_labels, labels_img, stats, centroids = cv2.connectedComponentsWithStats(mask)
        color_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=mask) # get color of mask in image
        processed_img = cv2.bitwise_or(processed_img, color_mask) # add to or'ed image
        for n in range(num_labels):
            xc, yc = centroids[n]
            if xc == 959.5 and yc == 539.5:
                continue 
            print(i, xc, yc)
            processed_img = cv2.circle(processed_img, (int(xc), int(yc)), 20, square_color, -1)
    return processed_img # return processed image

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
        key = cv2.waitKey(1)
        if key == 27: # if key is ESC
            break
    # end of while loop
    feed.release() # release resources
    cv2.destroyAllWindows() # close windows

if __name__ == "__main__":
    main()