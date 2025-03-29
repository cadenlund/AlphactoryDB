import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("POLYGON_API_KEY")


