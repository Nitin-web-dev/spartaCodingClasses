# # Try scraping the #1~50 songs of Billboard https://www.billboard.com/charts/hot-100

import requests
from bs4 import BeautifulSoup

url = 'https://www.billboard.com/charts/hot-100'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the container with the list of songs
    songs_container = soup.find('div', class_='chart-results-list')
   

    songs = songs_container.find_all('div', class_='o-chart-results-list-row-container')
    
    
    for i in range(50):
        song = songs[i]
        
        song_name = song.find('h3', class_='c-title').text.strip()
        artist_name = song.find('span', class_='c-label').text.strip()
        print(f"Song {i+1}: {song_name} - Artist: {artist_name} ")
else:
    print("Failed to retrieve webpage.")
        
        
        

