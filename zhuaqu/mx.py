import pandas as pd
filename='D:\pytho\pytho01.xls'
data=pd.read_excel(filename)
x=data.iloc[:,:8].as_matrix()
y=data.iloc[:,8].as_matrix()
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
rlr=RLR()
rlr.fit(x,y)
rlr.get_support()
print('通过随机逻辑模型筛选特征结束')
print('有效特征位: %s' % ','.join(data.columns[rlr.get_support()]))
x=data[data.columns[rlr.get_support()]].as_matrix()
lr=LR()
lr.fit(x,y)
print('逻辑回归模型训练结束')
print('模型的平均正确率：%s' % lr.score(x,y))
