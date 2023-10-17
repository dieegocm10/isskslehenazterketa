import hashlib
import os
from PIL import Image

def main():
	aurkitua = False
	
	for argazkia in os.listdir("/home/jon/1.Laborategia/irudia"):
		ruta = os.path.join("/home/jon/1.Laborategia/irudia", argazkia)
		if argazkia.endswith('.jpg'):
			with open(ruta, 'rb') as artxiboa:
				edukia = artxiboa.read()
			hash_obj = hashlib.md5()
			hash_obj.update(edukia)
			hash_emaitza = hash_obj.hexdigest()
			if hash_emaitza == "e5ed313192776744b9b93b1320b5e268" : 							
				aurkitua = True
				print("Zure irudia aurkitu da: ", argazkia)
				
					













if __name__ == "__main__": 
	main()
