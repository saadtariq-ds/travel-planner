"""
Itinerary Generation Module

This module uses LangChain with Groq's LLM to generate
custom travel itineraries based on a city and user interests.
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.prompts import ITINERARY_SYSTEM_PROMPT, ITINERARY_USER_PROMPT
from src.config.config import GROQ_API_KEY

# Initialize the Groq-powered Large Language Model
llm = ChatGroq(
    api_key=GROQ_API_KEY, model="openai/gpt-oss-20b", 
    temperature=0.7
)

# Create a structured chat prompt template
itinerary_prompt = ChatPromptTemplate([
    ("system", ITINERARY_SYSTEM_PROMPT),
    ("user", ITINERARY_USER_PROMPT)
])


def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Generate a travel itinerary for a given city based on user interests.

    This function formats the prompt with the provided inputs,
    sends it to the LLM, and returns the generated itinerary text.

    Args:
        city (str): Name of the city for which the itinerary is generated.
        interests (list[str]): List of user interests (e.g., food, history, nature).

    Returns:
        str: AI-generated itinerary content.
    """
    # Invoke the LLM with formatted prompt messages
    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=city,
            interests=", ".join(interests)
        )
    )

    # Return the generated itinerary text
    return response.content