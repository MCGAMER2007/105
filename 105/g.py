import cv2
import os

path = "images"

image = []

for file in os.listdir(path):
    name, ext = os.path.splittext(file)

    if ext in ['.gif', '.png', '.jpeg', '.jpg', '.jfif']:
        file_name = path+"/"+file 

        print(file_name)

        image.append(file_name)

print(len(image))
count = len(image)

frame = cv2.imread(image[0])
height, width, chanels = frame.shape
size = (width, height)

out = cv2.VIdeoWriter('pl.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(count -1, 0, -1):
    frame = cv2.imread(image[i])
    out.write(frame)

out.release()
print("Done")