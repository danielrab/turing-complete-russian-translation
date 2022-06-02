git pull
python .\upload_file.py
Invoke-WebRequest https://turingcomplete.game/download_translation/8 -OutFile Russian.txt
Copy-Item Russian.txt "C:\Program Files (x86)\Steam\steamapps\common\Turing Complete\translations\Russian.txt"
git add .
git commit -m "Automatic Sync"
git push
taskkill /im "Turing Complete.exe"
Start-Process "C:\Users\s17b1\Desktop\Turing Complete.url"