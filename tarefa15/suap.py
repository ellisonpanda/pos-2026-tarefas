from authlib.integrations.requests_client import OAuth2Session
from config import Config

authorization_url = (
    f"{Config.SUAP_URL}/o/authorize/"
)

token_url = (
    f"{Config.SUAP_URL}/o/token/"
)

api_base = (
    f"{Config.SUAP_URL}/api/"
)