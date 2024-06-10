import numpy as np # linear algebra
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# 다양한 분류 알고리즘 패키지를 임포트함.
from sklearn.linear_model import LogisticRegression  # Logistic Regression 알고리즘
#from sklearn.cross_validation import train_test_split # 데이타 쪼개주는 모듈 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  # for K nearest neighbours
from sklearn import svm  #for Support Vector Machine (SVM) Algorithm
from sklearn import metrics #for checking the model accuracy
from sklearn.tree import DecisionTreeClassifier #for using Decision Tree Algoithm
from sklearn.preprocessing import LabelEncoder


# 1. 데이터 불러오기
df = pd.read_csv("D:\\01.한라사랑\\[2]강의 및 토론 특강 방송 기고 상담 TARA#\\[2]제주대학교\\[21]컴퓨터 프로그래밍1-C++\\git_vsc\\oop\\afx\\Iris.csv") 

# 2. 데이터 정보 표시 
print(df.head(5)) # 데이터 프레임에 들어있는 10개 데이터 보여줌.
print("------------------------------") # 데이터에 대한 요약 통계를 보여줌.
print(df.info()) # 데이터에 비어있는(널) 값이 있는지 확인할 수 있음.

# 3. 데이터 전처리
df.drop('Id',axis=1,inplace=True) # 불필요한 열(ID) 제거: axis=1 : 컬럼, inplace=1 : 삭제 후 데이터 프레임에 반영 

# 4. 데이터 시각화

# 모든 컬럼 쌍에 대해 plot 시각화 - 'Species'에 따라 색을 달리 시각화 
sns.pairplot(df, hue='Species')
plt.show()

# heatmap 표시 - 숫자가 아닌 컬럼은 숫자로 바꾼 후 상관관계 확인
df_copy = df.copy()

# 숫자가 아닌 컬럼을 숫자로 바꾸기
le = LabelEncoder()
for col in df.columns:
    if df_copy[col].dtype == 'object':
        df_copy[col] = le.fit_transform(df_copy[col])

plt.figure(figsize=(8, 6))
sns.heatmap(df_copy.corr(), annot=True, cmap='coolwarm')
plt.show()

# 5. 데이터 나누기 (학습 데이터, 테스트 데이터)
train, test = train_test_split(df, test_size = 0.3)# in this our main data is split into train and test
train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]# taking the training data features
train_y = train.Species# output of our training data

test_X = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data features
test_y =test.Species   #output value of test data

# 6. 머신러닝 모델 학습 및 테스트 
accuracy_scores = {}

# SVM
model = svm.SVC()
model.fit(train_X,train_y)
prediction=model.predict(test_X)
accuracy_scores['SVM'] = metrics.accuracy_score(prediction,test_y) * 100

# Logistic Regression
model = LogisticRegression()
model.fit(train_X,train_y)
prediction = model.predict(test_X)
accuracy_scores['Logistic Regression'] = metrics.accuracy_score(prediction,test_y) * 100

# Decision Tree
model=DecisionTreeClassifier()
model.fit(train_X,train_y)
prediction=model.predict(test_X)
accuracy_scores['Decision Tree'] = metrics.accuracy_score(prediction,test_y) * 100

# KNN
model=KNeighborsClassifier(n_neighbors=3)
model.fit(train_X,train_y)
prediction=model.predict(test_X)
accuracy_scores['KNN'] = metrics.accuracy_score(prediction,test_y) * 100

# 그래프 그리기
#y축을 50%부터 100%까지로 설정
plt.ylim(50, 100)
plt.bar(accuracy_scores.keys(), accuracy_scores.values())
plt.title('Accuracy of Models')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.show()
