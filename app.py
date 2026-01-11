import streamlit as st
st.title("Simple Streamlit App")
st.write("This is my first Streamlit application.")

name = st.text_input("Type your name here")

if st.button("Say Hello"):
    if name == "":
        st.write("Please enter your name first.")
    else:
        st.write("Hello", name, "😊")
