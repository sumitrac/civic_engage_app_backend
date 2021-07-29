from typing import Collection
from bs4 import BeautifulSoup
import requests
# from firebase import Firebase 
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 

html_text = requests.get('https://www.portland.gov/events')
soup = BeautifulSoup(html_text, 'html.parser')    #To use lxml, need to instatl pip install lxml 

# events_title = soup.find_all('h2', class_="h3 order-1 mb-2").text
# events_title.text
# for event_title in events.find_all('h2', class_="h3 order-1 mb-2"):
#     print(event_title.text)

event_tag = soup.find('div', class_="badge badge-pill text-wrap text-left badge-light").text
event_title = soup.find('h2', class_="h3 order-1 mb-2").text
event_body = soup.find('div', class_="row no-gutters").text
# event_date = soup.find('span', class_="d-flex allign-items-center")

# event = soup.find('span', class_ = ("field field--name--title field--type--string field--label-hidden") 

print(event_tag)
print(event_title)
print(event_body)


# import firebase_admin
# from firebase_admin import credentials 
# from firebase_admin import firestore 

cred = credentials.Certificate("civic-engage-capstone-firebase-adminsdk-hkf3r-b65348f762.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save(collection_id, event_tag, event_title, event_body):
    db.collection(collection_id).document(event_tag).document(event_title).data(event_body)

save(
    collection_id = "event_1",
    event_tag = "event_tag",
    event_title = "event_title",
    event_body = "event_body"
)