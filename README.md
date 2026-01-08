

---

# AutoJudge – Automated Difficulty Prediction for Programming Problems

AutoJudge is a machine-learning system that **predicts the difficulty of programming problems using only their textual content**.
It supports two main prediction tasks:

1. **Difficulty Classification** — Easy / Medium / Hard
2. **Difficulty Regression** — A continuous numerical difficulty score

A lightweight **Streamlit web interface** is included for real-time predictions.

---

## 🚀 Project Overview

Competitive programming platforms often assign difficulty labels manually, which can be:

* Subjective
* Slow
* Inconsistent

**AutoJudge automates difficulty prediction using only text**, following the project constraint of using **no external metadata or submission trends**.

---

## 📂 Dataset

The dataset consists of real competitive programming challenges. Each entry includes:

* `title`
* `description`
* `input_description`
* `output_description`
* `problem_class` (Easy / Medium / Hard)
* `problem_score` (numerical difficulty)

The dataset originally in JSONL format was converted into CSV for preprocessing.

---

## 🧹 Data Preprocessing

Preprocessing steps include:

* Filling missing fields
* Concatenating all text sections into a unified string
* Applying log transformation to difficulty scores
* Adding numerical indicators extracted from text

The final processed text combines title, description, input, and output specifications.

---

## 🧠 Feature Engineering

A hybrid feature approach was used:

### **TF-IDF Features**

* Unigrams, bigrams, and trigrams
* Stopword removal
* Sublinear term-frequency scaling
* Vocabulary size limits for performance

### **Handcrafted Features**

Extracted directly from the problem text:

* Character length
* Mathematical symbol count (`=`, `<`, `^`, `/`, etc.)
* Keyword indicators for:

  * `dp`
  * `graph`
  * `tree`
  * `recursion`
  * `greedy`
  * `modulo`

All features adhere to the text-only constraint.

---

## 🤖 Models Used

Two separate models were created:

### **Random Forest Classifier**

Predicts **Easy / Medium / Hard**

### **XGBoost Regressor**

Predicts a **numerical difficulty score**

* Trained using log-scaled difficulty values
* Captures non-linear relationships effectively
* Models stored using `joblib`

---

## 📈 Evaluation

### **Classification**

* **Test Accuracy:** ~57.7%
* **Cross-Validation Accuracy:** ~52.5%
* Medium problems recognized most accurately
* Natural overlap exists between Medium and Hard

### **Regression** (log-scaled target)

* **MAE:** ~0.294
* **RMSE:** ~0.357

Reasonable predictive performance given the subjective nature of difficulty labels.

---

## 🌐 Web Application

A Streamlit interface allows users to test the model live.

Users can input:

* Problem description
* Input format
* Output format

App outputs:

* Predicted difficulty class
* Predicted difficulty score

Runs entirely on local machine.

---

## 🎥 Demo Video

👉 **[https://www.youtube.com/watch?v=vmTYcQcxZWg](https://www.youtube.com/watch?v=sDoskcUG9q4)**

---

## ▶️ How to Run Locally

### **1. Install dependencies**

```bash
pip install -r requirements.txt
```

### **2. Run Streamlit app**

```bash
streamlit run app_final.py
```

### **3. Open in browser**

```
http://127.0.0.1:5000/
```

---

## 👤 Author

**Name:** Parth Mishra
**Enrollment No.:** 23410026

---

