import datetime
import time
import requests
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def send_telegram_message(message):
	"""Envoi d'un message par le bot Telegram"""
	bot_token = "5889004504:AAF-mKs2KENoSgEyYR0TV89sQbsxjLdKVPE"
	chat_id = -1001514266177
	telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
	data = {"chat_id": chat_id, "text": message}
	requests.post(telegram_url, data=data)


def data(driver):
	"""Récupération des données du tableau général"""
	while True:
		try:
			# Recherche des cotes sur le site
			driver.get("https://wepari.fr/indexf.html")

			# Récupération des données du tableau général
			elem = driver.find_element(By.TAG_NAME, "tbody")

			# Première partie du nettoyage des données
			table_data = elem.text

			lines = table_data.split('\n')

			# Suppression des 10 premières lignes
			lines = lines[10:]

			# Suppression de toutes les lignes après la 15ᵉ ligne
			lines = lines[:5]

			print("Scan de " + str(datetime.datetime.now().strftime("%d/%m %H:%M")))
			for i in range(len(lines)):
				print(lines[i])
			print("")

			# Vérification sur le changement de la structure du site
			if "Cotes entre 1,70 et 1,85" not in lines[0] or "Cotes entre 3,50 et 3,75" not in lines[-1]:
				send_telegram_message("Le site a changé de structure, le script ne fonctionne certainement plus.")

			return lines

		# Gestion des erreurs
		except WebDriverException as e:
			send_telegram_message("Erreur lors du chargement de la page")

			# Envoi et affichage d'une notification d'erreur
			send_telegram_message(e)
			print(e)

			# Attente de 30 secondes avant de réessayer de charger la page
			time.sleep(30)


