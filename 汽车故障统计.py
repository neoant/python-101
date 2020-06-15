import pandas as pd
from pandas import Series,DataFrame

df1=pd.read_csv(r'C:\mypython\peixun\Data_Engine_with_Python-master\L1\car_data_analyze\car_complain.csv')
print(df1)
print(type(df1))
##########数据预处理-->删除problem列-->对problem列进行逗号拆分########get_dummies是按照分割列的数据内容进行0/1填充，列名是原数据内容
###########split是对分割列进行分割，填充内容是列原本的内容
# problem_split=df1['problem'].str.split(',',expand=True)
# df1=df1.drop(columns='problem').join(problem_split)
# df1.to_csv('fenge.csv')

problem_get_dummies=df1['problem'].str.get_dummies(',')
# print(problem_get_dummies)
df1=df1.drop(columns='problem').join(problem_get_dummies)
print(df1)
###############按品牌分组，统计投诉总数###########
df2=df1.groupby(by=['brand'])['id'].agg(['count'])
print('按照品牌进行投诉总数统计：')
print(df2)
print('每一类投诉的总数统计：')
df3=df1.groupby(by='brand')[df1.columns[7:]].agg(['sum'])
print(df3)

#合并表
print('****************按照故障总数进行排序--->降序**************')
df4=pd.merge(df2,df3,how='left',left_index=True, right_index=True)
# print(df4)
print(df4.sort_values(by='count',ascending=False))

print('*****************按照某一类故障进行排序---->降序***********')

df4.to_csv('df4.csv')

print(df4.sort_values(by=('A11','sum'),ascending=False))