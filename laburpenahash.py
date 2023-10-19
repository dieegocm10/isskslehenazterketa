import hashlib
import os

def main():
    aurkitua = False
    carpeta_irudia = "/home/diego/Descargas/irudia"

    for argazkia in os.listdir("/home/diego/Descargas/irudia"):
        ruta = os.path.join("/home/diego/Descargas/irudia", argazkia)
        if argazkia.endswith('.jpg'):
            with open(ruta, 'rb') as izena:
                edukia = izena.read()
            hash_obj = hashlib.md5()
            hash_obj.update(edukia)
            hash_emaitza = hash_obj.hexdigest()
            if hash_emaitza == "68745799f23dadff063fbd02bd38b547":
                aurkitua = True
                print("Zure irudia aurkitu da:", argazkia)

    if not aurkitua:
        print("Ez da zure irudirik aurkitu.")

if __name__ == "__main":
    main()
