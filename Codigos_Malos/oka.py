import tkinter as tk
import requests
import pandas as pd
from tkinter import *
import requests
from PIL import Image, ImageTk
import os

URL_CARDS = 'https://api.clashroyale.com/v1/cards'
URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImExMTgyZGZjLTQwNmQtNDA2Zi1hMTg0LTI0OTE1ODdjYWU1OSIsImlhdCI6MTY4NTQxMjEyNCwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuMjE2LjE0OS4xIl0sInR5cGUiOiJjbGllbnQifV19.LDsYdt59EmI-dBAC3p3jOT7BF3gFI-S-G_Re_xyCQiZ3eDTc3IM3Ri1XexHLHHBk0Jr-PC7r2fVWNmIS3TBuiw'
}

num_columns = 8

def get_player_battle_log():
    BATTLELOG = URL_BATTLELOG.replace('82UUGL0YC', e.get())
    response = requests.get(url=BATTLELOG, headers=headers)
    print("Player Battle Log Status code: " + str(response.status_code))

    if response.status_code == 200:
        battle_logs = response.json()
        cards_vec = []
        IMAGE_VEC = []

        for log in battle_logs:
            team = log['team']
            for card in team[0]['cards']:
                cards_vec.append(card['name'])

        cartas_vec = pd.Series(cards_vec)

        max_card = cartas_vec.value_counts().idxmax()

        result_window = Toplevel(root)
        result_window.title("Battle Log Results")

        text_widget = Text(result_window, width=100, height=100)
        text_widget.grid(row=0, column=0, padx=10, pady=10)


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
                    
                    IMAGE_VEC.append(cardop['name'] + ".jpg")

                    recommendation += '- ' + cardop['name'] + '\n'
                if recommendation_count == 3:
                    break

                text_widget.insert(END, recommendation)

                num_photos = len(IMAGE_VEC)
                num_rows = (num_photos + num_columns - 1) // num_columns

                for i in range(num_rows):
                    for j in range(num_columns):
                        index = i * num_columns + j

                        # Check if there are remaining photos
                        if index >= num_photos:
                            break

                        # Load the image
                        image = Image.open(IMAGE_VEC[index])
                        # Resize the image if needed
                        image = image.resize((200, 200), Image.LANCZOS)
                        # Convert the image to Tkinter-compatible format
                        photo = ImageTk.PhotoImage(image)

                        # Create a label to display the photo
                        label = tk.Label(result_window, image=photo)
                        label.image = photo  # Store a reference to the photo
                        label.grid(row=i, column=j, padx=10, pady=10)
    else:
        print("No se pudo obtener el registro de batallas del jugador.")

# Create the Tkinter window
root = tk.Tk()
root.title("Clash Royale Recommendation System")
# Create an entry widget for user input
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Create a button to trigger the player battle log retrieval
get_battle_log_button = tk.Button(root, text="Get Battle Log", command=get_player_battle_log)
get_battle_log_button.grid(row=2, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
