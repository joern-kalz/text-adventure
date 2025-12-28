"""Main entry point for the text adventure game backend."""

from src.adapters.api.app import create_app
from src.adapters.config.config import load_config

load_config()
app = create_app()
