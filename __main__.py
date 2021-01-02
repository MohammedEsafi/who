import os
import nmap
import subprocess


def printer(who):
	print('+{}+{}+{}+{}+'.format('-' * 7, '-' * 27, '-' * 22, '-' * 19))
	print('| {:5} | {:25} | {:20} | {:17} |'.format('No.', 'Devices', 'MAC Address', 'IP Address'))
	print('+{}+{}+{}+{}+'.format('-' * 7, '-' * 27, '-' * 22, '-' * 19))
	for index, device in enumerate(who):
		print('| {:5} | {:25} | {:20} | {:17} |'.format(str(index), device['Device'], device['MAC Address'], device['IP Address']))
		print('+{}+{}+{}+{}+'.format('-' * 7, '-' * 27, '-' * 22, '-' * 19))


def what_is_my_ip():
	""" get the IP address of the host. """
	IP = subprocess.Popen("hostname -I", shell=True, stdout=subprocess.PIPE)
	IP = IP.stdout.readline()
	IP = IP.decode("utf-8").split()[0]

	return IP


def who():
	nm = nmap.PortScanner()
	IP = what_is_my_ip()
	host = IP + '/24'
	dictList = nm.scan(hosts=host, arguments='-sn')
	scan = dictList.get("scan")

	WhoList = []
	for IP in scan:
		vendor = scan[IP].get('vendor')
		for MAC in vendor:
			WhoList.append({"IP Address": IP, "MAC Address": MAC, "Device": vendor[MAC]})

	return WhoList


if __name__ == "__main__":
	if os.getuid() == 1000:
		print("Please run this command as sudo! ‒ for better result")

	# find Who's connected to your Wi-Fi network
	who = who()

	# print `who` table on pretty formal
	printer(who)