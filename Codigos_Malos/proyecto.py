import requests
import json

if __name__== '__main__':
    url='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOzqYXT_lil4JDvRjza2ieA6robrktPuSkIre22pJ1e_hK-JgrDxa4f5yKAftoYGM5xAVRm0THbJ8vnrvusss_DsPSRDdndrW7GEw5aulG7bFUwhz6SafL7ZNxkFWhbrvm72Y8SU9ljFzqddryIGjUoIoa9zbRJ9x-9IzAZ6MnmiE3iR020dROiYc7/s1280/tumblr_6e1773dc46631842ccd2abbcd5c410d5_3ba25e77_1280.jpg'
    url3='https://c.files.bbci.co.uk/48DD/production/_107435681_perro1.jpg'
    url2= 'https://i0.wp.com/ningunlugarestalejos.com/wp-content/uploads/2022/08/Aang-Avatar.jpeg.webp?fit=1200%2C897&ssl=1'
    response= requests.get(url3,stream=True)#Realiza la peticion sin descargar el contenido
    with open('image2.jpg','wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()