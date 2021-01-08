## Generátor IVR pro Cisco Meeting Server
Generátor využívá Google TTS API. Pokud ho chcete použít, doporučuji projít si tutorial:
https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3
V tutorialu si jednak pod svým účtem zapnete TTS API a pak si vytvoříte credentials,
které jsou potřeba pro spuštění tohoto generátoru. Credentials se vytváří v kroku 4 tutorialu.
Uložte si je do lokálního souboru (třeba `credentials.json`).

## Příprava - Python virtulání prostředí, credentials
1. vytvořte virtuální prostředí `python3 -m venv venv`
2. přepněte do něj `source venv/bin/activate`
3. nainstalujte potřebné balíčky `pip install -r requirements.txt`
4. v Google TTS tutorialu uložte `key.json` na váš počítač do lokálního souboru `credentials.json`
5. připravte Google API credentials `export GOOGLE_APPLICATION_CREDENTIALS=credentials.json`

## Generování IVR hlášek
Seznam hlášek je v kapitole 3 [Customization Guide](https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Customisation/Version-3-0/Cisco-Meeting-Server-3-0-Customization-Guidelines.pdf). Spolu s názvy IVR souborů je najdete v [prompts.csv](prompts.csv), k otestování slouží [prompts-test.csv](prompts-test.csv). Soubor byl editován v Excelu, proto jsou použity jako oddělovače středníky a ne čárky. Pokud použijete jiné oddělovače, upravte podle toho `    csv.register_dialect('semicolon', delimiter=';')` v tts_generate.py. První řádek CSV souboru je hlavička:
* **file_name** označuje sloupec s názvy souborů
* **en-US** je sloupec s hláškami v angličtině
* přeložené texty dejte do sloupce s příslušným kódem jazyka. Pokud kód neznáte nebo nevíte, zda ho Google umí, spusťte `python tts_generate.py -f prompts-test.csv`. V prvním kroku se vám vypíšou dostupné kódy. Pak program přerušte ^C a vyplňte sloupec v prompts.csv.

Jestliže už máte prompts.csv připravené, generování promptů spustíte `python tts_generate.py -f prompts.csv` jako volitelné parametry lze uvést:
* **-l / --language** - kód jazyka (např. `cs-CZ`)
* **-v / --voice** - název hlasového generátoru (např. `cs-CZ-Wavenet-A`)
* **-d / --directory** - název adresáře, do kterého se mají vygenerované hlášky nahrát
