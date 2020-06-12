#coding=utf-8
import random
import numpy as np

from PlateCommon import *

if __name__ == "__main__":
    import all_kinds_plate
else:
    from . import all_kinds_plate


def aug_generate(com):

    # cv2.imwrite('03.jpg', com)
    com = rot(com, r(20)-10, com.shape, 10) # 矩形-->平行四边形
    # cv2.imwrite('04.jpg', com)
    com = rotRandrom(com, 5, (com.shape[1], com.shape[0])) # 旋转
    # cv2.imwrite('05.jpg', com)
    com = tfactor(com) # 调灰度
    # cv2.imwrite('06.jpg', com)

    com, loc = random_scene(com, "./background")    # 放入背景中
    # com,loc = random_scene_dangerous(com,"./dangerous_background") #针对黄牌大货车带危险品字样识别不好的情况进行特点生成
    if com is None or loc is None:
        return None, None
    # cv2.imwrite('07.jpg', com)
    com = AddGauss(com, 5) # 加高斯平滑
    # cv2.imwrite('08.jpg', com)
    com = addNoise(com)         # 加噪声
    # cv2.imwrite('09.jpg', com)
    return com, loc





class Draw:
    _draw = [
        all_kinds_plate.BlackPlate(),
        all_kinds_plate.BluePlate(),
        all_kinds_plate.GreenPlate(),
        all_kinds_plate.YellowPlate(),
        all_kinds_plate.WhitePlate(),
        all_kinds_plate.SpecialPlate(),
        all_kinds_plate.RedPlate(),
        all_kinds_plate.RedPlate1(),
    ]
    _provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"]
    _alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    _ads = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __call__(self):
        draw = random.choice(self._draw)
        candidates = [self._provinces, self._alphabets]
        if type(draw) == all_kinds_plate.GreenPlate:
            candidates += [self._ads] * 6
            label = "".join([random.choice(c) for c in candidates])
            return draw(label, random.randint(0, 1)), label
        elif type(draw) == all_kinds_plate.BlackPlate:
            if random.random() < 0.5:
                candidates += [self._ads] * 4
                candidates += [["港", "澳"]]
            else:
                candidates += [self._ads] * 5
            label = "".join([random.choice(c) for c in candidates])
            return draw(label), label
        elif type(draw) == all_kinds_plate.YellowPlate:
            if random.random() < 0.1:
                candidates += [self._ads] * 4
                candidates += [["学"]]
            else:
                candidates += [self._ads] * 5
            label = "".join([random.choice(c) for c in candidates])
            return draw(label), label
        elif type(draw) == all_kinds_plate.WhitePlate:
            candidates += [self._ads] * 4
            candidates += [["警"]]
            label = "".join([random.choice(c) for c in candidates])
            return draw(label), label
        elif type(draw) == all_kinds_plate.SpecialPlate:
            candidates = [self._alphabets, self._alphabets]
            candidates += [self._ads] * 5
            label = "".join([random.choice(c) for c in candidates])
            return draw(label), label
        else:
            candidates += [self._ads] * 5
            label = "".join([random.choice(c) for c in candidates])
            return draw(label), label


if __name__ == "__main__":
    import math
    import argparse
    import matplotlib.pyplot as plt
    import cv2
    parser = argparse.ArgumentParser(description="Random generate all kinds of chinese plate.")
    parser.add_argument("--num", help="set the number of plates (default: 9)", type=int, default=9)
    parser.add_argument("--savepath", help="savepath", type=str, default="./out")
    args = parser.parse_args()

    draw = Draw()
    for i in range(args.num):
        plate, label = draw()
        print(label)
        img = cv2.cvtColor(plate,cv2.COLOR_RGB2BGR)
        img,loc = aug_generate(img)
        path = os.path.join(args.savepath,label+".jpg")
        cv2.imwrite(path,img)