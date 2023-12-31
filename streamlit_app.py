import streamlit
import pandas

 

streamlit.title("My parents new healthy dinner")

 

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

 

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

 

 

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

 

import snowflake.connector

 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

 

# Add a form to allow the user to add a new fruit
streamlit.header("What fruit would you like to add?")
add_my_fruit = streamlit.text_input("Enter the new fruit:")
if streamlit.button("Add"):
    if add_my_fruit:
        my_cur.execute("INSERT INTO fruit_load_list (fruit_name) VALUES (%s)", (add_my_fruit,))
        my_cnx.commit()
        streamlit.success(f"Thanks for adding {add_my_fruit}")
    else:
        streamlit.warning("Please enter a fruit name.")

 

my_cur.execute("INSERT INTO fruit_load_list values ('from streamlit)")
