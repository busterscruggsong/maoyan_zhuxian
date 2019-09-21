import csv
import jieba # 分词
from wordcloud import WordCloud # 词云
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("ticks") # 设置绘图风格
plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文标签
plt.rcParams['axes.unicode_minus']= False # 解决保存图像是负号'-'，显示为方块的问题

def pie(data=None,title=None,length=6,height=6,dpi=100):
    # 绘制饼图函数
    fig, ax = plt.subplots(figsize=(length, height), dpi=dpi)
    size = 0.5
    labels = data.index
    ax.pie(data, labels=labels,
           startangle=90, autopct='%.1f%%', colors=sns.color_palette("husl", len(data)),
           radius=1, # 控制饼图半径，默认为1
           pctdistance=0.75, # 控制百分比显示位置
           wedgeprops=dict(width=size, edgecolor='w'), # 控制甜甜圈的厚度，边缘颜色等
           textprops=dict(fontsize=10) # 控制字号及颜色等
           )
    ax.set_title(title, fontsize=15)
    plt.show()
    
if __name__ == '__main__':
    # 1.数据采集
    # get_json_data()
    # 2.数据分析
    df = pd.read_csv('zhuxian.csv',encoding='gbk')
    # print(df)
    # 数据清洗
    # 数据处理
    # 1.观看人群性别
    gender = df['gender'].value_counts().sort_index(ascending=1)
    print(gender)
    gender_title = '观看人群性别比'
    pie(gender,gender_title)
    # 2.评分情况
    score = df['score'].value_counts().sort_index(ascending=1)
    print(score)
    score_title = '评分占比情况'
    pie(score, score_title)

    # 3.影评分析
    df['comment'].to_csv('zhuxian.txt', index=False)
    f = open('zhuxian.txt','r',encoding='utf-8')
    txt = f.read()
    f.close()
    words = jieba.lcut(txt)
    # print(words)
    nettxt = ' '.join(words)
    # print(nettxt)
    wordcloud = WordCloud(background_color='white',width=800,height=600,font_path='msyh.ttc',max_words=200,max_font_size=80).generate(nettxt)
    wordcloud.to_file('诛仙评论词云.png')
