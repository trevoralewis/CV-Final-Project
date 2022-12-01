import cv2
import numpy as np

# array of boundaries
bounds = np.array([
    np.array([10, 0, 200]), np.array([30, 255, 255]), # white boundaries
    np.array([35, 100, 0]), np.array([55, 255, 255]), # green boundaries
    np.array([170, 100, 0]), np.array([190, 255, 255]), # red boundaries
    np.array([75, 100, 0]), np.array([95, 255, 255]), # blue boundaries
    np.array([0, 100, 0]), np.array([10, 255, 255]), # orange boundaries
    np.array([15, 100, 0]), np.array([35, 255, 255]) # yellow boundaries
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
        if i != 0:
            continue
        mask = cv2.inRange(hsv_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10)) # kernel to clean up vertical divisions
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological open
        color_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=mask) # get color of mask in image
        processed_img = cv2.bitwise_or(processed_img, color_mask) # add to or'ed image
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