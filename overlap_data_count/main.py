import pandas as pd 
import numpy as np
import function
import matplotlib.pyplot as plt
import cv2

train_df = pd.read_csv("./train.csv")

print(train_df.columns)
# 'image_id', 'class_name', 'class_id', 'rad_id', 'x_min', 'y_min','x_max', 'y_max'

# print(train_df.describe())

image_id = train_df["image_id"]
class_name =  train_df["class_name"]
class_id = train_df["class_id"] 
rad_id = train_df["rad_id"]
x_min = train_df["x_min"]
y_min = train_df["y_min"]
x_max = train_df["x_max"]
y_max = train_df["y_max"]

#print(len(image_id.unique())) # 15000

# print(class_name.value_counts())
# print(class_name.value_counts().isna()) # check

# print(class_id.value_counts())
# print(class_id.value_counts().isna()) #check

# train_df["image_path"] = 0
# for i in range(train_df.shape[0]):
#     # train_df["image_path"].copy()[i] = f'./dataset/{image_id[i]}.dicom'
#     train_df["image_path"][i] = f'./dataset/{image_id[i]}.dicom'
# #print(train_df["image_path"])

img = function.read_xray('./dataset/0005e8e3701dfb1dd93d53e2ff537b6e.dicom')
print(f'{img}, {type(img)}, {img.shape}')
#img_zero = np.zeros_like(img)
img = cv2.merge((img, img, img))

indexes = train_df[train_df["image_id"] == "0005e8e3701dfb1dd93d53e2ff537b6e"].index

for index in indexes:
    print(train_df.iloc[index])
    print(f'({int(x_min[index])}, {int(y_min[index])}) / ({int(x_max[index])}, {int(y_max[index])})')
    cv2.rectangle(img, (int(x_min[index]), int(y_min[index])), (int(x_max[index]), int(y_max[index])), function.red, 3) 
    cv2.putText(img, str(class_name[index]), (int(x_min[index]), int(y_min[index]-3)),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255) , 2)




img = function.FitToWindowSize(img)
cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()