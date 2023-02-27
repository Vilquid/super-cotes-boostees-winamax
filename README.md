# super-cotes-boostees-winamax

## Utilité

Prévenir un utilisateur via une notification Telegram/myNotifier que de nouveaux paris sur les Grosses Cotes Boostées sont disponibles (Winamax).

## Configuration matérielle sur laquelle le projet tourne

Nom du système d’exploitation:              Microsoft Windows 10 Professionnel

Version du système:                         10.0.15063 N/A version 15063

Fabricant du système d’exploitation:        Microsoft Corporation

Configuration du système d’exploitation:    Station de travail autonome

Type de version du système d’exploitation:  Multiprocessor Free

## Installation

### Python

Installer Python (https://www.python.org/downloads/) et ne pas oublier d'activer les varibles d'environnement.

### Batch

Double-cliquer sur ``shortcut.bat``. Le script se lancera à chaque redémarrage du pc.
Modifier les variables ``LOCALISATION_geckodriver.exe``, ``LOCALISATION_python.exe`` et ``LOCALISATION_main.py`` dans ``setup.bat`` pour que les chemins correspondent aux chemins de la machine.

```batch
tasklist | find /i "geckodriver.exe" && (
	echo geckodriver is already running
) || (
	echo Launching geckodriver ...
	start /min "" "LOCALISATION_geckodriver.exe"
	echo geckodriver launched
)
echo.

echo Launching main code ...
"C:\Python\python.exe" "C:\Users\Leboncoin\Desktop\Winamax\main.py"
echo.
```

``LOCALISATION_geckodriver.exe`` : localisation de geckodriver.exe (ex : C:\Users\Leboncoin\Desktop\Winamax\geckodriver.exe)

``LOCALISATION_python.exe`` : localisation de python.exe (ex : C:\Python\python.exe)

``LOCALISATION_main.py`` : localisation de main.py (ex : C:\Users\Leboncoin\Desktop\Winamax\main.py)

### Notifications

Modifier les variables ``API_KEY_myNotifier``, ``TELEGRAM_BOT_TOKEN`` et ``TELEGRAM_CHAT_ID`` dans ``main.py`` pour recevoir les notification sur vos différents appareils.

```python
requests.post('https://api.mynotifier.app', {
	"apiKey": '65d7vv8f-4755-1ba1-a64e-70ddc3cd9f75',
	"message": "Winamax",
	"description": message,
	"body": "",
	"type": "warning",  # info, error, warning or success
	"project": ""
})
          
bot_token = "5882504504:AAF-mKs2AsjUtVNZYR0TV89sQbsxjLdKVPE"
chat_id = -563009334
```

``API_KEY_myNotifier`` : clé d'API de myNotifier (ex : 65d7vv8f-4755-1ba1-a64e-70ddc3cd9f75)

``TELEGRAM_BOT_TOKEN`` : token du bot Telegram (ex : 5882504504:AAF-mKs2AsjUtVNZYR0TV89sQbsxjLdKVPE)

``TELEGRAM_CHAT_ID`` : id du chat Telegram (ex : -563009334)

``TELEGRAM_BOT_TOKEN`` s'obtient via le BotFather et ``TELEGRAM_CHAT_ID`` s'obtient en recherchant ``https://api.telegram.org/botXXXXXX/getUpdates`` (XXXXXX étant l'id du bot).

#### Exemple pour trouver ``TELEGRAM_CHAT_ID``

Ici ce qui nous intéresse est ``-563009334``.

```json
[...]
"my_chat_member":{"chat":{"id":-563009334,"title":"Winamax","type":"group","all_members_are_administrators":true},"from":
[...]
```
