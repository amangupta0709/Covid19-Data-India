import requests
import os
import smtplib
from email.message import EmailMessage


def emailsent(name,email,state,city):

    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "1293145f1amsh1fd6f0f82c5a680p1b6215jsn3dc6b068b7ed"
    }

    data = requests.request("GET", url, headers=headers).json()
    statein = data['state_wise'][str(state)]

    confirmed = statein['confirmed']
    active = statein['active']
    deaths = statein['deaths']
    newconfirmed = statein['deltaconfirmed']
    newdeaths = statein['deltadeaths']
    lastupdatedtime = statein['lastupdatedtime']

    cityconfirmed = statein['district'][str(city)]['confirmed']
    citynewconfirmed = statein['district'][str(city)]['delta']['confirmed']

    # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    EMAIL_ADDRESS = 'covid19indiadata@gmail.com'
    EMAIL_PASSWORD = 'aman0709'

    name = str(name)
    name.upper()

    msg = EmailMessage()
    msg['Subject'] = 'Covid-19 Cases in your Area'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = str(email)
    msg.set_content(f'''
    Covid-19 Cases in {state}:
        Active Cases : {active}
        Total Confirmed Cases : {confirmed}  (New Cases: {newconfirmed} )
        Total Deaths : {deaths}  (New Cases: {newdeaths} )
    Covid-19 Cases in {city}:
        Total Confirmed Cases : {cityconfirmed}  (New Cases: {citynewconfirmed} )

    STAY AT HOME, STAY SAFE {name}
    ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

