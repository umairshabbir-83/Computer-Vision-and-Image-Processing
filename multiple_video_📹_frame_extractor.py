# Importing All Necessary Libraries
import cv2
import glob
from google.colab import drive
import os

drive.mount("/content/drive")

# Getting Folder 📂

folder = glob.glob("/content/drive/MyDrive/Dataset Collection/Newly Created/1")

# Getting Video 📹 List 📃
video_list = []
for i in folder:
    for j in glob.glob(i + "/*.mp4"):
        video_list.append(j)
        print(j)

# Creating Output Folder 📂

try:
    if not os.path.exists("/content/drive/MyDrive/Dataset Collection/FramesOUT"):
        os.makedirs("/content/drive/MyDrive/Dataset Collection/FramesOUT")
except OSError:
    print("ERROR: DIRECTORY NOT FOUND!")

# Extracting Frames

counter = 0
for i in video_list:
    cap = cv2.VideoCapture(i)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            cv2.imwrite(
                "/content/drive/MyDrive/Dataset Collection/FramesOUT/Frame."
                + str(counter)
                + ".jpg",
                frame,
            )
            counter += 1
        else:
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
print("Total Frames:", counter)
