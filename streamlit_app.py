import streamlit
import snowflake.connector
# from urllib.error 
# import URLerror


streamlit.title('My Parents New Healthy Diner')
streamlit.header('My Parents New Healthy Diner')          
streamlit.text('🥣 Omega 3 3 & Blueberry Otmeal')
streamlit.text('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')   
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')   

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 
# import pandas
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
   streamlit.error("Please select a fruit to get information.")
  else:
   fruityvice_response = requests.get("https://fruitvice.com/api/fruit/"+ fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   streamlit.dataframe(fruityvice_normalized)
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
# streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

# write your own comment -what does the next line do? 
# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
# don't run anthing past here while we troubleshoot
streamlit.stop()



# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
streamlit.write('Thanks for adding ', fruit_choice)

# streamlit.write('Thanks for adding ', add_my_fruit)
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")




