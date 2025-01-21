import os
from dotenv import load_dotenv

# Load environment variables from .env file during local execution
if os.getenv("ENV") != "production":
    load_dotenv()

AUTH_URL = os.getenv("AUTH_URL")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUDIENCE = os.getenv("AUDIENCE")
PATTODATEUSERNAME = os.getenv("PATTODATEUSERNAME")
PATTODATEPASSWORD = os.getenv("PATTODATEPASSWORD")
SCOPE = os.getenv("SCOPE")

BE_PROFILE_PATH = "api/v2/userprofile"
BE_SEARCH_PATH = "api/v2/search?pa=@"
BE_WAIT_BETWEEN_REQUESTS_SECS = int(os.getenv("BE_WAIT_BETWEEN_REQUESTS_SECS"))

BE_ENDPOINT = os.getenv("BE_ENDPOINT")