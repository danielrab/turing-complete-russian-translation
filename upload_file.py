import requests
import os
import sqlite3

with open('path_to_progress_ftile.txt') as file:
  save_path = file.read().strip()
database = sqlite3.connect(os.path.join(save_path, 'progress.dat'))
cursor = database.execute("SELECT value FROM progress WHERE key='account_token'")
token ,= cursor.fetchone()
cursor.close()
database.close()
requests.post('https://turingcomplete.game/translate', data={"language_id": 8}, files={"translation": open('Russian.txt', 'rb')}, cookies={"token":token})
requests.post('https://turingcomplete.game/translate', data={"language_id": 8}, files={"translation": open('Russian_missing.txt', 'rb')}, cookies={"token":token})