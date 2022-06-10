import re
import os
from pathlib import Path
import shutil

def deconstruct(file_name):
  with open(f'{file_name}.txt', 'rb') as file:
    data = file.read()
  shutil.rmtree(file_name)
  for section, text in re.findall(b'===(.+)===((?:.|\n)+?)(?====)', data):
    path = Path(f'{file_name}/{section.strip().decode()}.txt')
    os.makedirs(path.parent, exist_ok=True)
    with open(path, 'wb') as file:
      file.write(text)

deconstruct('Russian')
deconstruct('Russian_missing')