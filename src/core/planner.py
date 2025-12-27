"""
Travel Planner Module

This module defines the TravelPlanner class, which manages user inputs
(city and interests), generates a travel itinerary using an LLM-based chain,
and maintains conversational message history.
"""

from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException


# Initialize module-level logger
logger = get_logger(__name__)


class TravelPlanner:
    """
    TravelPlanner manages the end-to-end flow of itinerary generation.

    Responsibilities:
    - Store city and interests provided by the user
    - Maintain conversation history (Human & AI messages)
    - Generate a travel itinerary using an LLM chain
    - Log operations and handle errors gracefully
    """

    def __init__(self):
        """
        Initialize the TravelPlanner instance.

        Attributes:
            messages (list): Conversation history (HumanMessage & AIMessage)
            city (str): Selected city for travel
            interests (list): List of user interests
            itineary (str): Generated itinerary text
        """
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self, city: str):
        """
        Set the city for itinerary generation.

        The city is stored internally and added to the message history
        as a HumanMessage.

        Args:
            city (str): Name of the city.

        Raises:
            CustomException: If setting the city fails.
        """
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)

    def set_interests(self, interests_str: str):
        """
        Set user interests for itinerary generation.

        The interests string is split by commas, stripped of whitespace,
        and stored as a list. The raw input is also added to message history.

        Args:
            interests_str (str): Comma-separated list of interests.

        Raises:
            CustomException: If setting interests fails.
        """
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfully")
        except Exception as e:
            logger.error(f"Error while setting interests: {e}")
            raise CustomException("Failed to set interest", e)

    def create_itineary(self):
        """
        Generate a travel itinerary based on city and interests.

        The generated itinerary is:
        - Stored internally
        - Added to the message history as an AIMessage
        - Returned to the caller

        Returns:
            str: Generated itinerary text.

        Raises:
            CustomException: If itinerary generation fails.
        """
        try:
            logger.info(
                f"Generating itinerary for city: {self.city}, "
                f"interests: {self.interests}"
            )

            itineary = generate_itinerary(self.city, self.interests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))

            logger.info("Itinerary generated successfully")
            return itineary

        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)
