import cv2

gst = 'udpsrc port=9000 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=f'
cap = cv2.VideoCapture(gst,cv2.CAP_GSTREAMER)

while True:
    ret,frame = cap.read()
    cv2.imshow('gstreamer_test',frame)
    print(ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindow()
