import requests
from bs4 import BeautifulSoup
import regex as re
import json
URL = "https://google.qwiklabs.com/public_profiles/7e0abd7b-15e0-4e51-8db2-1d552322ad3c"


CHALLENGES_AVAILABLE = [
    'Integrate with Machine Learning APIs',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Explore Machine Learning Models with Explainable AI',
    'Engineer Data in Google Cloud',
    'Insights from Data with BigQuery',
    'Deploy to Kubernetes in Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Deploy and Manage Cloud Environments with Google Cloud',
    'Set up and Configure a Cloud Environment in Google Cloud',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Getting Started: Create and Manage Cloud Resources',
    'Google Cloud Essentials'
]


COMPLETED_QUESTS = []
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
quests = soup.findAll('div', attrs={'class': 'public-profile__badges'})
for row in quests[0].findAll('ql-badge'):
    var=str(row)
    str_dict = var[var.find('{'): var.find('}') + 1]
    dict_ = json.loads(str_dict)

    if dict_['title'] in CHALLENGES_AVAILABLE:
        COMPLETED_QUESTS.append(dict_['title'])
profile = soup.findAll('div', attrs={'class': 'public-profile__hero'})[0]
dp = profile.img['src']
name = profile.h1.text
# return {
#     "quests": COMPLETED_QUESTS,
#     "dp": dp,
#     "name": name.strip()
# }
