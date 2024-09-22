from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API URL and API key from the environment variables
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
