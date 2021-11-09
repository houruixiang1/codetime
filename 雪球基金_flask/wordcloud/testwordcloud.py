
import pymysql
import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算

# #准备词云所需的文字（词）
# host = 'localhost'
# user = 'root'
# password = '123456'
# db = '雪球基金'
# port = 3306
# db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
# cursor = db.cursor()
# sql = "select name from 雪球基金"
# cursor.execute(sql)
# text = ""
# for item in cursor.fetchall():
#     text =  text + item[0]
#     #print(item[0])
# #print(text)
# db.commit()
# db.close()
with open(r'C:\CodeTime\flasktest\static\test.txt',mode='r',encoding='utf-8')as f:
    text = f.read()
#分词
seg = jieba.cut(text)
with open(r'C:\CodeTime\flasktest\wordcloud\stop_words.txt', "r", encoding="utf-8") as f:
    stop_words = [w.split("\n")[0] for w in f.readlines()]
    # 去重
    stop_words = set(stop_words)
# 去除停用词
word_list = []
for w in seg:
    if w and (not w in stop_words):
        word_list.append(w)
string = ' '.join(word_list)
print(len(string))


img = Image.open(r'C:\CodeTime\flasktest\static\assets\img\tree.jpg')   #打开遮罩图片
img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="simhei.ttf"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

#plt.show()    #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'C:\CodeTime\flasktest\static\assets\img\test.jpg',dpi=500)
print("词云图生成成功！！！")

















