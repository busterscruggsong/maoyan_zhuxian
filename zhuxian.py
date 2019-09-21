import io
import sys
import requests
import json
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') # 改变标准输出的默认编码

def save_data(data):
    with open('zhuxian.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        title = ['gender', 'score', 'content', 'upCount', 'userLevel']
        writer.writerow([data[i] for i in title])

# 数据解析
def parse_json(text):
    data = {}
    content= json.loads(text)
    # print(content)
    comments= content['data'].get('comments')
    # print(comments)
    for i in comments:
        data['gender'] = i.get('gender')
        data['score'] = i.get('score')
        data['content'] = i.get('content')
        data['upCount'] = i.get('upCount')
        data['userLevel'] = i.get('userLevel')
        # 4.保存数据
        save_data(data)
    print('*' * 10 + '保存完毕' + '*' * 10)

# 数据获取
def get_json_data():
    # 1.目标url
    for k in range(0, 901, 15):
        url = 'http://m.maoyan.com/review/v2/comments.json?movieId=360504&userId=-1&offset=%s&limit=15&ts=1569057424639&type=3'% k
    # 2.发送请求
        response = requests.get(url)
        # print(response.text)
        # 3.解析网页
        parse_json(response.text)


if __name__ == '__main__':
    # 1.数据采集
    get_json_data()
