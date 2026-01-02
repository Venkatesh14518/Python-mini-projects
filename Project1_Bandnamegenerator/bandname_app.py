import streamlit as st
# Imports the Streamlit library so we can build a web app using Python

st.title("🎸 Band Name Generator")
# Displays a large title at the top of the web page

city = st.text_input("Which city did you grow up in?")
# Creates a text input box asking for the city name
# Whatever the user types is stored in the variable 'city' as a string

pet = st.text_input("What is the name of your pet?")
# Creates another text input box asking for the pet's name
# The user's input is stored in the variable 'pet' as a string

if city and pet:
    # Checks whether both 'city' and 'pet' contain some text
    # This ensures the output is shown only after both inputs are given

    st.success(f"Your band name could be: {city} {pet}")
    # Displays the generated band name in a highlighted success message
    # An f-string is used to combine city and pet with proper spacing
