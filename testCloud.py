# -*-.coding = utf-8 -*-
# @Time : 2020/10/18 10:12
# @Author : 叶福成
# @File : testCloud.py
# @Software: PyCharm

import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud #词云
from PIL import Image #图片处理
import numpy as np #矩阵运算
import sqlite3 #数据库

con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))

img = Image.open(r".\static\assets\img\tree.jpg")
img_array = np.array(img)#将图片转换为数组
wc = WordCloud(
    background_color="white",
    mask=img_array,
    font_path="STXINGKA.TTF"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")#是否显示坐标轴
# 显示输出的词云
# plt.show()
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)


