import hashlib
import os

def main():
    aurkitua = False
    carpeta_irudia = "/home/diego/Descargas/irudia"

    for argazkia in os.listdir(carpeta_irudia):
        ruta = os.path.join(carpeta_irudia, argazkia)
        if argazkia.endswith('.jpg'):
            with open(ruta, 'rb') as izena:
                edukia = izena.read()
            hash_obj = hashlib.md5()
            hash_obj.update(edukia)
            hash_emaitza = hash_obj.hexdigest()
            if hash_emaitza == "e5ed313192776744b9b93b1320b5e268":
                aurkitua = True
                print("Zure irudia aurkitu da:", argazkia)

    if not aurkitua:
        print("Ez da zure irudirik aurkitu.")

if __name__ == "__main":
    main()
