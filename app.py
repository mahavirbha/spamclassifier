import streamlit as st
import pickle
import string
import sklearn
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()
sw = stopwords.words('english')


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    l = []
    for i in text:
        if i.isalnum():
            l.append(i)

    text = l[:]
    l.clear()

    for i in text:
        if i not in sw and i not in string.punctuation:
            l.append(i)

    text = l[:]
    l.clear()

    for i in text:
        l.append(ps.stem(i))

    return " ".join(l)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area("Enter the message")

if st.button(":white[Predict]"):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)

    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. predict
    result = model.predict(vector_input)[0]

    # 4. display
    if result == 1:
        st.header(":red[Spam]")
    else:
        st.header(":green[Not Spam]")

