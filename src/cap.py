import cv2
import time

# cap = cv2.VideoCapture(0,cv2.CAP_AVFOUNDATION) #input is the id of the camera, 1st camera id is 0, specify which camera used to collect data
# while cap.isOpened(): # isopened() return true if the camera is opened
#     ret,frame = cap.read() #read one data from camera and assign to frame, ret is boolean, return means we read data otherwise we fail to read data
#     if ret:
#         cv2 .imwrite('frame.png',frame) #store the return data as jpg file
#         break
#     # cv2.imshow('frame',frame) #display the data
#     # if cv2.waitKey(1) & 0xFF == ord('q'): #if user enter q, then the window will be closed
#     #     break
# cap.release() # release resources
# integrate the above code as function
# def capture_Image():
#     cap = cv2.VideoCapture(0,cv2.CAP_AVFOUNDATION)
#
#     while cap.isOpened():
#         ret,frame = cap.read()
#         if ret:
#             cv2.imwrite('frame.png',frame)
#             break
#     cap.release()
def capture_Image():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        raise RuntimeError("Camera not opened")

    # 尝试开启自动曝光（部分后端有效）
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)

    # 预热：丢掉前 20~30 帧，并等待 0.3s，让曝光稳定
    for _ in range(30):
        cap.read()
    time.sleep(0.3)

    # 连续读几帧，选一张“亮度达标”的再保存
    ok = False
    for _ in range(30):
        ret, frame = cap.read()
        if not ret:
            continue
        if frame.mean() > 30:          # 简单亮度阈值，按需调高/调低
            cv2.imwrite('frame.png', frame)
            ok = True
            break

    cap.release()
    if not ok:
        raise RuntimeError("Image too dark — try turning on lights or raise exposure")
capture_Image()

def capture_Video():
    cap = cv2.VideoCapture(0,cv2.CAP_AVFOUNDATION)
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to read first frame")
    #store the frame of data as video file
    h, w = frame.shape[:2]
    size = (w, h)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #specify output file format
    out = cv2.VideoWriter('output.mp4',fourcc,fps,size) #output filename frames per second resolution

    i = 0
    while cap.isOpened():
         ret,frame = cap.read()
         if ret:
             if i <= 100:
                out.write(frame)
             else:
                 break
             i+=1
         else:
             print("video capture error")
             break
    cap.release()
    out.release()
#capture_Video()
