import hashlib
import os
from PIL import Image

for foto in os.listdir("/home/diego/Descargas/irudia"):
    ruta_completa = os.path.join("/home/diego/Descargas/irudia", foto)
    if foto.endswith('.jpg'):
        try:
            with open(ruta_completa, 'rb') as archivo:
                contenido = archivo.read()

            hash_obj = hashlib.md5()
            hash_obj.update(contenido)
            hash_resultado = hash_obj.hexdigest()
            if hash_resultado == "e5ed313192776744b9b93b1320b5e268":
                print(f'Archivo JPG encontrado: {foto} ')
        except Exception as e:
            print(f'Error al abrir {foto}: {e}')
