import sys,time
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

from src import osy

ui_path = 'src\\ui\\debug_ui.xml'

#LOG_DEF_LINE = f'{datetime.today()}'  # Not working, its the same time xD im stupid

logname = f'log-{osy.datereg}'
osy.init.logHandler.createFile(logname)

#t = [f'<{datetime.today()}>  -  UI File {ui_path} successful loaded', f'<{datetime.today()}>  -  Pressed Encrypt button', f'<{datetime.today()}>  -  Pressed Decrypt button', f'<{datetime.today()}>  -  vkey: ValueError']
# upper not working lol stupid again


class MainApp(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi(ui_path, self)

		
		osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  UI File {ui_path} successful loaded')

		self.button_Encrypt.clicked.connect(self.EncryptFile)
		self.button_Decrypt.clicked.connect(self.DecryptFile)



	def exitProgram(self):
		exit()

	def EncryptFile(self):
		vkey = self.line_key.text()
		vfilename = self.line_filename.text()
		osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  Pressed Encrypt button')

		try:
			vkey = int(vkey)
		except ValueError:
			print('\nError: ValueError')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vkey: Key is not an Integer (Number) [{vkey}]')
			return

		print(f'\nvkey: {vkey}\nvfilename: {vfilename}\n')

		try:
			osy.init.encrypt(vfilename, vkey)
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  Done with encrypted file ({vfilename}, {vkey})')
			self.label_status.setText('DONE')
			time.sleep(0.5)
			self.label_status.setText('')

		except FileNotFoundError:
			print('FILE NOT FOUND')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vfilename: file not found ({vfilename})')
		except ValueError:
			print('OVER 255 LIMIT')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vkey: over 255 limit')

	def DecryptFile(self):
		vkey = self.line_key.text()
		vfilename = self.line_filename.text()
		osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  Pressed Decrypt button')

		try:
			vkey = int(vkey)
		except ValueError:
			print('\nError: ValueError')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vkey: Key is not an Integer (Number) [{vkey}]')
			return

		print(f'\nvkey: {vkey}\nvfilename: {vfilename}\n')

		try:
			osy.init.decrypt(vfilename, vkey)
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  Done with decrypted file ({vfilename}, {vkey})')
			self.label_status.setText('DONE')
			time.sleep(0.5)
			self.label_status.setText('')

		except FileNotFoundError:
			print('FILE NOT FOUND')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vfilename: file not found ({vfilename})')
		except ValueError:
			print('OVER 255 LIMIT')
			osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  vkey: over 255 limit')

if __name__ == '__main__':
	app = QApplication(sys.argv)

	appMain = MainApp()
	appMain.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		osy.init.logHandler.writeLine(logname, f'<{datetime.today()}>  -  Closed Window with topright_x')
		print('Closing Window...')