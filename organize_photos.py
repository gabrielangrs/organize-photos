import os

# Change working directory to Photos
os.chdir("Photos")
# Assign variable 'originals' to list the contents of directory
originals = os.listdir()

def extract_place(filename):
	# Find first underscore in a string
	first = filename.find("_")
	# Slice from after first underscore and assign to variable 'partial'
	partial = filename[first+1:]
	# Find second underscore from leftover string
	second = partial.find("_")
	return partial[:second]

print(originals)