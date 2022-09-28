# -*- coding: utf-8 -*-


import os
import json


with open('C:/Users/Dell/Desktop/taxon work/hse_pathogens.bacteria_w_taxa.json') as mf1:
    bacteria = json.load(mf1)

with open('C:/Users/Dell/Desktop/taxon work/hse_pathogens.fungi_w_taxa.json') as mf2:
    fungi = json.load(mf2)

with open('C:/Users/Dell/Desktop/taxon work/hse_pathogens.helminths_w_taxa.json') as mf3:
    helminths = json.load(mf3)

with open('C:/Users/Dell/Desktop/taxon work/hse_pathogens.protozoa_w_taxa.json') as mf4:
    protozoa = json.load(mf4)

init="curl -X GET --header 'Accept: text/xml' 'https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?filter="
end="&fields=id,name,collection_date,TAXONOMY,description,insdc_center_name,geographic_location_country_andor_sea'"

query = init

for i in range(len(bacteria)):
    query += "%20TAXONOMY:"+str(bacteria[i]["taxon_id"])+"%20OR%20"
    
for i in range(len(fungi)):
    query += "%20TAXONOMY:"+str(fungi[i]["taxon_id"])+"%20OR%20"

for i in range(len(helminths)):
    query += "%20TAXONOMY:"+str(helminths[i]["taxon_id"])+"%20OR%20"


for i in range(len(protozoa)):
    query += "%20TAXONOMY:"+str(protozoa[i]["taxon_id"])
    if i < len(protozoa)-1:
        query += "%20OR%20"  

query += end

output_url = open("C:/Users/Dell/Desktop/taxon work/output.txt","w")
output_url.write(query)
output_url.close()

output = "C:/Users/Dell/Desktop/taxon work/output.xml"
os.system(query+" > "+output)




