import numpy as np
from skimage import io
import matplotlib.pyplot as plt
# back=io.imread('backround2.png',as_gray=True)
# # back=back[273:488,787:1130]
# back[back>0.9]=0
# io.imshow(back)
# plt.show()
# [xlist,ylist]=[[],[]]
# for y in range(len(back[0])):
#     if sum(back[:,y])<0.2:
#         ylist.append(y)
# for x in range(len(back)):
#     if sum(back[x])<0.2:
#         xlist.append(x)
# print(xlist,'\n',ylist)
import cv2
cv2.imread('backround2.png')