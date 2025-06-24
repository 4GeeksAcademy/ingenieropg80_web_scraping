import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import StringIO

#COMO EXPLICO CARLOS TRAAJAR TABLAS CON PANDAS
URL = "https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify"
response= requests.get(URL)
html = response.text
tablas =pd.read_html(StringIO(html))
df = tablas[0]

print(df.head())

df = df.dropnas(subset=["Song", "Artist"]) ?????????????????????????

