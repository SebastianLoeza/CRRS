
import requests
from PIL import Image
import json

URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'
URL_CARDS= 'https://api.clashroyale.com/v1/cards'

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNmYmIzMjkzLTg3ODAtNDBiZi05ZmVmLTM2ZDY0NjE4MTZiNiIsImlhdCI6MTY4MzgyODYxNCwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNDguMjA0LjU2LjI0MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.xuDPIR9Pnmxc-D8rl2E8eGoH8td14r5vbDtrj9K3hQQLCHciExFUFljPB6H0WBK5GW_DgsguGpbi-NkselH4gA'

}
"""
import requests
from PIL import Image

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

# Example usage
card_name = 'Knight'
image_url = get_card_image_url(card_name)

if image_url:
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open('card_image.jpg', 'wb') as file:
            file.write(response.content)

        image = Image.open('card_image.jpg')
        image.show()
else:
    print("Card not found.")



"""
def get_all_cards():
    response = requests.get(url=URL_CARDS, headers=headers)
    print("Cards status code: " + str(response.status_code))
    
    card_map = {}  # Dictionary to store card names and URLs
    
    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')

        for item in items_list:
            card_name = item['name']
            card_url = item['iconUrls']['medium']
            card_map[card_name] = card_url  # Assign URL to card name in the dictionary


    return card_map

ola=get_all_cards()

print(ola['Knight'])


