import sys,time,os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from src.PFP import cpp

cpp.clear()
print('CryPe started at %s \nMade by syke (D4R10) - Python 3.9\n  if you see this, you started the debug app, or a dev\n' % cpp.date)


LOG_NAME = 'log-%s.log' % cpp.datereg
cpp.init.logHandler.createFile(LOG_NAME)

logwrite = cpp.init.logHandler.writeLine

string = str
integer = int

n = '\n'

#
try:
	ARG_1 = sys.argv[1]
except IndexError:
	ARG_1 = None
	pass

if ARG_1 == '.debug':
	debug = True
else: debug = False

#
LOCATION_UI = string('src\\UI\\')
UI_FILENAME = string('ui.gui')
ICON_PATH = string('src\\ICO\\stpyi.ico')
#

if debug == True:
	i='Debug is activated, you can now see hidden text'
	print(i)

class MainApp(QMainWindow, QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi(LOCATION_UI + UI_FILENAME, self)
		self.setWindowIcon(QIcon(ICON_PATH))
		print('Finished Loading!')
		if debug == True:
			print(QIcon(ICON_PATH))


		self.button_Encrypt.clicked.connect(self.encryption_file) # Connect button to a function
		self.button_Decrypt.clicked.connect(self.decryption_file) # Same too

	def encryption_file(self):
		# GET KEY AND FILENAME
		V_FILENAME = string(self.line_filename.text())
		
		if V_FILENAME == None:
			error_msg = '<System> -> No File?'
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> No File typed in the box')
			logwrite(LOG_NAME, log_txt)
			return
		if os.path.exists(V_FILENAME):
			pass
		else:
			print("<System> -> File doesn't exists! (%s)" % V_FILENAME)
            
			log_txt = string(f"<{datetime.today()}> -> File doesn't exists (%s)" % V_FILENAME)
			logwrite(LOG_NAME, log_txt)
			return
        
        
		try:
			V_KEY = integer(self.line_key.text())
		except ValueError:
			error_msg = '<ValueError> -> %s' % self.line_key.text()
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> ValueError (%s)' % self.line_key.text())
			logwrite(LOG_NAME, log_txt)
			return
		
		if V_KEY >= 255:
			error_msg = '<ValueError> -> %s (over 255)' % V_KEY
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is over 255')
			logwrite(LOG_NAME, log_txt)
			return
		elif V_KEY <= 0:
			error_msg = '<ValueError> -> %s (under 1)' % V_KEY
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is under 1')
			logwrite(LOG_NAME, log_txt)
			return
		elif V_KEY == None:
			error_msg = '<System> -> No Key?'
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is None (nothing typed in)')
			logwrite(LOG_NAME, log_txt)
			return
		else:
            # Decrypt the File
			if debug:
				msg_status = string('USED:')
				msg_status1 = string(' Filename: %s' % V_FILENAME)
				msg_status2 = string(' Key: %s' % V_KEY)
				print(msg_status + n + msg_status1 + n + msg_status2)
			
			cpp.init.decrypt(V_FILENAME, V_KEY)
            
			log_txt = string(f'<{datetime.today()}> -> Finished encoding %s' % V_FILENAME)
			logwrite(LOG_NAME, log_txt)
		
		return


	def decryption_file(self):
        # GET KEY AND FILENAME
		V_FILENAME = string(self.line_filename.text())
		
		if V_FILENAME == None:
			error_msg = '<System> -> No File?'
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> No File typed in the box')
			logwrite(LOG_NAME, log_txt)
			return
		if os.path.exists(V_FILENAME):
			pass
		else:
			print("<System> -> File doesn't exists! (%s)" % V_FILENAME)
            
			log_txt = string(f"<{datetime.today()}> -> File doesn't exists (%s)" % V_FILENAME)
			logwrite(LOG_NAME, log_txt)
			return
        
        
		try:
			V_KEY = integer(self.line_key.text())
		except ValueError:
			error_msg = '<ValueError> -> %s' % self.line_key.text()
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> ValueError (%s)' % self.line_key.text())
			logwrite(LOG_NAME, log_txt)
			return
		
		if V_KEY >= 255:
			error_msg = '<ValueError> -> %s (over 255)' % V_KEY
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is over 255')
			logwrite(LOG_NAME, log_txt)
			return
		elif V_KEY <= 0:
			error_msg = '<ValueError> -> %s (under 1)' % V_KEY
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is under 1')
			logwrite(LOG_NAME, log_txt)
			return
		elif V_KEY == None:
			error_msg = '<System> -> No Key?'
			print(error_msg)
            
			log_txt = string(f'<{datetime.today()}> -> Key is None (nothing typed in)')
			logwrite(LOG_NAME, log_txt)
			return
		else:
            # Decrypt the File
			if debug:
				msg_status = string('USED:')
				msg_status1 = string(' Filename: %s' % V_FILENAME)
				msg_status2 = string(' Key: %s' % V_KEY)
				print(msg_status + n + msg_status1 + n + msg_status2)
			
			cpp.init.decrypt(V_FILENAME, V_KEY)
            
			log_txt = string(f'<{datetime.today()}> -> Finished decoding %s' % V_FILENAME)
			logwrite(LOG_NAME, log_txt)
		return




if __name__ == '__main__':
	app = QApplication(sys.argv)

	

	appMain = MainApp()

	if debug:
		print(string(app) + n + str(appMain))

	appMain.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		log_txt = string(f'<{datetime.today()}> -> Closed program with win.TOPRIGHT_X')
		logwrite(LOG_NAME, log_txt)
		print('\nExit program...')
