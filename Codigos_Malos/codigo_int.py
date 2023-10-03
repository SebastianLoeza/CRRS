from tkinter import *
import requests
import json
import pandas as pd
#


URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'


headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImExMTgyZGZjLTQwNmQtNDA2Zi1hMTg0LTI0OTE1ODdjYWU1OSIsImlhdCI6MTY4NTQxMjEyNCwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuMjE2LjE0OS4xIl0sInR5cGUiOiJjbGllbnQifV19.LDsYdt59EmI-dBAC3p3jOT7BF3gFI-S-G_Re_xyCQiZ3eDTc3IM3Ri1XexHLHHBk0Jr-PC7r2fVWNmIS3TBuiw'
}


root= Tk()
root.title("Clash Royale Recommendation System")


e= Entry(root,width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def get_player():

    PLAYER=URL_PLAYER.replace('82UUGL0YC',e.get())
    response= requests.get(url=PLAYER,headers=headers)
    print("Player Status code: "+str(response.status_code))
    user_json= response.json()
    
    if(response.status_code==200):
       print('Name: '+user_json['name'])
       print('Level: ' + str(user_json['expLevel']))
       print('Trophies: ' + str(user_json['trophies']))
       print('Battle Count: ' + str(user_json['battleCount']))
       print("==============================")


def get_all_tournaments():
    response= requests.get(url= URL_TOURNAMENTS + '?name='+ e.get(), headers= headers)
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

def get_player_battle_log():

    BATTLELOG= URL_BATTLELOG.replace('82UUGL0YC',e.get())
    response = requests.get(url=BATTLELOG, headers=headers)
    print("Player Battle Log Status code: " + str(response.status_code))

    if response.status_code == 200:
        battle_logs = response.json()
        cards_vec = []

        for log in battle_logs:
            team = log['team']
            for card in team[0]['cards']:
                cards_vec.append(card['name'])
                # print('- ' + card['name'])

        cartas_vec = pd.Series(cards_vec)

        max_card = cartas_vec.value_counts().idxmax()
        print("En los últimos 25 juegos la carta más repetida es:", max_card)
        min_card = cartas_vec.value_counts().idxmin()
        print("En los últimos 25 juegos la carta menos repetida es:", min_card)

        recommendation_count = 0  # Contador de recomendaciones

        for log in battle_logs:
            team = log['team']
            crowns = team[0]['crowns']
            opponent = log['opponent']
            crowns_opponent = opponent[0]['crowns']

            player_cards = [card['name'] for card in team[0]['cards']]

            if max_card in player_cards and crowns_opponent > crowns:
                print("Te recomiendo usar el siguiente mazo: ")
                for cardop in opponent[0]['cards']:
                    print('- ' + cardop['name'])
                
                recommendation_count += 1  # Incrementar el contador de recomendaciones

                if recommendation_count == 3:  # Salir del bucle después de 3 recomendaciones
                    break
    else:
        print("No se pudo obtener el registro de batallas del jugador.")


#button_GetTournaments= Button(root,text= "Ready!", padx=40, pady=20, command=get_all_tournaments)

#button_GetBattle_Log=Button(root, text="Ready!", padx=40, pady=20, command=get_player_battle_log)
button_GetPlayer=Button(root,text="Ready!", padx=20,pady=20,command=get_player)

#button_GetPlayer.grid(row=1,column=0,columnspan=3)
#button_GetBattle_Log.grid(row=1,column=0,columnspan=3)
button_GetPlayer.grid(row=1,column=0,columnspan=3)




root.mainloop()



