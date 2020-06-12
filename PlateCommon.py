#coding=utf-8
import os
import random
import numpy as np
import cv2
from PIL import Image
from PIL import ImageDraw
from math import *

INDEX_PROVINCE = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10,
                  "浙": 11, "皖": 12, "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20,
                  "琼": 21, "川": 22, "贵": 23, "云": 24, "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30}

INDEX_DIGIT = {"0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36, "6": 37, "7": 38, "8": 39, "9": 40}

INDEX_LETTER = {"A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47,"H": 48, "J": 49, "K": 50, "L": 51, "M": 52,
                "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60, "W": 61, "X": 62, "Y": 63, "Z": 64}

PLATE_CHARS_PROVINCE = {"京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑",
                        "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤",
                        "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"}

PLATE_CHARS_DIGIT = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

PLATE_CHARS_LETTER = {"A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P",
                      "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

index = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10, "浙": 11, "皖": 12,
         "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20, "琼": 21, "川": 22, "贵": 23, "云": 24,
         "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30, "0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36,
         "6": 37, "7": 38, "8": 39, "9": 40, "A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48,
         "J": 49, "K": 50, "L": 51, "M": 52, "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60,
         "W": 61, "X": 62, "Y": 63, "Z": 64}

chars = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂",
         "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

def AddSmudginess(img, Smu):
    img_h, img_w = img.shape[:2]
    rows = r(Smu.shape[0] - img_h)

    cols = r(Smu.shape[1] - img_w)
    adder = Smu[rows:rows + img_h, cols:cols + img_w]
    adder = cv2.resize(adder, (img_w, img_h))
    adder = cv2.bitwise_not(adder)
    #   adder = cv2.bitwise_not(adder)
    # img = cv2.resize(img,(50,50))
    # img = cv2.bitwise_not(img)
    # img = cv2.bitwise_and(adder, img)
    # img = cv2.bitwise_not(img)
    val = random.random() * 0.5
    img = cv2.addWeighted(img, 1 - val, adder, val, 0.0)
    return img

def rot(img,angel,shape,max_angel):
    size_o = [shape[1],shape[0]]
    # print size_o
    # size = (shape[1]+ int(shape[0]*cos((float(max_angel )/180) * 3.14)),shape[0])
    # print size
    size = (shape[1]+ int(shape[0]*sin((float(max_angel )/180) * 3.14)),shape[0])
    # print size
    interval = abs( int( sin((float(angel) /180) * 3.14)* shape[0]))

    pts1 = np.float32([[0,0],[0,size_o[1]],[size_o[0],0],[size_o[0],size_o[1]]])
    if(angel>0):
        pts2 = np.float32([[interval,0],[0,size[1]  ],[size[0],0  ],[size[0]-interval,size_o[1]]])
    else:
        pts2 = np.float32([[0,0],[interval,size[1]  ],[size[0]-interval,0  ],[size[0],size_o[1]]])

    M  = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,size)

    return dst

def rotRandrom(img, factor, size):
    shape = size
    pts1 = np.float32([[0, 0], [0, shape[0]], [shape[1], 0], [shape[1], shape[0]]])
    pts2 = np.float32([[r(factor), r(factor)],
                        [ r(factor), shape[0] - r(factor)],
                        [shape[1] - r(factor), r(factor)],
                        [shape[1] - r(factor), shape[0] - r(factor)]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, size)
    return dst

def tfactor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hsv[:,:,0] = hsv[:,:,0]*(0.8+ np.random.random()*0.2)
    hsv[:,:,1] = hsv[:,:,1]*(0.3+ np.random.random()*0.7)
    hsv[:,:,2] = hsv[:,:,2]*(0.2+ np.random.random()*0.8)

    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    return img

def random_envirment(img,data_set):
    index=r(len(data_set))
    env = cv2.imread(data_set[index])
    env = cv2.resize(env,(img.shape[1],img.shape[0]))

    # bak = (img==0);
    # bak = bak.astype(np.uint8)*255;
    # inv = cv2.bitwise_and(bak,env)
    # img = cv2.bitwise_or(inv,img)
    val = random.random() * 0.4
    img = cv2.addWeighted(img, 1 - val, env, val, 0.0)
    return img

def random_scene(img, data_set):
    files = os.listdir(data_set)
    file = random.choice(files)
    bg_img_path = os.path.join(data_set,file)

    env = cv2.imdecode(np.fromfile(bg_img_path,dtype=np.uint8),-1)
    if env is None:
        print(bg_img_path + ' is not a good file')
        return None, None
    width = random.randint(130,190)
    # int(img.shape[1]/img.shape[0]*new_height)
    img = cv2.resize(img,(width,int(img.shape[0]/img.shape[1]*width)))
    x = int(r(env.shape[1] - img.shape[1]))
    y = int(r(env.shape[0] - img.shape[0]))
    new_height = img.shape[0]
    new_width = img.shape[1]
    env[y:y+new_height, x:x+new_width, :] = img[:,:,:]

    
    x1= random.randint(x-30,x+10)
    y1 = random.randint(y-20,y+10)
    # y1 = y+20
    if x1<0:
        x1 = 0
    if y1<0:
        y1 = 0
    x2 = random.randint(x+img.shape[1]-4,x+img.shape[1]+20)
    y2 = random.randint(y+img.shape[0]-4,y+img.shape[0]+20)
    # print(w1,h1)
    env = env[y1:y2, x1:x2,:]
 
    print(x, y, x + img.shape[1], y + img.shape[0])
    return env,(x, y, x + img.shape[1], y + img.shape[0])
        


def random_scene_old(img, data_set):
    files = os.listdir(data_set)
    print(data_set)
    file = random.choice(files)
    print(file)

    bg_img_path = os.path.join(data_set,file)

    env = cv2.imread(bg_img_path)
    if env is None:
        print(bg_img_path + ' is not a good file')
        return None, None
 
    scale = random.uniform(0.5,0.95)
    new_width = int(env.shape[1]*scale) #int(new_width * scale + 0.5)
    new_height = int(env.shape[0]*scale)#int(new_height * scale + 0.5)
    img = cv2.resize(img, (new_width, new_height))
    print(scale,new_width, new_height)
    # img = cv2.resize(img, (220, 70))
    # if env.shape[1] <= img.shape[1] or env.shape[0] <= img.shape[0]:
    #     # print env.shape, '---', img.shape
    #     return None, None
    x = r(env.shape[1] - img.shape[1])
    y = r(env.shape[0] - img.shape[0])
    # bak = (img==0)
    # cv2.imwrite("000.jpg",img)
    # bak = bak.astype(np.uint8)*255
    # inv = cv2.bitwise_and(bak, env[y:y+new_height, x:x+new_width, :])
    # cv2.imwrite("111.jpg",inv)
    # img = cv2.bitwise_or(inv, img)
    # cv2.imwrite("222.jpg",img)
    env[y:y+new_height, x:x+new_width, :] = img[:,:,:]
    print("11111",x, y, x + img.shape[1], y + img.shape[0])
    if random.random()<1:
        x1= random.randint(0,x+10)
        y1 = random.randint(0,y+15)
        # y1 = y+20
        w1 = random.randint(x + img.shape[1]-4,env.shape[1])
        h1 = random.randint(y + img.shape[0]-4,env.shape[0])
        print(w1,h1)
        env = env[y1:y1+h1, x1:x1+w1, :]
        # return env, (x, y, x + img.shape[1], y + img.shape[0])
        print(x, y, x + img.shape[1], y + img.shape[0])
        return env,(x, y, x + img.shape[1], y + img.shape[0])
        


    return env, (x, y, x + img.shape[1], y + img.shape[0])



dangerous_path = []
for parent, _, filenames in os.walk("./dangerous"):
    for filename in filenames:
        dangerous_path.append(parent + "/" + filename)





def random_scene_dangerous(img, data_set):
    

    dangerous_img =cv2.imread(random.choice(dangerous_path))
    files = os.listdir(data_set)
    print(data_set)
    file = random.choice(files)
    # print(file)
    print(11111)
    bg_img_path = os.path.join(data_set,file)
    env = cv2.imdecode(np.fromfile(bg_img_path,dtype=np.uint8),-1)
    # env = cv2.imread(bg_img_path)
    if env is None:
        print(bg_img_path + ' is not a good file')
        return None, None
    x = int(r(env.shape[1] - img.shape[1]))
    y = int(r(env.shape[0] - img.shape[0]))
    new_width = int(dangerous_img.shape[1]) #int(new_width * scale + 0.5)
    new_height = int(dangerous_img.shape[0])#int(new_height * scale + 0.5)
    dangerous_img = cv2.resize(dangerous_img, (new_width, new_height))


    env[y:y+new_height, x:x+new_width, :] = dangerous_img[:,:,:]

    cv2.imwrite("tt.jpg",env)
    
    img_width = int(img.shape[1]/img.shape[0]*new_height)
    img_height = new_height
    print(img_width, img_height)
    img = cv2.resize(img, (img_width, img_height))
    print(img.shape)
    xx = x+new_width
    env[y:y+img.shape[0], xx:xx+img.shape[1],:] = img[:,:,:]
    # print("11111",x, y, x + img.shape[1], y + img.shape[0])
    print(3333)
    x1= random.randint(x,x+new_width)
    y1 = random.randint(y-20,y)
    if y1<0:
        y1=0
    delta = random.randint(0,20)
    env = env[y1:y+new_height+delta, x1:random.randint(x+new_width+img_width,x+new_width+img_width+20),:]
    # return env, (x, y, x + img.shape[1], y + img.shape[0])
    print(x, y, x + img.shape[1], y + img.shape[0])
    return env,(x, y, x + img.shape[1], y + img.shape[0])



def GenCh(f,val):
    img=Image.new("RGB", (45,70),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 3),val,(0,0,0),font=f)
    img = img.resize((23,70))
    A = np.array(img)
    return A

def GenCh1(f,val):
    img=Image.new("RGB", (23,70),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 2),val,(0,0,0),font=f)
    A = np.array(img)
    return A

def AddGauss(img, level):
    # return cv2.blur(img, (level * 2 + 1, level * 2 + 1))
    return cv2.blur(img, (1+r(level), 1+r(level)))

def r(val):
    return int(np.random.random() * val)

def AddNoiseSingleChannel(single):
    diff = 255-single.max()
    noise = np.random.normal(0,1+r(6),single.shape)
    noise = (noise - noise.min())/(noise.max()-noise.min())
    noise= diff*noise
    noise= noise.astype(np.uint8)
    dst = single + noise
    return dst

def addNoise(img,sdev = 0.5,avg=10):
    img[:,:,0] =  AddNoiseSingleChannel(img[:,:,0])
    img[:,:,1] =  AddNoiseSingleChannel(img[:,:,1])
    img[:,:,2] =  AddNoiseSingleChannel(img[:,:,2])
    return img