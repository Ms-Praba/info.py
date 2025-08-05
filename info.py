import streamlit as st
st.title("school application forms")
name=st.text_input("what is your name")
age=st.text_input("what is your age")
region=st.text("what region are you in")
if st.button("submit"):
	if name == "Araba" and age == "15":
		st.success("welcome to wesley girls high")
	else:
		st.success("who are you?")
