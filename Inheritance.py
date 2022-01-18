class Setup( object ):
	def __init__(self):
		print('Set up database connection, initialize stuff.')

	def setup_db(self):
		print('Db setup!')

	def initialize_stuff(self):
		print('Initialized stuff!')

class DiskWriting(Setup):
	def __init__(self):
		print('Class handling all disk writing.')

	def write_disk(self):
		print('Wrote disk!')

class DiskReading(Setup):
	def __init__(self):
		print('Class handling all disk reading.')

	def read_disk(self):
		print ('Read disk!')

class MainApplication( DiskWriting, DiskReading ):
	def __init__(self):
		print('My main app!')

		# Setup
		self.setup_db()
		self.initialize_stuff()

		# Work!
		self.write_disk()
		self.read_disk()



my_app = MainApplication()