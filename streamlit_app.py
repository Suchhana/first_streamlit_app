import streamlit

streamlit.title('my parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,spinach & rocket smoothie')
streamlit.text('🐔Hard boiled free-range egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build your own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
