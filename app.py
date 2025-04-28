import streamlit as st
from flight_intents import detect_intent
from flight_entities import extract_entities

# Set the title of the app
st.title("Flight Booking Assistant")

# Add custom CSS for background and styling
st.markdown(
    """
    <style>
        body {
            background-image: url('https://your_image_url_here.jpg'); /* Replace with your image URL or local path */
            background-size: cover;
            background-position: center;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .streamlit-expanderHeader {
            color: #0074D9;
        }
        .stButton button {
            background-color: #0074D9;
            color: white;
            border: none;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .stTextInput input {
            background-color: rgba(255, 255, 255, 0.8);
            color: black;
            border-radius: 5px;
            border: 1px solid #0074D9;
        }
        .stTextInput input:focus {
            border-color: #0056b3;
        }
        .stWrite {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 5px;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state if not already done
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Function to clear the input and results
def clear_input():
    st.session_state.user_input = ""  # Clear the input field

# Input text box for user input
user_input = st.text_input("Please enter your flight booking request:", value=st.session_state.user_input)

# Process the input when the user submits a request
if user_input:
    # Detect intent
    intent = detect_intent(user_input)

    # Extract entities
    entities = extract_entities(user_input)

    # Display the results
    st.write(f"**Detected Intent**: {intent}")
    st.write(f"**Detected Entities**: {entities}")

# Add a Clear button
if st.button("Clear"):
    clear_input()
    st.experimental_rerun()  # Rerun the app to clear everything
