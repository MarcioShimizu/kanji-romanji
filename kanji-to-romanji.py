# -*- coding: shiftjis -*-
import pykakasi
import csv 
import json
from time import sleep




def translate(japanese):
  translater = pykakasi.kakasi()
  result = translater.convert(japanese)
  for item in result:
    translated = item['hepburn']
  return translated

def insert_dash(string, index):
    result =  translate(string[:index]) + '-' + translate(string[index:])
    return result

#---------------------------------------

data = []
count = 0
a = 1000
print('inicio')
with open('input/text.csv', encoding='shiftjis') as csvFile:
  csvOpenedFile = csv.DictReader(csvFile)
  for row in csvOpenedFile:
    
    count = count + 1
    if count == a:
      print(a)
      a = a + 1000
    
    roman1 = translate(row['7']) if row['7'] == '�k�C��' else insert_dash(row['7'], -1)
    
    roman2 = insert_dash(row['8'], -1)
   
    roman3 = translate(row['9']) 
    kana1 = translate(row['4']) 
    kana2 = translate(row['5']) 
    kana3 = translate(row['6']) 
    kanji1 = row['7']
    kanji2 = row['8']
    kanji3 = row['9']
    zipcode = insert_dash(row['3'], 4)
    dataOrganizado = {
      "roman1": roman1,
      "roman2": roman2,
      "roman3": roman3,
      "kana1": kana1,
      "kana2": kana2,
      "kana3": kana3,
      "kanji1": kanji1,
      "kanji2": kanji2,
      "kanji3": kanji3,
      "zipcode": row['3'],
    }
    data.append(dataOrganizado)
      
    with open(f'output/end/ende-{count}.json', 'w', encoding='shiftjis') as jsonF:
        jsonF.write(json.dumps(data, indent=2))
    data.clear()
