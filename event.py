from typing import Collection
from bs4 import BeautifulSoup as bs 
import requests

# from firebase import Firebase 
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 

#Section to get all event data from external site 
url = "https://www.portland.gov/events"

# print(response) | gave success response 200 
response = requests.get(url)
# print(html) | printed all html 
html = response.content 
# print(soup ) | little better to look at it 
soup = bs(html, "lxml")  

#Section for firestore credentials 
cred = credentials.Certificate("civic-engage-capstone-firebase-adminsdk-hkf3r-17f4b9b0b2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to get all 
def save(collection_id, event_tag, event_title, event_start_date, event_end_date, event_des):
    db.collection(collection_id).add({"tag": event_tag, "title": event_title, "event_start": event_start_date, "event_end": event_end_date, "desc": event_des})

event_list = soup.find_all("div", class_="views-field views-field-search-api-rendered-item")

for event in event_list: #loop through each event
    # gets event tags 
    event_tag = soup.find('div', class_="badge badge-pill text-wrap text-left badge-light").get_text(strip=True) 
    # print(event_tag.get_text(strip=True))

    # gets event titles 
    event_title = event.find("span", class_="field field--name-title field--type-string field--label-hidden").get_text(strip=True) 
    # print(event_title.get_text(strip=True))

    # gets event start date
    event_start_date = soup.find("div", class_="field field--name-field-start-date field--type-datetime field--label-hidden").get_text(strip=True) 
    # print(event_start_date.get_text(strip=True))

    # prints event end data 
    event_end_date = soup.find("div", class_="field field--name-field-end-date field--type-datetime field--label-hidden").get_text(strip=True) 
    # print(event_end_date.get_text(strip=True))

    # prints event description 
    event_des = soup.find("div", class_="morsel__text").get_text(strip=True)
    # print(event_des.get_text(strip=True))

    save(
        collection_id = "meetings",
        event_tag = event_tag,
        event_title = event_title,
        event_start_date = event_start_date,
        event_end_date = event_end_date,
        event_des = event_des
    )




















# # Getting data from external site using BeautifulSoup 
# html_text = requests.get('https://www.portland.gov/events').text
# soup = BeautifulSoup(html_text, 'html.parser')    
# #To use lxml, need to install pip install lxml 

# # events_title = soup.find_all('h2', class_="h3 order-1 mb-2").text
# # events_title.text
# # for event_title in events.find_all('h2', class_="h3 order-1 mb-2"):
# #     print(event_title.text)

# meeting_tag = soup.find('div', class_="badge badge-pill text-wrap text-left badge-light").text
# meeting_title = soup.find('h2', class_="h3 order-1 mb-2").text
# meeting_description = soup.find('div', class_="row no-gutters").text
# # event_date = soup.find('span', class_="d-flex allign-items-center")

# # event = soup.find('span', class_ = ("field field--name--title field--type--string field--label-hidden") 
# print(meeting_tag)
# print(meeting_title)
# print(meeting_description)


# # def find_event_div(tag):
# #     if tag.name != "div":
# #         return False 
# #     if not tag.has_attr("class"):
# #         return False 
# #     if "views-field" not in tag["class"]:
# #         return False 
# #     # if tag:
# #     h2 = tag.find("h2")
# #     if h2 is None:
# #         return False 
# #     return True
# # # events = soup.find_all('div', class_="views-field")
# # events = soup.find_all(find_event_div)

# # for event in events:
# #     print(event.text)
# #     print("------------------")

# # create function to especific tags 


# # Sending data to firestore 
# cred = credentials.Certificate("civic-engage-capstone-firebase-adminsdk-hkf3r-17f4b9b0b2.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# def save(collection_id, meeting_tag, meeting_title, meeting_description):
#     # help(db.collection(collection_id).document(event_tag))
#     # db.collection(collection_id).document(event_tag).set({"title": event_title, "body": event_body})
#     # db.collection(collection_id).document(document_id).set({"tag": meeting_tag, "title": meeting_title, "desc": meeting_description})
#     db.collection(collection_id).add({"tag": meeting_tag, "title": meeting_title, "desc": meeting_description})

#     # db.collection(collection_id).document(event_tag).data(event_title).data(event_body)

# save(
#     collection_id = "meetings",
#     # document_id= document_id,
#     meeting_tag = meeting_tag,
#     meeting_title = meeting_title,
#     meeting_description = meeting_description
# )



# # prints event tags 
# event_tag = soup.find_all('div', class_="badge badge-pill text-wrap text-left badge-light")
# def print_tag(event_tag):
#     for tag in event_tag:
#         print(tag.get_text(strip=True))
# print(print_tag)

# # prints event titles 
# event_title = soup.find_all('h2', class_="h3 order-1 mb-2")
# def print_title(event_title):
#     for title in event_title:
#         print(title.get_text(strip=True))

# # # prints event start dates 
# # event_start_date = soup.find_all("div", class_="field field--name-field-start-date field--type-datetime field--label-hidden")
# # for start_date in event_start_date:
# #     print(start_date.get_text(strip=True))

# # # prints event end dates
# # event_end_date = soup.find_all("div", class_="field field--name-field-end-date field--type-datetime field--label-hidden")
# # for end_date in event_end_date:
# #     print(end_date.get_text(strip=True))

# # prints all date and time.............
# event_date_time = soup.find_all("span", class_="d-flex align-items-center")
# def print_date_time(event_date_time):
#     for time in event_date_time:
#         print(time.get_text(strip=True))


# # Not sure how to print all time because all time have different tags 

# # prints event description 
# event_des = soup.find_all("div", class_="morsel__text")
# # "field field--name-field-summary field--type-string field--label-hidden")
# def print_des(event_des):
#     for des in event_des:
#         print(des.get_text(strip=True))


# Section to send data to Firestore 
# cred = credentials.Certificate("civic-engage-capstone-firebase-adminsdk-hkf3r-17f4b9b0b2.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# def save(collection_id, print_tag, print_title, print_date_time, print_des):
# #     # help(db.collection(collection_id).document(event_tag))
# #     # db.collection(collection_id).document(event_tag).set({"title": event_title, "body": event_body})
# #     # db.collection(collection_id).document(document_id).set({"tag": meeting_tag, "title": meeting_title, "desc": meeting_description})
#     db.collection(collection_id).add({"tag": print_tag, "title": print_title, "date_time": print_date_time, "desc": print_des})

# #     # db.collection(collection_id).document(event_tag).data(event_title).data(event_body)

# save(
#     collection_id = "Events",
#     # document_id= document_id,
#     print_tag = print_tag,
#     print_title = print_title,
#     print_date_time = print_date_time,
#     print_des = print_des
# )

    # # prints all date and time.............
    # event_date_time = soup.find_all("span", class_="d-flex align-items-center")
    # def print_date_time(event_date_time):
    #     for time in event_date_time:
    #         print(time.get_text(strip=True))

    # prints time of the event 
    # if all day:
        # print all day
    # else:
        # print(start time) and end time

# Section to send data to Firestore 
# cred = credentials.Certificate("civic-engage-capstone-firebase-adminsdk-hkf3r-17f4b9b0b2.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# def save(collection_id, event_tag, event_title, event_start_date, event_end_date, event_des):
#     # help(db.collection(collection_id).document(event_tag))
#     # db.collection(collection_id).document(event_tag).set({"title": event_title, "body": event_body})
#     # db.collection(collection_id).document(document_id).set({"tag": meeting_tag, "title": meeting_title, "desc": meeting_description})
#     db.collection(collection_id).add({"tag": event_tag, "title": event_title, "event_start": event_start_date, "desc": event_des})

# save(
#     collection_id = "meetings",
#     # document_id= document_id,
#     meeting_tag = meeting_tag,
#     meeting_title = meeting_title,
#     meeting_description = meeting_description
# )