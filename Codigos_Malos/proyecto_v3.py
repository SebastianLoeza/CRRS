#IMPORTANTE ESTE CÓDIGO SOLO ES PARA USAR EN TU CASA
import requests
import json
import pandas as pd
from collections import Counter
#tournament_name= input()

URL_CARDS= 'https://api.clashroyale.com/v1/cards'
URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_PLAYER='https://api.clashroyale.com/v1/players/%2382UUGL0YC'
URL_BATTLELOG= 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'

headers={ 'Content-type':'aplication/json', 'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImExMTgyZGZjLTQwNmQtNDA2Zi1hMTg0LTI0OTE1ODdjYWU1OSIsImlhdCI6MTY4NTQxMjEyNCwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuMjE2LjE0OS4xIl0sInR5cGUiOiJjbGllbnQifV19.LDsYdt59EmI-dBAC3p3jOT7BF3gFI-S-G_Re_xyCQiZ3eDTc3IM3Ri1XexHLHHBk0Jr-PC7r2fVWNmIS3TBuiw'}




def get_all_cards():
    response= requests.get(url=URL_CARDS,headers=headers)
    print("Cards status code: "+ str(response.status_code))
    if(response.status_code==200):
        items_obj = json.loads(response.text)      
        items_list = items_obj.get('items')

        for item in items_list:
            print('Id: '+ str(item['id']))
            print('Name: ' + item['name'])
            print('Max Level: '+ str(item['maxLevel']))
            print('Image: '+ item['iconUrls']['medium'])
            print('======================')
            
def get_all_tournaments(tournament_name):
    response= requests.get(url= URL_TOURNAMENTS + '?name='+ tournament_name, headers= headers)
    print("Tournament status code: "+ str(response.status_code))

    if(response.status_code==200):
       items_obj= json.loads(response.text)
       items_list= items_obj.get('items')

    for item in items_list:
        print('Name: '+ item['name'])
        print('Status: '+ item['status'])
        print('Tag: '+ item['tag'])
        print('Max Capacity:' + str(item['maxCapacity']))
        print('Capacity:' + str(item['capacity'])) 
        print('======================')

def get_player():
    response= requests.get(url=URL_PLAYER,headers=headers)
    print("Player Status code: "+str(response.status_code))
    user_json= response.json()
    
    if(response.status_code==200):
       print('Name: '+user_json['name'])
       print('Level: ' + str(user_json['expLevel']))
       print('Trophies: ' + str(user_json['trophies']))
       print('Battle Count: ' + str(user_json['battleCount']))
       print("==============================")


def get_player_battle_log():
    response = requests.get(url=URL_BATTLELOG, headers=headers)
    print("Player Battle Log Status code: " + str(response.status_code))

    if response.status_code == 200:
        battle_logs = response.json()
        cards_vec=[]

        for log in battle_logs:
            team = log['team']
            for card in team[0]['cards']:
                cards_vec.append(card['name'])
        cartas_vec=pd.Series(cards_vec)
                #print('- ' + card['name'])
        
        print(cartas_vec.value_counts())

        max= cartas_vec.value_counts().idxmax()
        print("En los ultimos 25 juegos la carta más repetida es: ",max)
        min=cartas_vec.value_counts().idxmin()
        print("En los ultimos 25 juegos la carta menos repetida es: ", min)












#get_all_cards()
#get_all_tournaments(tournament_name)
#get_player()
get_player_battle_log()
