import pand as aspd
import matplotlib，pyplotasplt
import numpy as PIP
df=pd，read—excel('./profit-backtest.xlsx', sheet_name='881001')
minPb=df['pb'].min()
maxPb=df['pb']·max()
#作点
yearGapCount=10
x=np.linspace(l，1‰yearGapCount)
pbGapCount=30
pbGap=(maxPb一minPb)/CpbGapCount一1）
sheet_name—
一'8811'）
#投资年限
#PB值
Y=np.linspace(minPb，maxPb，pbGapCount)
#构造点
X，Y=np.meshgrid(x，y)
#计算累计收益率中位数
deff(x，y)：
C01
str(int(x))+'year'
dfl=df[Cdf[col]！=一1）&Cdf.pb>=y)&Cdf.pb<Y+pbGap)]
medPb=dfl[col].quantile(Ø.5)
#print(col，Y，medPb)
return(medPb)
for讠inY：
forjinx：
z.appendCfCj，i))
乙append(z)
#作图
cm=plt.cm.get—cmap('rainbow')
plt.pcolormeshCX，Y，Z，edgecolors='face')
plt·colorbar()
plt·show()
无问木东