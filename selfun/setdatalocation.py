import pickle, os

def replaceNames(directory):

	print(directory)

	# Scan through datafolders in directory
	for folder in os.listdir(directory):
		# Scan through files in each folder
		print(folder)
		for file in os.listdir( os.path.join(directory, folder) ):
			print(file, os.path.join(directory, folder))
			# Search for info files
			if file.endswith('Information.pickle'):
				# Load infofile
				with open(os.path.join(directory, folder, file), "rb") as input:
					file_info  = pickle.load(input)

				print(file_info.data_path)
				# Replace directory with the correct one
				file_info.data_path = directory
				print(file_info.data_path)
				
				# Repickle file
				file_info.pickleInformation(file)

		print("")


if __name__ == '__main__':

	directory = raw_input("Location of data directory: ")

	replaceNames(directory)