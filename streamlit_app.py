import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('My Parents New Healthy Diner')          
streamlit.text('🥣 Omega 3 3 & Blueberry Otmeal')
streamlit.text('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')   
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')   

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

