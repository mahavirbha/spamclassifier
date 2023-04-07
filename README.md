## A Spam Classifier for SMS/Emails
### Databases : SMS Spam Collection Dataset (https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
### Technologies/Frameworks: Python, Pandas, Numpy, Sklearn, streamlit (Frontend Framework), matplotlib, nltk, seaborn, 

#### run _spamClassifier.ipynb_ and get pkl files and add to your project workplace

#### install required packages & run _streamlit run main.py_

## Steps for this project:
1. Data Cleaning
    - renaming
    - missing values
    - remove duplicates
2. EDA (to understand underlying data)
    - plotting charts (ham vs spam)
    - wordcount
3. Text Pre-Processing (with the help of nltk library)
   - Lower case
   - Tokenization
   - Removing special characters
   - Removing stop words and punctuation
   - Stemming
4. Model Building (with the help of sklearn library)
   - train-test data
   - tfidf vectorization
   - model training on various ML classifiers
5. Evaluation
   - compare and choose on best model
6. Improvement
   - re-train model by hyper parameter tuning (here TfidfVectorizer(max_features=3000))
7. Website
   - create & open a project in editor
   - crete & code app.py file
   - import .pkl files & functions from ipynb file
   - integrate it in streamlit

Local URL: http://localhost:8501

Network URL: http://192.168.1.113:8501

Example Outputs:

![Screenshot (234).png](..%2F..%2F..%2F..%2FPictures%2FScreenshots%2FScreenshot%20%28234%29.png)

![Screenshot (235).png](..%2F..%2F..%2F..%2FPictures%2FScreenshots%2FScreenshot%20%28235%29.png)

![Screenshot (236).png](..%2F..%2F..%2F..%2FPictures%2FScreenshots%2FScreenshot%20%28236%29.png)