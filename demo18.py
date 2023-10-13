import face_recognition
import cv2
import os
import numpy as np

# 步骤1：收集和标记人脸数据集
# 在"known_faces"目录中放置包含已知人脸的图像，每个图像应包含一个人的脸。

# 步骤2：使用dlib训练人脸特征提取器
# 这一步通常不需要你自己操作，因为dlib已经内置了一个训练好的人脸特征提取器。你可以直接使用它。

# 步骤3：人脸识别
# 加载已知人脸数据集
known_faces = []
known_names = []

for image_file in os.listdir('known_faces'):
    image = face_recognition.load_image_file(os.path.join('known_faces', image_file))
    face_encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(face_encoding)
    known_names.append(image_file.split('.')[0])

# 使用OpenCV打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 缩小图像，加速识别

    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        top *= 4

        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
