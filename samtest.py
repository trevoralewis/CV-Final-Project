import cv2
import numpy as np
import time

# array of boundaries
bounds = np.array([
    np.array([170, 100, 0]), np.array([190, 255, 255]), # red boundaries
    np.array([0, 100, 0]), np.array([10, 255, 255]), # orange boundaries
    np.array([15, 100, 0]), np.array([35, 255, 255]), # yellow boundaries
    np.array([35, 100, 0]), np.array([55, 255, 255]), # green boundaries
    np.array([75, 100, 0]), np.array([95, 255, 255]), # blue boundaries
    np.array([10, 0, 0]), np.array([20, 255, 255]) # white boundaries
])

SIGMA_BLUR = 5.0

def processImage(bgr_img):
    # convert to grayscale
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    # blur image
    gauss_img = cv2.GaussianBlur(
        src=gray_img,
        ksize=(17, 17),  # kernel size (should be odd numbers; if 0, compute it from sigma)
        sigmaX=SIGMA_BLUR, sigmaY=SIGMA_BLUR
    )
    # get edge image with canny
    thresh_canny = 5
    edge_img = cv2.Canny(
        image=gauss_img,
        apertureSize=3,  # size of Sobel operator
        threshold1=thresh_canny,  # lower threshold
        threshold2=3*thresh_canny,  # upper threshold
        L2gradient=True # use more accurate L2 norm
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
    edge_img = cv2.morphologyEx(edge_img, cv2.MORPH_CLOSE, kernel)
    """
    output_thresh, edge_img = cv2.threshold(
        src=edge_img,
        maxval=255,
        type=cv2.THRESH_OTSU,
        thresh=0
    )
    # find contours in image
    contours, hierarchy = cv2.findContours(
        image=edge_img,
        mode=cv2.RETR_LIST,
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    # loop throuh contours
    i = 0
    for contour in contours:
        if i == 0:
            i = 1
            continue
        approx = cv2.approxPolyDP(contour, 0.05 * cv2.arcLength(contour, True), True)
        M = cv2.moments(contour)
        x, y = [1, 1]
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            #time.sleep(1)
        if len(approx) == 4:
            #cv2.putText(bgr_img, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.circle(bgr_img, (x, y), 5, (0, 0, 255), -1)
            cv2.drawContours(bgr_img, [contour], 0, (255, 0, 255), 5)
        i += 1
    """
    processed_img = edge_img
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