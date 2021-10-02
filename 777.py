import os



def run(dizin):
	if os.listdir(dizin) == []:
		pass
	else:
		
		#os.system("chmod 777 " + dizin )
		os.system("chmod 777 " + dizin + "/*")
		for i in os.listdir(dizin):
			if os.path.isdir(dizin + "/" + i):
				run(dizin + "/" +i)

		
run("/var/www/html")