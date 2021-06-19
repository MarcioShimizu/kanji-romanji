# -*- coding: shiftjis -*-
import pykakasi
import csv 
import json

def traduzir(japones):
  tradutor = pykakasi.kakasi()
  resultado = tradutor.convert(japones)
  for item in resultado:
    traduzido = item['hepburn']
  return traduzido
  
data = []
with open('input/text.csv', encoding='shiftjis') as csvFile:
  csvOpenedFile = csv.DictReader(csvFile)
  n = 1
  for row in csvOpenedFile:
    n = n + 1
    print(n)
    address1 = traduzir(row['7'])
    address2 = traduzir(row['8'])
    address3 = traduzir(row['9']) 
    kana1 = traduzir(row['4']) 
    kana2 = traduzir(row['5']) 
    kana3 = traduzir(row['6']) 
    dataOrganizado = {
      "address1": address1,
      "address2": address2,
      "address3": address3,
      "kana1": kana1,
      "kana2": kana2,
      "kana3": kana3,
      "zipcode": row['3']
    }
    data.append(dataOrganizado)
      
with open('output/traduzido.json', 'w', encoding='shiftjis') as jsonF:
		jsonF.write(json.dumps(data, indent=2))

