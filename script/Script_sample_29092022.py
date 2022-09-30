# -*- coding: utf-8 -*-

"""
Created on Thu Sep 29 14:55:26 2022

@author: kgy
"""

import os
import json
import webbrowser 


init1="curl -X GET --header 'Accept: text/xml' 'https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?filter="
init2= "https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?filter="
end="&size=15" # &fields=id,name,collection_date,TAXONOMY,description,insdc_center_name,geographic_location_country_andor_sea'"

'''
this function allows to read the json file 
but also to get the taxon_id and to launch the results in the webbrowser.
'''

def requet (file_directory):
    with open(file_directory) as mf:
        file = json.load(mf)
    query = init2
    for i in range(len(file)):
        query += "%20TAXONOMY:"+str(file[i]["taxon_id"])
        if i < len(file)-1:
            query += "%20OR"
    query += end
    webbrowser.open_new_tab(query)

# requet('C:/Users/Dell/Desktop/taxon work/hse_pathogens.bacteria_w_taxa.json')
# requet('C:/Users/Dell/Desktop/taxon work/hse_pathogens.fungi_w_taxa.json')
# requet('C:/Users/Dell/Desktop/taxon work/hse_pathogens.helminths_w_taxa.json')
requet('C:/Users/Dell/Desktop/taxon work/hse_pathogens.protozoa_w_taxa.json')



# # output = "C:/Users/Dell/Desktop/taxon work/output.xml"
# # os.system(query+" > "+output)




