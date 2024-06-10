import numpy as np # linear algebra
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
df = pd.read_csv("D:\\01.한라사랑\\[2]강의 및 토론 특강 방송 기고 상담 TARA#\\[2]제주대학교\\[21]컴퓨터 프로그래밍1-C++\\git_vsc\\oop\\afx\\Iris.csv") 

# 2. 데이터 정보 표시 
print(df.head(5)) # 데이터 프레임에 들어있는 10개 데이터 보여줌.
print("------------------------------") # 데이터에 대한 요약 통계를 보여줌.
print(df.info()) # 데이터에 비어있는(널) 값이 있는지 확인할 수 있음.

# 3. 데이터 전처리
print(df.columns)
df.drop(['Id'],axis=1,inplace=True) # 불필요한 열(ID) 제거: axis=1 : 컬럼, inplace=1 : 삭제 후 데이터 프레임에 반영 
print(df.columns)

# 4. 데이터 시각화 
# 모든 컬럼 쌍에 대해 plot 시각화 - 'Species'에 따라 색을 달리 시각화 
sns.pairplot(df, hue='Species')
plt.show()

# heatmap 표시 - 숫자가 아닌 컬럼은 숫자로 바꾼 후 상관관계 확인
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

df_copy = df.copy()

# 숫자가 아닌 컬럼을 숫자로 바꾸기
le = LabelEncoder()
for col in df.columns:
    if df_copy[col].dtype == 'object':
        df_copy[col] = le.fit_transform(df_copy[col])

plt.figure(figsize=(8, 6))
sns.heatmap(df_copy.corr(), annot=True, cmap='coolwarm')
plt.show()

