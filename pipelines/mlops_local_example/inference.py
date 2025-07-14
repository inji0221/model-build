# inference.py
import pandas as pd
import joblib

# 테스트 데이터 준비 (여기선 학습 데이터 일부 사용)
df = pd.read_csv('./data/iris.csv')
X_test = df.drop('target', axis=1).iloc[:5]

# 모델 불러오기
model = joblib.load('./model/model.joblib')

# 예측
preds = model.predict(X_test)
print('예측 결과:', preds)
