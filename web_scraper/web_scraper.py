import requests
from bs4 import BeautifulSoup
import re

url = input('Paste a legit wikipedia url link here: ')
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
citation_needed = soup.find_all(title='Wikipedia:Citation needed')


def get_citations_needed_count():
    print(f'******************This link of page need {len(citation_needed)} citations.*************************')


def get_citations_needed_report():
    print("******************The following places require citations******************")
    for citation in citation_needed:
        content = str(citation.parent.parent.parent)
        pattern = r"<[^<>]+>"
        parsed_content = re.sub(pattern, '', content)
        print(parsed_content)


get_citations_needed_count()
get_citations_needed_report()
