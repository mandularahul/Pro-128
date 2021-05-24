from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')
print(len(star_table))


temp_list= []
table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)



Star_names = []
Constellation = []
RightAscension = []
Declination = []
Appmag = []
Distance = [] 
Spectraltype = []
Browndwarf= []
Mass= []
Radius = []
orbitalperiod = []
Discoverydate = []


for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Constellation.append(temp_list[i][2])
    RightAscension.append(temp_list[i][3])
    Declination.append(temp_list[i][4])
    App.mag.append(temp_list[i][5])
    Spectraltype.append(temp_list[i][7])
    Browndwarf.append(temp_list[i][8])
    orbitalperiod.append(temp_list[i][11])
    Discoverydate.append(temp_list[i][12])
    Distance.append(temp_list[i][6])
    Mass.append(temp_list[i][9])
    Radius.append(temp_list[i][10])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_names','Constellation','Right Ascension','Declination','App.mag','Distance','Spectral type','Brown dwarf','Mass','Radius','orbital period','Discovery date'])
print(df2)

df2.to_csv('dwarf_stars.csv')
