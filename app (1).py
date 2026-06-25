import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Spam Email Detector")

message = st.text_area("Enter Message")

if st.button("Predict"):
    data = vectorizer.transform([message])
    result = model.predict(data)[0]

    if result == "spam":
        st.error("🚨 SPAM")
    else:
        st.success("✅ NOT SPAM")