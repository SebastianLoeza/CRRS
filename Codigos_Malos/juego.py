user_name=input("Ingresa el coódigo del jugador")



URL_CARDS = 'https://api.clashroyale.com/v1/cards'
URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'
nuevo_string= URL_BATTLELOG.replace('82UUGL0YC',user_name)
print(nuevo_string)