{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0c5b928c-4129-4a1e-aad1-c593ddeeb400",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-14T05:27:14.681679Z",
     "iopub.status.busy": "2025-07-14T05:27:14.681386Z",
     "iopub.status.idle": "2025-07-14T05:27:15.061430Z",
     "shell.execute_reply": "2025-07-14T05:27:15.060793Z",
     "shell.execute_reply.started": "2025-07-14T05:27:14.681658Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = [\n",
    "    [5.1, 3.5, 1.4, 0],\n",
    "    [4.9, 3.0, 1.4, 0],\n",
    "    [6.2, 3.4, 5.4, 1],\n",
    "    [5.9, 3.0, 5.1, 1],\n",
    "    [5.0, 3.6, 1.4, 0],\n",
    "    [6.7, 3.1, 4.7, 1],\n",
    "    [5.6, 2.5, 3.9, 1],\n",
    "    [5.4, 3.9, 1.7, 0],\n",
    "    [6.9, 3.1, 5.1, 1],\n",
    "    [5.5, 2.3, 4.0, 1]\n",
    "]\n",
    "\n",
    "columns = ['feature1', 'feature2', 'feature3', 'label']\n",
    "\n",
    "df = pd.DataFrame(data, columns=columns)\n",
    "df.to_csv('data.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aae46a5-516a-4ff4-b813-ad1ae1a9c9b8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abf55fac-1cc6-48ee-b0d1-c26d707f91aa",
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
