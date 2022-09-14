# Imported all Necessary Libraries

import cv2
import glob
from google.colab import drive
import os

drive.mount("/content/drive")

# Getting Input Folder 📂

folder = glob.glob("/content/drive/MyDrive/Dataset Collection/FramesOUT")

# Getting Size of the Input Folder 📂

total_size = 0
for dirpath, dirnames, filenames in os.walk(
    "/content/drive/MyDrive/Dataset Collection/FramesOUT"
):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)
print("Folder size: " + str(total_size) + " bytes")

# Getting Input Files 📂

frames_list = []
for i in folder:
    for j in glob.glob(i + "/*.jpg"):
        frames_list.append(j)
print("Total number of frames: ", len(frames_list))

# Locating Output Folder 📂

try:
    if not os.path.exists("/content/drive/MyDrive/Dataset Collection/Resized"):
        os.makedirs("/content/drive/MyDrive/Dataset Collection/Resized")
except OSError:
    print("ERROR: DIRECTORY NOT FOUND!")

# Resizing Frames

counter = 0
for i in frames_list:
    img = cv2.imread(i, -1)
    resized = cv2.resize(img, (224, 224))
    cv2.imwrite(
        "/content/drive/MyDrive/Dataset Collection/Resized/Frame."
        + str(counter)
        + ".jpg",
        resized,
    )
    counter += 1

# Getting Size of the Output Folder 📂

total_size = 0
for dirpath, dirnames, filenames in os.walk(
    "/content/drive/MyDrive/Dataset Collection/Resized"
):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)
print("Folder size: " + str(total_size) + " bytes")
