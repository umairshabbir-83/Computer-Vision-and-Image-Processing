# Importing All Necessary Libraries
import cv2
import glob
import os

# Getting Folder 📂

folder = glob.glob("C:/Users/UMAIR SHABBIR/Downloads/1")

# Getting Video 📹 List 📃
video_list = []
for i in folder:
    for j in glob.glob(i + "/*.mp4"):
        video_list.append(j)

# Creating Output Folder 📂

try:
    if not os.path.exists("C:/Users/UMAIR SHABBIR/Downloads/FramesOUT"):
        os.makedirs("C:/Users/UMAIR SHABBIR/Downloads/FramesOUT")
except OSError:
    print("ERROR: DIRECTORY NOT FOUND!")

# Extracting Frames

counter = 0
for i in video_list:
    cap = cv2.VideoCapture(i)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("FPS: ", fps, "fps")
    skip_frame = fps - 2
    print("FRAMES SKIPPED: ", skip_frame, "fps")
    j = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if j > skip_frame:
            cv2.imwrite(
                "C:/Users/UMAIR SHABBIR/Downloads/FramesOUT/Fire_Frame."
                + str(counter)
                + ".jpg",
                frame,
            )
            counter += 1
            print("C:/Users/UMAIR SHABBIR/Downloads/FramesOUT/Fire_Frame."
                  + str(counter)
                  + ".jpg")
            j = 0
        j += 1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
print("TOTAL FRAMES EXTRACTED: ", counter)
