import cv2
import time

cam = cv2.VideoCapture(0)

# vars for calculating fps

prev_frame_time = 0
new_frame_time = 0

while True:

    ret, frame = cam.read()
    
    new_frame_time = time.time()
    fps = int(1 / (new_frame_time - prev_frame_time))
    prev_frame_time = new_frame_time

    # display fps

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
            frame, 
            str(fps),
            (7,70),
            font,
            3,
            (100, 255, 0),
            3,
            cv2.LINE_AA)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()