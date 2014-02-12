import os

class file_changes_watcher:
	__files_last_modified = dict()

	def __init__(self, dirs, extension = "", watch_recursevely = True, stopwords = []):
		self.extension = extension
		self.dirs = dirs
		self.watch_recursevely = watch_recursevely
		self.stopwords = stopwords
		self.__update_all_files() #initialize __files_last_modified

	def __all_files(self):
		all_files = []
		for dir in self.dirs:
			if self.watch_recursevely:
				for root, dirs, files in os.walk(dir):
					all_files += [os.path.join(root,f) for f in files]
			else:
				for file in os.listdir(dir):
					path = os.join(dir, file)
					if os.path.isfile(path):
						all_files.append(path)

		all_files = [f for f in all_files if f.endswith(self.extension)]

		for stopword in self.stopwords:
			all_files = [f for f in all_files if f.count(stopword) == 0]

		return all_files

	def __changed_files(self):
		all_files = self.__all_files()
		for f in all_files:
			if self.__files_last_modified.get(f, None) != os.path.getmtime(f):
				yield f

	def __update_all_files(self):
		for f in self.__changed_files():
			self.__files_last_modified[f] = os.path.getmtime(f)

	def get_all_files(self):
		self.__update_all_files()
		return self.__all_files()

	def get_changed_files(self):
		changed_files = list(self.__changed_files())
		self.__update_all_files()
		return changed_files

	def is_smth_changed(self):
		return len(list(self.__changed_files())) > 0