def send_cotes(cotes_avant, cotes_apres):
	"""Parsing des données et envoi d'une notification si les cotes ont changé"""
	# Vérification des cotes avant et après pour chaque ligne du tableau
	for i in range(len(cotes_avant)):
		# Envoi d'une notification si les cotes ont changé
		if cotes_avant[i] != cotes_apres[i]:
			for j in range(len(cotes_apres)):
				if len(cotes_apres[j].split(' ')) == 14:
					print(len(cotes_apres[j].split(' ')))
					borne_inf = float(cotes_apres[j].split(' ')[2].replace(',', '.'))
					borne_sup = float(cotes_apres[j].split(' ')[4].replace(',', '.'))
					cote_moyenne = float(cotes_apres[j].split(' ')[5].replace(',', '.'))
					nb_paris = float(cotes_apres[j].split(' ')[6].replace(',', '.'))
					gain_net = float(cotes_apres[j].split(' ')[7].replace(',', '.'))
					prc_paris_gagnant = int(cotes_apres[j].split(' ')[9].replace('%', ''))
					gain_net_mise = float(cotes_apres[j].split(' ')[11].replace('€/€', '').replace(',', '.'))

					print("Message envoyé :")
					print(f'Borne inférieure : {borne_inf}' + " " + f'Borne supérieure : {borne_sup}' + " " + f'Cote moyenne : {cote_moyenne}' + " " + f'Nombre de paris : {nb_paris}' + " " + f'Gain net : {gain_net}' + " " + f'Pourcentage de paris gagnants : {prc_paris_gagnant}' + " " + f'Gain net / mise : {gain_net_mise}')
					message = "Bornes : " + str(borne_inf) + "-" + str(borne_sup) + " Cote moyenne : " + str(cote_moyenne) + " Nombre de paris : " + str(nb_paris) + " Gain net : " + str(gain_net) + "€ Pourcentage de paris gagnants : " + str(prc_paris_gagnant) + " Gain net/mise : " + str(gain_net_mise)

					# Envoi de la notification sur mon téléphone
					requests.post('https://api.mynotifier.app', {
						"apiKey": '65d7aa5f-4755-4ba1-a64e-70ddc3cd9f75',
						"message": "Winamax",
						"description": message,
						"body": "",
						"type": "warning",  # info, error, warning or success
						"project": ""
					})

					# Envoi de la notification sur le groupe Telegram
					send_telegram_message(message)

				if len(cotes_apres[j].split(' ')) == 15:
					print(len(cotes_apres[j].split(' ')))
					borne_inf = float(cotes_apres[j].split(' ')[2].replace(',', '.'))
					borne_sup = float(cotes_apres[j].split(' ')[4].replace(',', '.'))
					cote_moyenne = float(cotes_apres[j].split(' ')[5].replace(',', '.'))
					nb_paris = float(cotes_apres[j].split(' ')[6].replace(',', '.'))
					part1 = cotes_apres[j].split(' ')[7].replace(',', '.')
					part2 = cotes_apres[j].split(' ')[8].replace(',', '.')
					gain_net = part1 + part2
					prc_paris_gagnant = int(cotes_apres[j].split(' ')[10].replace('%', ''))
					gain_net_mise = float(cotes_apres[j].split(' ')[12].replace('€/€', '').replace(',', '.'))
					
					print("Message envoyé :")
					print(f'Borne inférieure : {borne_inf}' + " " + f'Borne supérieure : {borne_sup}' + " " + f'Cote moyenne : {cote_moyenne}' + " " + f'Nombre de paris : {nb_paris}' + " " + f'Gain net : {gain_net}' + " " + f'Pourcentage de paris gagnants : {prc_paris_gagnant}' + " " + f'Gain net / mise : {gain_net_mise}')
					message = "Bornes : " + str(borne_inf) + "-" + str(borne_sup) + " Cote moyenne : " + str(cote_moyenne) + " Nombre de paris : " + str(nb_paris) + " Gain net : " + str(gain_net) + "€ Pourcentage de paris gagnants : " + str(prc_paris_gagnant) + " Gain net/mise : " + str(gain_net_mise)

					# Envoi de la notification sur mon téléphone
					requests.post('https://api.mynotifier.app', {
						"apiKey": '65d7aa5f-4755-4ba1-a64e-70ddc3cd9f75',
						"message": "Winamax",
						"description": message,
						"body": "",
						"type": "warning",  # info, error, warning or success
						"project": ""
					})

					# Envoi de la notification sur le groupe Telegram
					send_telegram_message(message)

				if len(cotes_apres[j].split(' ')) == 16:
					print(len(cotes_apres[j].split(' ')))
					borne_inf = float(cotes_apres[j].split(' ')[2].replace(',', '.'))
					borne_sup = float(cotes_apres[j].split(' ')[4].replace(',', '.'))
					cote_moyenne = float(cotes_apres[j].split(' ')[5].replace(',', '.'))
					part1 = cotes_apres[j].split(' ')[6].replace(',', '.')
					part2 = cotes_apres[j].split(' ')[7].replace(',', '.')
					nb_paris = part1 + part2
					part1 = cotes_apres[j].split(' ')[8].replace(',', '.')
					part2 = cotes_apres[j].split(' ')[9].replace(',', '.')
					gain_net = part1 + part2
					prc_paris_gagnant = int(cotes_apres[j].split(' ')[10].replace('%', ''))
					gain_net_mise = float(cotes_apres[j].split(' ')[12].replace('€/€', '').replace(',', '.'))

					print("Message envoyé :")
					print(f'Borne inférieure : {borne_inf}' + " " + f'Borne supérieure : {borne_sup}' + " " + f'Cote moyenne : {cote_moyenne}' + " " + f'Nombre de paris : {nb_paris}' + " " + f'Gain net : {gain_net}' + " " + f'Pourcentage de paris gagnants : {prc_paris_gagnant}' + " " + f'Gain net / mise : {gain_net_mise}')
					message = "Bornes : " + str(borne_inf) + "-" + str(borne_sup) + " Cote moyenne : " + str(cote_moyenne) + " Nombre de paris : " + str(nb_paris) + " Gain net : " + str(gain_net) + "€ Pourcentage de paris gagnants : " + str(prc_paris_gagnant) + " Gain net/mise : " + str(gain_net_mise)

					# Envoi de la notification sur mon téléphone
					requests.post('https://api.mynotifier.app', {
						"apiKey": '65d7aa5f-4755-4ba1-a64e-70ddc3cd9f75',
						"message": "Winamax",
						"description": message,
						"body": "",
						"type": "warning",  # info, error, warning or success
						"project": ""
					})

					# Envoi de la notification sur le groupe Telegram
					send_telegram_message(message)


def main():
	send_telegram_message("Début du programme principal - " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
	print("Début du programme principal - " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
	# Options de Firefox
	options = Options()
	options.add_argument("--private-window")
	options.add_argument("--headless")

	# Ouverture de Firefox
	driver = webdriver.Firefox(options=options)

	# Récupération des cotes
	cotes_avant = data(driver)

	# Fermeture de Firefox pour économiser de l'énergie
	driver.close()

	while True:
		# Attendre 3 minutes
		time.sleep(180)

		#  Ouverture de Firefox
		driver = webdriver.Firefox(options=options)

		# Récupération des cotes
		cotes_apres = data(driver)

		# Fermeture de Firefox
		driver.close()

		# Comparaison les données
		if cotes_avant != cotes_apres:
			send_cotes(cotes_avant, cotes_apres)

		cotes_avant = cotes_apres

	send_telegram_message("Alerte - Fin du programme - Quelque chose s'est mal passé")


if __name__ == '__main__':
	main()
