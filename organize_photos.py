import os

# Change working directory to Photos
os.chdir("Photos")
# Assign variable 'originals' to list the contents of directory
originals = os.listdir()

# Find first underscore in a string
first = filename.find("_")
# Slice from after first underscore and assign to variable 'partial'
partial = filname[first+1:]

# Find second underscore from leftover string
second = partial.find("_")
destination = partial[:second]

print(originals)