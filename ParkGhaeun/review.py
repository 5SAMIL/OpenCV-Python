import cv2
import datetime

capture = cv2.VideoCapture(0)                       # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 29.97                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (640, 360)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'MJPG')            # 압축 코덱 설정

# 카메라 속성 콘솔창에 출력
print("프레임 해상도:", size)
print("압축코덱 숫자:", fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

capture.set(cv2.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])     	# 해상도 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("your_img_video.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

count = 0 # 캡쳐된 사진 파일 이름에 넣을 번호
while True:
    ret, frame = capture.read()             # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    # 뽀샤시 필터 적용
    frame = cv2.bilateralFilter(frame, 5, 100, 100)

    # 동영상 저장
    writer.write(frame)

    # 캡쳐된 이미지 저장
    if count % 100 == 0: # 1초마다 한 번 캡쳐
        now = datetime.datetime.now()
        filename = now.strftime("%Y%m%d_%H%M%S") + ".jpg"
        cv2.imwrite(filename, frame)
    count += 1

    cv2.imshow("View Frame from Camera", frame)

writer.release()
capture.release()
cv2.destroyAllWindows()