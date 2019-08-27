import os

def extract_place(filename):
    return filename.split("_")[1]

os.chdir("Photos")
originals = os.listdir()
places = []

for filename in originals:
    places.append(extract_place(filename))