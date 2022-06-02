import requests
import os
import re

with open('path_to_progress_ftile.txt') as file:
  save_path = file.read().strip()
with open(os.path.join(save_path, 'progress.dat'), 'rb') as file:
  progress_data = file.read()
token = re.search(b'account_token([0-9A-F]{40})', progress_data).group(1).decode('ascii')
r = requests.post('https://turingcomplete.game/translate', data={"language_id": 8}, files={"translation": open('Russian.txt', 'rb')}, cookies={"token":token})
print(r)