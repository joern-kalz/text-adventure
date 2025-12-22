"""Configuration loader for the application."""

import getpass
import os
from dotenv import load_dotenv


def load_config():
    """Loads configuration from environment variables or prompts the user."""
    load_dotenv()
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
