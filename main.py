import cv2
import numpy as np

# set boundaries
RED_UPPER_BOUND = np.array([70, 80, 255])
RED_LOWER_BOUND = np.array([0, 0, 140])
ORANGE_UPPER_BOUND = np.array([70, 140, 255])
ORANGE_LOWER_BOUND = np.array([0, 50, 150])
YELLOW_UPPER_BOUND = np.array([100, 255, 255])
YELLOW_LOWER_BOUND = np.array([50, 100, 100])
GREEN_UPPER_BOUND = np.array([150, 255, 180])
GREEN_LOWER_BOUND = np.array([50, 173, 100])
BLUE_UPPER_BOUND = np.array([255, 200, 110])
BLUE_LOWER_BOUND = np.array([150, 0, 0])
WHITE_UPPER_BOUND = np.array([255, 255, 255])
WHITE_LOWER_BOUND = np.array([170, 170, 170])
# array of boundaries
bounds = np.array([
    RED_LOWER_BOUND, RED_UPPER_BOUND,
    ORANGE_LOWER_BOUND, ORANGE_UPPER_BOUND,
    YELLOW_LOWER_BOUND, YELLOW_UPPER_BOUND,
    GREEN_LOWER_BOUND, GREEN_UPPER_BOUND,
    BLUE_LOWER_BOUND, BLUE_UPPER_BOUND,
    WHITE_LOWER_BOUND, WHITE_UPPER_BOUND
])

def processImage(bgr_img):
    processed_img = np.zeros((bgr_img.shape[0], bgr_img.shape[1], 3), dtype="uint8") # value to return
    for i in range(6): # loop through for all 6 colors
        if i == 0 or i == 1 or i == 2:
            mask = cv2.inRange(bgr_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
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