import hashlib
import os
from PIL import Image

def main():
	aurkitua = False
	
	for argazkia in os.listdir("/home/diego/Descargas/irudia"):
		ruta = os.path.join("/home/diego/Descargas/irudia", argazkia)
		ruta = ("/home/diego/Descargas/irudia", argazkia)
		if argazkia.endswith('.jpg'):
			with open(ruta, 'rb') as izena:
				edukia = izena.read()
			hash_obj = hashlib.md5()
			hash_obj.update(edukia)
			hash_emaitza = hash_obj.hexdigest()
			if hash_emaitza == "e5ed313192776744b9b93b1320b5e268" : 							
				aurkitua = True
				print("Zure irudia aurkitu da: ", argazkia)
				


if __name__ == "__main__": 
	main()
