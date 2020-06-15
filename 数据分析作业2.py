import pandas as pd
from pandas import Series,DataFrame
import numpy as np

print('***************问题1：求100以内偶数和*************************')
sr1=Series(range(2,102,2))
# print(sr1)
sum=sum(sr1)
print('2+4+6...+100=',sum)

print('***************问题2：统计全班的成绩*************************')

#打印提示
print('班级成绩表：')

###创建Dataframe数据结构
data=[[68,65,30],[95,76,98],[98,86,88],[90,88,77],[80,90,90]]
df1=DataFrame(data=data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
df1.index.name='姓名'
print(df1)

####进行数据统计及简单分析
print('各科的平均成绩：')
print(df1[['语文','数学','英语']].mean())

print('各科的最大成绩：')
print(df1.iloc[:].max())
print('各科的最小成绩：')
print(df1.loc[:].min())
print('各科成绩的方差：')
print(df1.loc[:,['语文','数学','英语']].var())
print('各科成绩的标准差：')
print(df1.iloc[[0,1,2,3,4],[0,1,2]].std())
print('**************五人的总成绩排名--->降序*********')
df1['sum']=df1.apply(np.sum,axis=1)
print(df1.sort_values(by='sum',ascending=False))