import requests
import os

from dotenv import load_dotenv, find_dotenv, set_key
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

REFRESH_TOKEN = "https://graph.instagram.com/refresh_access_token"

def refresh_access_token():
    resp = requests.get(REFRESH_TOKEN, params={"grant_type":"ig_refresh_token", 
                                               "access_token": os.environ["INSTA_ACCESS_TOKEN"]}).json()
    print(resp)
    set_key(dotenv_file, "INSTA_ACCESS_TOKEN", resp["access_token"])

def boot_unfollowers():
    pass

if __name__ == "__main__":
    pass
