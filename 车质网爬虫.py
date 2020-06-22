import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#创建请求的url


def get_page_content(url):
#创建请求头
    header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) App'
                  'leWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
    }

    ##创建get请求
    html=requests.get(url,headers=header,timeout=100)
    # print(html.content.decode('utf-8'))
    # content=html.content.decode('utf-8')
    content=html.text
    # print(html.text)
    soup=BeautifulSoup(content,'html.parser', from_encoding='utf-8')
    return soup
# print(soup)
def analysis(soup):
    temp = soup.find('div',class_="tslb_b")
    # print(temp)
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list=temp.find_all('tr')
    # print(type(tr_list))
    for tr in tr_list:
        temp={}
        td_list=tr.find_all('td')
        # print(td_list)
        if len(td_list)>0:
            id,brand,car_model,type,desc,problem,datetime,status=td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'],temp['problem'],temp['datetime'],temp['status']=id,brand,car_model,type,desc,problem,datetime,status
            df=df.append(temp,ignore_index=True)
    return df

###
result = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
pages=int(input('请输入爬取页数：'))
for i in range(pages):
    url=base_url+str(i+1)+'.shtml'
    soup=get_page_content(url)
    df =analysis(soup)
    result=result.append(df)
    print('爬取第',i+1,'页')

# print(df)
result.to_csv('df.csv')
print('爬取完成')