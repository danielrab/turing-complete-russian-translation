git pull
python .\upload_file.py
Invoke-WebRequest https://turingcomplete.game/download_translation/8 -OutFile Russian.txt
Invoke-WebRequest https://turingcomplete.game/download_translation_missing/8 -OutFile Russian_missing.txt
Copy-Item Russian.txt "C:\Program Files (x86)\Steam\steamapps\common\Turing Complete\translations\Russian.txt"
git add .
git commit -m "Automatic Sync"
git push
taskkill /im "Turing Complete.exe"
Start-Process "steam://rungameid/1444480"