{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cf817c9-476a-46ce-a362-41740fe157e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "\n",
    "data = {\n",
    "    \"inputs\": [[5.1, 3.5, 1.4]]\n",
    "}\n",
    "response = requests.post(\"http://<EC2-IP>:1234/invocations\", json=data)\n",
    "print(response.json())\n"
   ]
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
