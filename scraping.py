import requests
from bs4 import BeautifulSoup

base_url = 'https://dlpsgame.com/category/ps4/page/'

jumlah_halaman = 5

for halaman in range(1, jumlah_halaman + 1):

    url = base_url + str(halaman) + '/'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
    else:
        print(f'Gagal mengambil halaman {url}. Kode status:', response.status_code)
        continue

    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all(class_='post-title entry-title')

    for title in titles:
        print('Halaman', halaman, '- Judul:', title.text.strip())
