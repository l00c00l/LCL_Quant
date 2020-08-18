import pandas as pd

import numpy as np

year_list=[]

month_list=[]

rtn_list=[]

# 生成对数收益率，以半年为周期

for year in range(2006,2017):

    for month in [6,12]:

        year_list.append(year)

        month_list.append(month)

        rtn=round((-1)**(month/6)*(month/6/10),3)+(np.random.random()-0.5)*0.1

        rtn_list.append(rtn)

# 生成半年为周期的收益率df

df=pd.DataFrame()

df['year']=year_list

df['month']=month_list

df['rtn']=rtn_list


round(df['rtn'].mean()/df['rtn'].std()*np.sqrt(2),3)
# 生成每年的收益数据df_year（对数收益率可以直接相加）
df_year=df.groupby(['year']).sum()
del df_year['month']
round(df_year['rtn'].mean()/df_year['rtn'].std(),3)