import sys
import socket
from datetime import datetime
import time

def scan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex((target,port))
	if result == 0:
		print(f"Port {port} is open             {datetime.now()}")
	s.close()

while True:
	target = input("Enter an IP adress: ")

	print("-" * 60)
	print(f"Scanning target: {target}")
	print(f"Time started: {datetime.now()}")
	print("-" * 60)

	try:
		scan(20)
		scan(21)
		scan(22)
		scan(23)
		scan(25)
		scan(53)
		scan(67)
		scan(80)
		scan(110)
		scan(119)
		scan(123)
		scan(143)
		scan(443)
		scan(465)
		scan(563)
		scan(989)
		scan(990)
		scan(993)
		scan(995)
		scan(3389)
		print("-" * 60)
	except KeyboardInterrupt:
		print("\nExiting program.")
		print("-" * 60)
		sys.exit()
	except socket.gaierror:
		print("Hostname could not be resolved.")
		sys.exit()
	except socket.error:
		print("Could not connect to the server.")
		print("-" * 60)