# -*-.coding = utf-8 -*-
# @Time : 2020/10/23 10:16
# @Author : 叶福成
# @File : imgTest.py
# @Software: PyCharm
from PIL import Image
import sqlite3
import numpy as np
from matplotlib import pyplot as plt
from app import movie
import matplotlib.image as mpimg
from requests import request
from PIL import Image
from io import BytesIO
import numpy as np
import urllib


datalist = []
cnn = sqlite3.connect("movie.db")
cur = cnn.cursor()
sql = "select pic_link from movie250"
data = cur.execute(sql)
for item in data:
    datalist.append(item)

cur.close()
cnn.close()

img_src = datalist[1]
# print(img_src)
response = request.post(img_src)
image = Image.open(BytesIO(response.content))
image.show()





