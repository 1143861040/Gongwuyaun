# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import numpy as np
from os import path
import pandas as pd
import re
import requests
from scipy.misc import imread
import time
from wordcloud import WordCloud,ImageColorGenerator
'''
# 从新闻网站爬取若干新闻标题信息并进行解析
def fetch_sina_news():
    PATHERN=re.compile('.shtml"target="_blank">(.*?)</a><span>(.*?)</span></li>')
    BASE_URL="http://roll.news.sina.com.cn/news/gnxw/gdxwl/index_"
    MAX_PAGE_NUM=6
    
    with open('subject.txt','w',encoding='utf-8')as f:
        for i in range(1,MAX_PAGE_NUM):
            print('Downloding page#{}'.format(i))
            r=requests.get(BASE_URL)+str(i)+'.shtml'
            r.encoding='gb2312'
            data=r.text
            p=re.findall(PATHERN,data)
            for s in p:
                f.write(s[0])
            time.sleep(5)
'''

            
def extract_words():
   # with open('subject.txt','r',encoding='utf-8')as f:
    #    news_subjects=f.readlines()
    
    with open('subject1.txt','r',encoding='gb2312')as f:
        news_subjects=f.readlines()
    print (news_subjects)
    #news_subjects=(line.strip() for line in open('stopwords.txt',encoding='utf-8'))
    #print (''.join(news_subjects))
    
    #去除停用词 例如“的”，“我们”
    stop_words=set(line.strip() for line in open('stopwords.txt',encoding='utf-8')) 
    #print(stop_words)
    newslist=[]
    #for subject in news_subjects:
    for subject in news_subjects:
        if subject.isspace():#？
            continue
            
        #segment words line by line
        word_list=pseg.cut(subject)
        #print (word_list)
        for word,flag in word_list:
            if not word in stop_words and flag=='n':
                newslist.append(word)
    
    print (newslist)#分成一个一个的字词   
    d=path.dirname(__file__)
    mask_image=imread(path.join(d,"mickey.png"))
       
    content=','.join(newslist)
    print(content)
    wordcloud=WordCloud(font_path='simhei.ttf',background_color='grey',
                        mask=mask_image,max_words=100).generate(content)
    image_colors=ImageColorGenerator(mask_image)
    #Display the generated image；
    plt.imshow(wordcloud.recolor(color_func=image_colors),interpolation="bilinear")
    plt.axis('off')
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
        
if __name__=="__main__":
    #fetch_sina_news()
    extract_words()
        
            
