#coding=utf-8
import os
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw


class BlackPlate:
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/black_bg.png")), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        return cv2.cvtColor(cv2.bitwise_or(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (255, 255, 255),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (0, 0, 0)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img

class YellowPlate:
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/yellow_bg.png")), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        # return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 0),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img

class BluePlate:
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/blue_bg.png")), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        return cv2.cvtColor(cv2.bitwise_or(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (255, 255, 255),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (0, 0, 0)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img

def load_font():
    return {
        "京": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne000.png")),
        "津": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne001.png")),
        "冀": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne002.png")),
        "晋": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne003.png")),
        "蒙": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne004.png")),
        "辽": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne005.png")),
        "吉": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne006.png")),
        "黑": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne007.png")),
        "沪": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne008.png")),
        "苏": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne009.png")),
        "浙": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne010.png")),
        "皖": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne011.png")),
        "闽": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne012.png")),
        "赣": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne013.png")),
        "鲁": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne014.png")),
        "豫": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne015.png")),
        "鄂": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne016.png")),
        "湘": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne017.png")),
        "粤": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne018.png")),
        "桂": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne019.png")),
        "琼": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne020.png")),
        "渝": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne021.png")),
        "川": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne022.png")),
        "贵": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne023.png")),
        "云": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne024.png")),
        "藏": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne025.png")),
        "陕": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne026.png")),
        "甘": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne027.png")),
        "青": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne028.png")),
        "宁": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne029.png")),
        "新": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne030.png")),
        "A": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne100.png")),
        "B": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne101.png")),
        "C": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne102.png")),
        "D": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne103.png")),
        "E": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne104.png")),
        "F": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne105.png")),
        "G": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne106.png")),
        "H": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne107.png")),
        "J": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne108.png")),
        "K": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne109.png")),
        "L": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne110.png")),
        "M": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne111.png")),
        "N": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne112.png")),
        "P": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne113.png")),
        "Q": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne114.png")),
        "R": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne115.png")),
        "S": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne116.png")),
        "T": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne117.png")),
        "U": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne118.png")),
        "V": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne119.png")),
        "W": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne120.png")),
        "X": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne121.png")),
        "Y": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne122.png")),
        "Z": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne123.png")),
        "0": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne124.png")),
        "1": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne125.png")),
        "2": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne126.png")),
        "3": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne127.png")),
        "4": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne128.png")),
        "5": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne129.png")),
        "6": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne130.png")),
        "7": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne131.png")),
        "8": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne132.png")),
        "9": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne133.png"))
    }


class GreenPlate:
    _font = load_font()
    _bg = [
        cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/green_bg_0.png")), (480, 140)),
        cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/green_bg_1.png")), (480, 140))
    ]

    def __call__(self, plate, bg=0):
        if len(plate) != 8:
            print("ERROR: Invalid length")
            return None
        try:
            fg = self._draw_fg(plate)
            return cv2.cvtColor(cv2.bitwise_and(fg, self._bg[bg]), cv2.COLOR_BGR2RGB)
        except KeyError:
            print("ERROR: Invalid character")
            return None
        except IndexError:
            print("ERROR: Invalid background index")
            return None

    def _draw_char(self, ch):
        return cv2.resize(self._font[ch], (43 if ch.isupper() or ch.isdigit() else 45, 90))

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (480, 140), (255, 255, 255)))
        offset = 15
        img[25:115, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 9
        img[25:115, offset:offset+43] = self._draw_char(plate[1])
        offset = offset + 43 + 49
        for i in range(2, len(plate)):
            img[25:115, offset:offset+43] = self._draw_char(plate[i])
            offset = offset + 43 + 9
        return img
    # def _draw_fg(self, plate):
    #     img = np.array(Image.new("RGB", (480, 140), (255, 255, 255)))
    #     offset = 15
    #     img[25:115, offset:offset+45] = self._draw_char(plate[0])
    #     offset = offset + 45 + 9
    #     img[25:115, offset:offset+45] = self._draw_char(plate[1])
    #     offset = offset + 45 + 49
    #     for i in range(2, len(plate)):
    #         img[25:115, offset:offset+45] = self._draw_char(plate[i])
    #         offset = offset + 45 + 9
    #     return img


class WhitePlate:
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/white_bg.jpg")), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        # cv2.imwrite("12.jpg",fg)
        # return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 0),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_char_last(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 255),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 34
        for i in range(1, len(plate)-1):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char_last(plate[-1])
        # img[0:140, offset:offset+45] = self._draw_char(plate[i])
        offset = offset + 45 + 12
        return img

class SpecialPlate:
    #军牌，武警车牌
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/sp_bg.jpg")), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        # cv2.imwrite("12.jpg",fg)
        # return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 0),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_char_last(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 255),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char_last(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char_last(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)-1):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[-1])
        # img[0:140, offset:offset+45] = self._draw_char(plate[i])
        offset = offset + 45 + 12
        return img
class RedPlate:
    #为了解决默写场景，红灯照射黄色车牌，导致车牌变红，网络无法识别的情况
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/yellow_bg.png")), (440, 140))
    _bg[:,:,1] =_bg[:,:,1]*1.3

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        # return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 0),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img
        
class RedPlate1:
    #为了解决某些场景，红灯照射蓝色车牌，导致车牌变红，网络无法识别的情况
    _font = [
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/eng_92.ttf"), 126),
        ImageFont.truetype(os.path.join(os.path.dirname(__file__), "res/zh_cn_92.ttf"), 95)
    ]
    _bg = cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/blue_bg.png")), (440, 140))
    _bg[:,:,0] =_bg[:,:,0]*0.2

    def __call__(self, plate):
        if len(plate) != 7:
            print("ERROR: Invalid length")
            return None
        fg = self._draw_fg(plate)
        return cv2.cvtColor(cv2.bitwise_or(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 95, 140), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, -11 if ch.isupper() or ch.isdigit() else 3), ch,
            fill = (0, 0, 255),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (0, 0, 0)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img
