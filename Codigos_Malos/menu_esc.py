import tkinter as tk
from tkinter import *
import requests
import json
import pandas as pd
#

URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'
URL_CARDS= 'https://api.clashroyale.com/v1/cards'

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNmYmIzMjkzLTg3ODAtNDBiZi05ZmVmLTM2ZDY0NjE4MTZiNiIsImlhdCI6MTY4MzgyODYxNCwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNDguMjA0LjU2LjI0MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.xuDPIR9Pnmxc-D8rl2E8eGoH8td14r5vbDtrj9K3hQQLCHciExFUFljPB6H0WBK5GW_DgsguGpbi-NkselH4gA'

}


root = Tk()
root.title("Clash Royale Recommendation System")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def get_all_tournaments():
    response = requests.get(url=URL_TOURNAMENTS + '?name=' + e.get(), headers=headers)
    print("Tournament status code: " + str(response.status_code))

    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')

        result_window = Toplevel(root)
        result_window.title("Results")

        text_widget = Text(result_window, width=100, height=100)
        text_widget.pack()

        for item in items_list:
            result = (
                'Name: ' + item['name'] +
                '\nStatus: ' + item['status'] +
                '\nTag: ' + item['tag'] +
                '\nMax Capacity: ' + str(item['maxCapacity']) +
                '\nCapacity: ' + str(item['capacity']) +
                '\n======================\n'
            )
            text_widget.insert(END, result)
def get_player():

    PLAYER = URL_PLAYER.replace('82UUGL0YC', e.get())

    response = requests.get(url=PLAYER, headers=headers)
    result_window = tk.Toplevel(root)  # Create a new window for the result
    result_window.title("Results")
    
    if response.status_code == 200:
        user_json = response.json()
        result_text = tk.Text(result_window)
        result_text.pack()

        result_text.insert(tk.END, 'Name: ' + user_json['name'] + "\n")
        result_text.insert(tk.END, 'Level: ' + str(user_json['expLevel']) + "\n")
        result_text.insert(tk.END, 'Trophies: ' + str(user_json['trophies']) + "\n")
        result_text.insert(tk.END, 'Battle Count: ' + str(user_json['battleCount']) + "\n")
        result_text.insert(tk.END, "==============================\n")
    else:
        result_text = tk.Text(result_window)
        result_text.pack()
        result_text.insert(tk.END, "Player not found or an error occurred.\n")

def get_player_battle_log():
    BATTLELOG = URL_BATTLELOG.replace('82UUGL0YC', e.get())
    response = requests.get(url=BATTLELOG, headers=headers)
    print("Player Battle Log Status code: " + str(response.status_code))

    if response.status_code == 200:
        battle_logs = response.json()
        cards_vec = []

        for log in battle_logs:
            team = log['team']
            for card in team[0]['cards']:
                cards_vec.append(card['name'])

        cartas_vec = pd.Series(cards_vec)

        max_card = cartas_vec.value_counts().idxmax()
        min_card = cartas_vec.value_counts().idxmin()

        result_window = Toplevel(root)
        result_window.title("Battle Log Results")

        text_widget = Text(result_window, width=100, height=100)
        text_widget.pack()
        
        
        
        result = (
            "En los últimos 25 juegos la carta más repetida es: " + max_card +
            "\nEn los últimos 25 juegos la carta menos repetida es: " + min_card +
            "\n\nRecomendaciones de mazo:"
        )
        text_widget.insert(END, result)

        recommendation_count = 0

        for log in battle_logs:
            team = log['team']
            crowns = team[0]['crowns']
            opponent = log['opponent']
            crowns_opponent = opponent[0]['crowns']

            player_cards = [card['name'] for card in team[0]['cards']]

            if max_card in player_cards and crowns_opponent > crowns:
                recommendation = "\n\nTe recomiendo usar el siguiente mazo:\n"
                for cardop in opponent[0]['cards']:
                    recommendation += '- ' + cardop['name'] + '\n'
                
                text_widget.insert(END, recommendation)
                recommendation_count += 1

                if recommendation_count == 3:
                    break

    else:
        print("No se pudo obtener el registro de batallas del jugador.")


def get_card_image_url(card_name):
    # Make a request to the Clash Royale API to get all cards
    response = requests.get(url=URL_CARDS, headers=headers)

    if response.status_code == 200:
        cards_data = response.json()

        for card in cards_data['items']:
            if card['name'] == card_name:
                return card['iconUrls']['medium']

    # Return an empty string if the card name is not found or an error occurred
    return ''


button_GetPBattleLog = Button(root, text="Get Battle Log", padx=40, pady=20, command=get_player_battle_log)
button_GetPBattleLog.grid(row=1, column=0, columnspan=3)


button_GetPlayer = Button(root, text="Tournaments!", padx=40, pady=20, command=get_all_tournaments)
button_GetPlayer.grid(row=2, column=0, columnspan=3)

button_GetPlayerResume=Button(root,text='Player context',padx=40,pady=20,command=get_player)
button_GetPlayerResume.grid(row=3,column=0,columnspan=3)
root.mainloop()
