"""Configuration loader for the application."""

import getpass
import os
from dotenv import load_dotenv
import boto3


def load_config():
    """Loads configuration from environment variables, secret manager, or prompts the user."""
    load_dotenv()

    if "GROQ_API_KEY" not in os.environ:
        if "GROQ_SECRET_NAME" in os.environ:
            client = boto3.client("secretsmanager")
            response = client.get_secret_value(SecretId=os.environ["GROQ_SECRET_NAME"])
            os.environ["GROQ_API_KEY"] = response["SecretString"]
        else:
            os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
