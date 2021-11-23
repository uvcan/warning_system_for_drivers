import cv2
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID');
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
capture.set(3, 512)
capture.set(4, 420)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(capture.get(3)),int(capture.get(4))));
print(capture.get(3))
print(capture.get(4))
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:'+ str(capture.get(3)) + 'Height:' + str(capture.get(4))
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


capture.release()
out.release()
cv2.destroyAllWindows()