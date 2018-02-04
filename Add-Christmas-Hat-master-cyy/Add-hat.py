# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:49:17 2018

@author: samsung
"""

#给img中的人添加圣诞帽 人脸最好为正脸

import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt

def add_hat(img,hat_img):
    #分离rbga通道，合成rgb三通道的帽子图，a通道后面做mask用
    r,g,b,a=cv2.split(hat_img)
    rgb_hat=cv2.merge((r,g,b))
    #cv2.imwrite("hat_rgb.jpg",rgb_hat)
    #cv2.imwrite("hat_r.jpg",r)
    cv2.imwrite("hat_aplha.jpg",a)
    
    #dlib人脸关键点检测器
    #使用官方提供的训练的模型构建特征提取器
    predictor_path="shape_predictor_5_face_landmarks.dat"
    predictor=dlib.shape_predictor(predictor_path)
    #dlib自带正脸检测器
    detector=dlib.get_frontal_face_detector()
    #正脸检测
    dets=detector(img,1) #1位表示最大限度的采样
    #检测到人脸
    if len(dets)>0:  #len(dets)代表检测到人脸的个数
        for d in dets:
            #left表示人脸左边距离图片左边界的位置right表示人脸右边距离图片左边界的位置
            #top表示人脸上边距离图片上边界的位置bottom表示人脸下边距离图片上边界的位置
            
            x,y,w,h=d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top()
            #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)#?
            
            #人脸关键点检测，使用5个关键点
            shape=predictor(img,d)
            #print(shape)
            #win=dlib.image_window()
            #win.add_overlay(shape)
           
            #选取左右眼中间的点
            point1=shape.part(0)#?
            
            point2=shape.part(2)#？
            
            #point3=shape.part(1)
            #point4=shape.part(3)
            #point5=shape.part(4)
            #print(point1,point2,point3,point4,point5)#五个点的分布是什么？
            #plt.show(point1)
            
            #求两点的中心
            eyes_center=((point1.x+point2.x)//2,(point1.y+point2.y)//2)
            #根据人脸的大小调整帽子的大小?
            factor=1.5#?
            print(rgb_hat.shape[0])
            print(rgb_hat.shape[1])
            resized_hat_h=int(round(rgb_hat.shape[0]*w/rgb_hat.shape[1]*factor))
            resized_hat_w=int(round(rgb_hat.shape[1]*w/rgb_hat.shape[1]*factor))
            if resized_hat_h<y:
                resized_hat_h=y-1
            #根据人脸的大小调整帽子的大小
            resized_hat=cv2.resize(rgb_hat,(resized_hat_w,resized_hat_h))
            #用alpha通道作为mask？
            mask=cv2.resize(a,(resized_hat_w,resized_hat_h))
            mask_inv=cv2.bitwise_not(mask)#?
            #帽子相对于人脸框的上线的偏移量
            dh=0
            dw=0
            #原图的ROI?
            bg_roi=img[y+dh-resized_hat_h:y+dh,(eyes_center[0]-resized_hat_w//3):(eyes_center[0]+resized_hat_w//3*2)]
            #原图ROI中提取帽子的区域
            bg_roi=bg_roi.astype(float)
            mask_inv=cv2.merge((mask_inv,mask_inv,mask_inv))
            alpha=mask_inv.astype(float)/255
            #相乘之前保证两者大小一致（可能会有四舍五入原因不一致）？
            alpha=cv2.resize(alpha,(bg_roi.shape[1],bg_roi.shape[0]))
            bg=cv2.multiply(alpha,bg_roi)
            bg=bg.astype('uint8')
            cv2.imwrite("bg.jpg",bg)
            #提取帽子区域
            hat=cv2.bitwise_and(resized_hat,resized_hat,mask=mask)
            cv2.imwrite("hat.jpg",hat)
            #相加之前保证两者大小一致（可能会有四舍五入原因不一致）？
            hat=cv2.resize(hat,(bg_roi.shape[1],bg_roi.shape[0]))
            #两个ROI区域相加
            add_hat=cv2.add(bg,hat)
            #把添加好的帽子区域放回原图(=左右两边注意不能调换位置)
            img[y+dh-resized_hat_h:y+dh,(eyes_center[0]-resized_hat_w//3):(eyes_center[0]+resized_hat_w//3*2)]=add_hat
            #展示效果
            return img
    #win.add_overlay(dets)    
#读取帽子图，第二个参数-1表示rgba通道，否则为rgb通道
hat_img=cv2.imread("hat2.png",-1)
#读取头像图
img=cv2.imread("test.jpg")
output=add_hat(img,hat_img)
#展示效果
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.imwrite("output.jpg",output)
cv2.destroyAllWindows()
            
    
    
