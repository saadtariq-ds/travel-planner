"""
Streamlit UI for AI Travel Itinerary Planner

This module provides a simple Streamlit-based user interface
that allows users to generate a travel itinerary by entering
a city and their interests.
"""

import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(page_title="AI Travel Planner")

# Application title and description
st.title("AI Travel Itinerary Planner")
st.write(
    "Plan your day trip itinerary by entering your city and interests."
)

# Create a form to collect user inputs
with st.form("planner_form"):
    # Input for city name
    city = st.text_input("Enter the city name for your trip")

    # Input for user interests (comma-separated)
    interests = st.text_input(
        "Enter your interests (comma-separated)"
    )

    # Submit button for the form
    submitted = st.form_submit_button("Generate itinerary")

    # Handle form submission
    if submitted:
        if city and interests:
            # Initialize the travel planner
            planner = TravelPlanner()

            # Set city and interests
            planner.set_city(city)
            planner.set_interests(interests)

            # Generate itinerary
            itineary = planner.create_itineary()

            # Display the generated itinerary
            st.subheader("📄 Your Itinerary")
            st.markdown(itineary)
        else:
            # Warn user if required inputs are missing
            st.warning(
                "Please fill in both City and Interests to continue."
            )