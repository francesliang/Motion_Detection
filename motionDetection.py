import cv2

# Image difference function
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
retval, img = cam.read()


winName = "Motion Detection"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read 3 images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while retval:
    
    img = diffImg(t_plus, t, t_minus)
    cv2.imshow(winName, img)  
    
    #retval, img = cam.read()
    
    # Read the next image
    t_minus = t;
    t = t_plus;
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    
    key = cv2.waitKey(10)
    if key == 27: #ASCII code for ESC key
        cam.release()
        cv2.destroyWindow(winName)
        break

