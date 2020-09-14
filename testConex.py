import json

def getDatosConex():
 with open('config.json') as json_files:
  data = json.load(json_files)
  for p in data['conexion']:
   print('Usuario: '+p['usuario'])
   print('Password: '+p['password'])
   print('URL: '+p['url'])

getDatosConex()
