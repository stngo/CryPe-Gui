
debugMode = False

from datetime import datetime
import os

date = datetime.today()
datereg = datetime.today().strftime ('%m-%d-%Y %H_%M_%S')

def clear():
    # check and make call for specific operating system
    _ = os.system('clear' if os.name =='posix' else 'cls')

class init:
	def encrypt(filename, key):
		fileOpen = open(filename, "rb")
		data = fileOpen.read()
		fileOpen.close()

		data = bytearray(data)
		for index, value in enumerate(data):
			if debugMode:
				print(f"\nget.index = {index}\n get.value = {value}\n")
			data[index] = value ^ key

		fileOpen = open(filename + '_e', "wb")
		fileOpen.write(data)
		fileOpen.close()

	def decrypt(filename, key):
		fileOpen = open(filename, "rb")
		data = fileOpen.read()
		fileOpen.close()

		data = bytearray(data)
		for index, value in enumerate(data):
			if debugMode:
				print(f"\nget.index = {index}\n get.value = {value}\n")
			data[index] = value ^ key

		fileOpen = open(filename + '_d', "wb")
		fileOpen.write(data)
		fileOpen.close()

	class logHandler:
		def createFile(logname):

			logFolder = 'logs/'

			if os.path.exists(logFolder):
				pass
			else:
				os.mkdir(logFolder)
				print('log folder created successfully')


			with open(logFolder+logname, "w") as logFile:
				logFile.write('Log File created %s' % date)
				pass

		def writeLine(logname, text):
			with open('logs/'+logname, 'r') as logFile:
				d = logFile.read()
			with open('logs/'+logname, 'w') as logFile:
				logFile.write(d +'\n\n'+ text)