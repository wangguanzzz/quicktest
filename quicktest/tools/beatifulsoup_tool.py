from crewai_tools import BaseTool
import requests
from bs4 import BeautifulSoup

class BSTool(BaseTool):
    name: str = "BSTool"
    description: str = (
        "Input the web page URL, this tool will return the context of the page"
    )
    
    
    def _run(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
