import streamlit as st

# Title of the web app
st.title("My Streamlit Web App")

# Add some text to the app
st.header("Welcome to my web app!")
st.subheader("Here's a simple example:")

# Add an input widget to the app
name = st.text_input("Enter your name", "John Doe")

# Add a button widget to the app
button_clicked = st.button("Submit")

# Check if the button is clicked
if button_clicked:
    # Display a message with the entered name
    st.success(f"Hello, {name}!")

# Add a plot to the app
st.subheader("Data Visualization")
data = [1, 2, 3, 4, 5]
st.line_chart(data)

# Add a sidebar to the app
st.sidebar.header("Sidebar")
sidebar_selection = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected option from the sidebar
st.sidebar.text(f"Selected: {sidebar_selection}")
