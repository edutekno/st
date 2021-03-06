import streamlit as st
import pandas as pd
# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
#name = st.text_input("Enter Your name", "Type Here ...")
st.header('BMI Calculator')
weight = st.number_input('Weight', min_value=1, max_value=200, value=75, step=1)
height = st.number_input('Height', value=100)
x = weight/(height*height)
if x < 18.5:
    result ='Underweight'
if x>=18.5 and x<25:
    result ="Normal"
if x >= 25 and x < 30:
   result ='Overweight'
if x >= 30:
   result ='Obesity'


# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	#result = name.title()
	st.success(result)

	
#st.title("Welcome to Streamlit!")

#st.write("Our first DataFrame")

#st.write(
#  pd.DataFrame({
#      'A': [1, 2, 3, 4],
#      'B': [5, 6, 7, 8]
#    })
#)
