import threading  # 多线程
import json  # json解析
import requests  # 请求
from PIL import Image  # 图片处理
from io import BytesIO  # 二进制处理
from playsound import playsound  # 音频播放
import os  # 临时文件
import sys
from PyQt6 import QtCore, QtGui, QtWidgets


def getVoice(word):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    # 1是英音，2是美音
    voiceUrl = f"https://dict.youdao.com/dictvoice?audio={word}&type=2"
    tmp_file = 'tmp_voice.mp3'
    tmp_path = os.path.join(curr_path, tmp_file)
    voiceRes = requests.get(voiceUrl)
    voice = voiceRes.content
    f = open(tmp_file, 'wb')
    f.write(voice)
    f.close()
    for i in range(3):
        playsound(tmp_path)
    os.remove(tmp_path)


def getImg(word):
    url = f"https://cn.bing.com/images/vsasync?q={word}"
    res = requests.get(url)
    response = json.loads(res.text)
    result = response["results"]
    imgList = []
    for i in result:
        imgList.append(i["imageUrl"])
        if len(imgList) > 2:
            break
    for imgUrl in imgList:
        imgRes = requests.get(imgUrl)
        image = Image.open(BytesIO(imgRes.content))
        image.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    hello_widget = QtWidgets.QWidget()
    hello_widget.resize(280, 150)
    hello_widget.setWindowTitle("English Words Searching")

    hello_label = QtWidgets.QLabel(hello_widget)
    hello_label.setText("hello pyqt5")

    hello_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # word = input("请输入要查询的单词：")
    # t1 = threading.Thread(target=getVoice, args=(word,))
    # t2 = threading.Thread(target=getImg, args=(word,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    main()
