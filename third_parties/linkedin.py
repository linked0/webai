import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles
    Manually scrape the information from the LinkedIn profile"""
    if mock:
        linked_profile_url = "https://gist.githubusercontent.com/linked0/52e9b1f33884808631e820cb7e723c54/raw/f9ca94cfaba8d34241f55fc4a8169c1108565a6d/eden-marco.json"
        response = requests.get(linked_profile_url,
                                timeout=10,
                                )
    else:
        api_key = os.environ.get("PROXYCURL_API_KEY")
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        response = requests.get(api_endpoint,
                                params={'linkedin_profile_url': linkedin_profile_url},
                                headers=headers,
                                timeout=10,)

    data = response.json()
    return data

def main_mock():
    return scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco",
        mock=True,
    )

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco",
            mock=True,
        )
    )
