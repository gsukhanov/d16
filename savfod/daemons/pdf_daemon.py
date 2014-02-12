import os
import shutil
import subprocess
import sys
import time
import file_changes_watcher

WATCH_DIRECTORIES = ['/home/sav/Dropbox/d16-calculus', '/home/sav/Dropbox/d16-programming']
STOPWORDS = ['related']
WAIT_TIME = 10 

def make_pdf(file_path):
	directory, file_name = os.path.split(file_path)
	log_name = file_name[:-4] + '.log'
	pdf_name = file_name[:-4] + '.pdf'
	log_path = file_path[:-4] + '.log'
	pdf_path = file_path[:-4] + '.pdf'

	try:
		os.remove(pdf_name)
	except FileNotFoundError:
		pass

	subprocess.call('iconv -f utf-8 -t cp1251 ' + '"' + file_path + '" > "' + file_name + '"', shell=True)
	p = subprocess.Popen(['pdflatex', '-shell-escape', '-halt-on-error', '"' + file_name + '"'])
	p.wait(WAIT_TIME)

	if os.path.exists(pdf_name):
		print("success")
		try:
			os.remove(log_path)
		except FileNotFoundError:
			pass
		shutil.move(pdf_name, pdf_path)
	else:
		print("error")
		shutil.move(log_name, log_path)

def main():
	watcher = file_changes_watcher.file_changes_watcher(WATCH_DIRECTORIES, ".tex", stopwords=STOPWORDS)
	while True:
		try:
			for file_path in watcher.get_changed_files():
				make_pdf(file_path)
		except Exception as e:
			print(sys.exc_info())
			raise e

		time.sleep(1)

if __name__ == "__main__":
    main()