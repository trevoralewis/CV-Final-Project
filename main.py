import cv2
import numpy as np

# set boundaries
RED_UPPER_BOUND = np.array([70, 70, 255])
RED_LOWER_BOUND = np.array([0, 0, 150])
ORANGE_UPPER_BOUND = np.array([70, 140, 255])
ORANGE_LOWER_BOUND = np.array([0, 100, 150])
YELLOW_UPPER_BOUND = np.array([150, 255, 255])
YELLOW_LOWER_BOUND = np.array([50, 195, 195])
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
        mask = cv2.inRange(bgr_img, bounds[i*2], bounds[i*2+1]) # grab mask for specific range
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 10)) # kernel to clean up vertical divisions
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



    # open image
    #bgr_img = openImage("Rubik_t5.jpg")
    # get image details
    width = bgr_img.shape[1]
    height = bgr_img.shape[0]
    # define masks
    r_mask = cv2.inRange(bgr_img, RED_LOWER_BOUND, RED_UPPER_BOUND)
    o_mask = cv2.inRange(bgr_img, ORANGE_LOWER_BOUND, ORANGE_UPPER_BOUND)
    y_mask = cv2.inRange(bgr_img, YELLOW_LOWER_BOUND, YELLOW_UPPER_BOUND)
    g_mask = cv2.inRange(bgr_img, GREEN_LOWER_BOUND, GREEN_UPPER_BOUND)
    b_mask = cv2.inRange(bgr_img, BLUE_LOWER_BOUND, BLUE_UPPER_BOUND)
    w_mask = cv2.inRange(bgr_img, WHITE_LOWER_BOUND, WHITE_UPPER_BOUND)
    # process each image to obtain a cleaner image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (100, 10))
    cv2.imshow('Mask1', w_mask)
    cv2.waitKey(0)
    filtered_r = cv2.morphologyEx(w_mask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Mask1', filtered_r)
    cv2.waitKey(0)
    # grab indivdual images for every color
    r_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=r_mask)
    o_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=o_mask)
    y_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=y_mask)
    g_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=g_mask)
    b_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=b_mask)
    w_mask = cv2.bitwise_and(bgr_img, bgr_img, mask=w_mask)
    # combine the images into one image
    bgr_img = cv2.bitwise_or(r_mask, o_mask)
    bgr_img = cv2.bitwise_or(bgr_img, y_mask)
    bgr_img = cv2.bitwise_or(bgr_img, g_mask)
    bgr_img = cv2.bitwise_or(bgr_img, b_mask)
    bgr_img = cv2.bitwise_or(bgr_img, w_mask)
    # show image
    cv2.imshow("rubik test", bgr_img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()