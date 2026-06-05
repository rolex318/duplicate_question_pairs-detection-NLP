# Duplicate Question Detection Using NLP

## 📌 Project Overview

This project aims to identify whether two questions have the same meaning (duplicate questions) using Natural Language Processing (NLP) and Machine Learning techniques. The model is trained on the Quora Question Pairs dataset and deployed using Streamlit.

---

## 🚀 Features

* Text preprocessing and cleaning
* Duplicate question detection
* NLP-based feature extraction using Bag of Words
* Machine Learning model training and evaluation
* Real-time prediction through Streamlit Web Application
* Model serialization using Pickle

---

## 📂 Dataset

The project uses the **Quora Question Pairs Dataset**, which contains pairs of questions and a target label:

* **1** → Duplicate Questions
* **0** → Non-Duplicate Questions

Dataset Columns:

| Column       | Description     |
| ------------ | --------------- |
| qid1         | Question ID 1   |
| qid2         | Question ID 2   |
| question1    | First Question  |
| question2    | Second Question |
| is_duplicate | Target Variable |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-Learn
* XGBoost
* Streamlit
* Pickle

---

## 🔄 Project Workflow

### 1. Data Preprocessing

The text data is cleaned using:

* Lowercase conversion
* Removal of punctuation
* Stopword removal
* Tokenization
* HTML tag removal

### 2. Feature Engineering

Bag of Words (BoW) is used to convert textual data into numerical vectors.

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000)
```

### 3. Model Training

The following machine learning algorithms were trained:

* Random Forest Classifier
* XGBoost Classifier

### 4. Model Evaluation

Models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### Results

| Model         | Accuracy         |
| ------------- | ---------------- |
| Random Forest | Best Performance |
| XGBoost       | Good Performance |

Random Forest achieved the highest accuracy and was selected as the final model.

---

## 💾 Model Saving

```python
import pickle

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(cv, open('cv.pkl', 'wb'))
```

---

## 🌐 Streamlit Deployment

Run the Streamlit application:

```bash
streamlit run app.py
```

The application allows users to:

1. Enter Question 1
2. Enter Question 2
3. Click Predict
4. View Duplicate/Non-Duplicate prediction

---

## 📁 Project Structure

```text
Duplicate-Question-Detection/

│
├── app.py
├── model.pkl
├── cv.pkl
├── train.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── quora_questions.csv
│
└── notebooks/
    └── EDA.ipynb
```

---

## 📊 Sample Prediction

Input:

Question 1:
How can I learn Python quickly?

Question 2:
What is the fastest way to learn Python?

Output:

Duplicate Questions ✅

---

## 🔮 Future Improvements

* TF-IDF Vectorization
* Word2Vec Embeddings
* GloVe Embeddings
* BERT-based Semantic Similarity
* Sentence Transformers
* Deep Learning Models (LSTM, GRU)
* Advanced Feature Engineering

---

## 🎯 Learning Outcomes

Through this project, the following concepts were learned:

* Natural Language Processing (NLP)
* Text Preprocessing
* Feature Extraction
* Machine Learning Classification
* Model Deployment using Streamlit
* Pickle Serialization

---

## 👨‍💻 Author

Chinmaya Giri

B.Tech Student | Data Science | AI/ML | NLP Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star!
