import cv2
import time
import webcam_reader

# vars for calculating fps

prev_frame_time = 0
new_frame_time = 0

cam = webcam_reader.WebcamVideoStream(0).start()

while True:
    
    frame = cam.read()
    new_frame_time = time.time()
    fps = int(1 / (new_frame_time - prev_frame_time))
    prev_frame_time = new_frame_time

    # display fps

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
            frame, 
            str(fps),
            (7,30),
            font,
            1,
            (100, 255, 0),
            2,
            cv2.LINE_AA)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        cam.stop()
        cv2.destroyAllWindows()
        break

