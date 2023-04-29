import cv2
import datetime

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 29.97
delay = round(1000/ fps)
size  = (640, 360)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

print("프레임 해상도:", size)
print("압축코덱 숫자:", fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv2.VideoWriter("your_img_video.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

count = 0
while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    frame = cv2.bilateralFilter(frame, 5, 100, 100)

    writer.write(frame)

    if count % 100 == 0:
        now = datetime.datetime.now()
        filename = now.strftime("%Y%m%d_%H%M%S") + ".jpg"
        cv2.imwrite(filename, frame)
    count += 1

    cv2.imshow("View Frame from Camera", frame)

writer.release()
capture.release()
cv2.destroyAllWindows()