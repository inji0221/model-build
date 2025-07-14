# train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 데이터 경로
data_path = './data/iris.csv'
model_dir = './model'
os.makedirs(model_dir, exist_ok=True)

# 데이터 로드
df = pd.read_csv(data_path)
X = df.drop('target', axis=1)
y = df['target']

# 모델 학습
model = RandomForestClassifier()
model.fit(X, y)

# 모델 저장
joblib.dump(model, f'{model_dir}/model.joblib')
print('모델 저장 완료:', f'{model_dir}/model.joblib')
