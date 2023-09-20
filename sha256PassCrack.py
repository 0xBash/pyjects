# sha256PassCrack.py
from pwn import *
import sys

if len(sys.argv) != 2:
	print("Invalid argument!")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	# print(len(sys.argv))
	exit()

wanted_hash = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with log.progress("Attempting to hack: {}!\n".format(wanted_hash)) as p:
	with open (password_file, 'r', encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			passowrd_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), passowrd_hash))
			if passowrd_hash == wanted_hash:
				p.success("Password hash found after {} attempts! ** {} ** hashes to {} !".format(attempts, password.decode('latin-1'), passowrd_hash))
				exit()
			attempts += 1
		p.failure("Passowrd hash not found!")	

