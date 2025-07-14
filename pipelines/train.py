{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ca17bb7b-280d-4ca8-aa3d-314d3c7d432b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-14T05:05:14.828093Z",
     "iopub.status.busy": "2025-07-14T05:05:14.827761Z",
     "iopub.status.idle": "2025-07-14T05:05:18.091032Z",
     "shell.execute_reply": "2025-07-14T05:05:18.090497Z",
     "shell.execute_reply.started": "2025-07-14T05:05:14.828070Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31m2025/07/14 05:05:18 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.\u001b[0m\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logged with accuracy: 1.0\n"
     ]
    }
   ],
   "source": [
    "import mlflow\n",
    "import mlflow.sklearn\n",
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# 데이터 불러오기\n",
    "df = pd.read_csv('data.csv')\n",
    "X = df[['feature1', 'feature2', 'feature3']]\n",
    "y = df['label']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "with mlflow.start_run():\n",
    "    clf = RandomForestClassifier(n_estimators=10, random_state=42)\n",
    "    clf.fit(X_train, y_train)\n",
    "    preds = clf.predict(X_test)\n",
    "    acc = accuracy_score(y_test, preds)\n",
    "\n",
    "    mlflow.log_param(\"n_estimators\", 10)\n",
    "    mlflow.log_metric(\"accuracy\", acc)\n",
    "    mlflow.sklearn.log_model(clf, \"model\")\n",
    "    print(f\"Logged with accuracy: {acc}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f79303a1-1299-4b91-85fb-d937a5facf13",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
