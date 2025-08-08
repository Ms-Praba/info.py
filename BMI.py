import streamlit as st
st.title("BMI calculator")
weight=st.text_input("enter your weight")
height=st.text_input("enter your height")

if st.button("calculate"):
	BMI=int(weight) / (float(height)**2)
	if BMI < 16.0:
		st.success("you are severely weight")
	elif BMI >= 16.0 and  BMI <= 16.9:
		st.success("you are very underweight")
	elif BMI >= 17.0 and BMI <= 18.4:
		st.success("underweight")
	elif BMI >= 18.5 and BMI <= 24.9:
	    st.success("normal healthy weight")
	elif BMI >= 25.0 and BMI <= 29.9:
	    st.success("overweight")
	elif BMI >= 30.0 and BMI <= 34.9:
	    st.success("obese class i")
	elif BMI >= 35.0 and BMI <= 39.9:
	    st.success("obese class ii")
	else:
	    st.success("obese class iii")    	

