import os

# Function for extracting name of place from original filename
def extract_place(filename):
    return filename.split("_")[1]

# Function for making new directories from list of extracted places
def make_place_directories(places):
	for dir_name in places:
		os.mkdir(dir_name)

def organize_photos(directory):
	# Change working directory, list directory and assign that list to a variable
	os.chdir(directory)
	originals = os.listdir()
	# Empty list for extracted places
	places = []

	# Runs function to extract place name from original list and appends them to an empty list
	for filename in originals:
		place = extract_place(filename)
		# Checks if place name already exists, otherwise add it into list
		if place not in places:
		    places.append(place)

	# Makes new directories using places list
	make_place_directories(places)

	# Runs function to extract place name from original list, appends the path and moves the file into that path
	for filename in originals:
		place = extract_place(filename)
		os.rename(filename, os.path.join(place, filename))

organize_photos("Photos")
