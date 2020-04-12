# from django.forms import ModelForm, TextInput
from django import forms
from Register.models import Registration

import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "1293145f1amsh1fd6f0f82c5a680p1b6215jsn3dc6b068b7ed"
    }

data = requests.request("GET", url, headers=headers).json()

statelist = data['state_wise'].keys()
STATE_CHOICES = [(i,i) for i in statelist]

citylist = {}
for i in range(len(statelist)):
    try:
        citylist[list(statelist)[i]] = list(data['state_wise'].values())[i]['district'].keys()
    except KeyError:
        i += 1
cities = []
for i in range(len(citylist)):
    for j in list(citylist.values())[i]:
        cities.append((j))

cities.sort()
CITY_CHOICES = [(x,x) for x in cities if not '*' in x and not x=='Unknown']
STATE_CHOICES.sort()

class registrationform(forms.Form):
    stateselect = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'id':'inputState', 'class':'form-control'}))
    cityselect = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'id':'inputState', 'class':'form-control'}))
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}) )
