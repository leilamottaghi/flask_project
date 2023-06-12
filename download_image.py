
import sqlite3
from urllib.request import Request, urlopen
import requests
import PIL
import numpy
from PIL import Image
from PIL import Image
import glob
import glob, os

def Convert_images_to_list():
	connection = sqlite3.connect("database.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM posts ')
	result = crsr.fetchall()
	barcode_list =[]
	for row in result:
		barcode = row[16]
		print(barcode)
		barcode_list.append(str(barcode).lower())
	image_list = []
	for barcode in barcode_list:
		image_str_list =[]		
		for file in glob.glob("img/%s"%(barcode)):
			for image in glob.glob("img/%s/*.jpeg"%(barcode)):
				image_str_list.append(image)
		# print(image_str_list)
		image_list.append(image_str_list)
		# images_str = "|".join(image_list)

	# print(image_list)
	# print(images_str)

	dict_images = dict(zip(barcode_list, image_list))
	print(dict_images)

def Convert(string):
    li = list(string.split("|"))
    return li
  
def download_images():
	connection = sqlite3.connect("database.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM posts ')
	result = crsr.fetchall()
	
	for row in result:
		image_list = row[14]
		barcode = row[6]
		try:
			if len(image_list) != 0:
				img_list = Convert(image_list)
				alphab = ['a','b','c','d','e','f','g','h','i','j','k','l']
				for img in img_list:
					print(img)
					if img != '':
						req = Request(str(img), headers={'User-Agent': 'Mozilla/5.0'})
						f = urlopen(req)
						parent_dir = "trendyol_images/"
						directory = str(barcode)
						history_directoy = parent_dir + directory			
						if not os.path.isdir(history_directoy):
							path = os.path.join(parent_dir, directory)
							os.mkdir(path)
							print("Directory '%s' created" % directory)
						# with open(str(history_directoy)+"/"+"%s-lcwikiki-%s.webp"%(barcode,alphab[0]), "wb") as local_file:			
				
						with open(str(history_directoy)+"/"+"%s-trendyol-%s.jpeg"%(barcode,alphab[0]), "wb") as local_file:			
						# with open("img/%s/%s%s.jpeg"%(barcode,barcode,alphab[0]), "wb") as local_file:
							local_file.write(f.read())
						local_file.close()
						alphab.pop(0)
			else:
				break
				# continue
		except Exception as e:
			print(e)
	connection.commit()
	connection.close()
		
download_images()
# Convert_images_to_list()