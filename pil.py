# 适合能获得完整背景图情况
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters,io,measure,color
import os
def showimg(img):
    io.imshow(img)
    plt.show()
def get_x(img,ran_ge):
    for x in ran_ge:
        if sum(img[x])>20:
            return x
def get_y(img,ran_ge):
    for y in ran_ge:
        if sum(img[:,y])>20:
            return y
# 获取左右以及上下边界，把>0.9的白色周围部分去除，获取单纯的内容图片
def get_pure_img(img):
    img[img>0.9]=0
    x0=get_x(img,range(len(img)))
    x1=get_x(img,range(len(img)-1,-1,-1))
    y0=get_y(img,range(len(img[0])))
    y1=get_y(img,range(len(img[0])-1,-1,-1))
    return img[x0:x1,y0:y1]
#获取与当前截屏图片对应的背景图
def ensure_back(img):#返回pure 背景图
    # 获取背景图文件夹中所有图片路径
    root_path=os.getcwd()+'/background/'
    img_files=os.listdir(root_path)
    for im in img_files:
        open_img=io.imread(root_path+im,as_gray=True)
        # 去除背景图白边
        open_img=get_pure_img(open_img)
        # 对比两个图片的相似度，因为去除白边后会有几个像素大小的宽度以及高度不相同，统一对比宽195长320部分
        if measure.compare_ssim(open_img[:195,:320],img[:195,:320])>0.75:#阈值选择要合适
            return open_img
def compare(screenshot,background):#对比两个pure
    # showimg(screenshot)
    # showimg(background)
    # 同样因为维度问题，截取传入图片的固定部分做差值。
    new=background[:180,:250]-screenshot[:180,:250]
    # 缺口部分差值差不多为0.2,0.4左右，将>0.8和<0.1部分变黑，二值化，其余为1
    new[new>0.8]=0
    new=np.where(new>0.1,1,0)
    # showimg(new)
    # y方向遍历列，其他部分大部分是黑色值为0，因此存在一行及其往后4行和大于120可以认为是缺口
    for i in range(len(new[0])):
        if new[:180,i:i+4].sum()>120:
            return i


def m():
    # 获取全屏截图中有效部分
    screenshot=io.imread('screenshot.png',as_gray=True)[273:488,787:1130]#参数待定
    # showimg(screenshot)
    # 预处理两个图片
    screenshot=get_pure_img(screenshot)
    background=ensure_back(screenshot)
    dark=0
    # 可移动的方块初始位置是固定的，因此从70往后找到阴影部分缺口即可
    try:
        dark=compare(screenshot[:,70:], background[:,70:])
    except:
        print(type(screenshot),type(background))
    # 截屏出来的图片像素大小是330左右，但是网页上是160*260，等比例缩小移动距离
    return (dark+63)*260/328
    # print(dark+70)





if __name__ == '__main__':
    # screenshot_new=get_pure_img(screenshot)
    # background_new=get_pure_img(background)
    m()

