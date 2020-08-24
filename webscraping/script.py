import requests

from bs4 import BeautifulSoup

 

URL = 'https://www.managementstudyguide.com/real-estate-articles.htm'

page = requests.get(URL)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('article')

for job_elem in results:

    print(job_elem, end='\n'*2)

URL = 'https://economictimes.indiatimes.com/wealth/real-estate'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='eachStory')

for job_elem in results:

    print(job_elem, end='\n'*2)

URL = 'https://timesofindia.indiatimes.com/business/real-estate'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span', class_='w_tle')

for job_elem in results:

    print(job_elem, end='\n'*2)

for x in range(1,100):

    URL = 'https://housing.com/news/page/'+str(x)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('article')

    for job_elem in results:

        print(job_elem, end='\n'*2)