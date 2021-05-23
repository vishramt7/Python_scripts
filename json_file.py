
##############
# The analysis of json proceeds as follows
# Step 1 : Open it and load , use python library json
# Step 2 : check the type and length of individual objects
# Step 3 : If the object is a list => loop over it, If its a dictionary => print out the needed key's value 
# Iterate steps 2 and 3
##############

import json
#import pandas as pd
#from pandas.io.json import json_normalize

#f = open('furin_blastp.json')
#data = json.load(f)

#for values in data['BlastOutput2']:
#    print(values)

#f.close()

with open ('furin_pdb.json') as f:
    data = json.load(f)

output = open("pdb_complete_unique.txt","w")

#print(json.dumps(data, indent=2))
value = data['BlastOutput2']
print ("The type is", type(value), "The length is", len(value))
details = value[0]
print ("The type is", type(details), "and the length is",len(details))
print("The type is ", type(details['report']),"The length is", len(details['report']))

program_name = details['report']['program']
program_version = details['report']['version']
reference = details['report']['reference']
target_database = details['report']['search_target']['db']
parameters = details['report']['params']
results = details['report']['results']

print("program name = ", program_name, "target database was", target_database)
print("the size of results is", len(results), "the type is ", type(results))

result_hits = results['search']['hits']
print("The type of hits is ", type(result_hits), "the size of hits is", len(result_hits))

print ("num sciname bit_score score evalue identity")
unique_organisms = []
for result in result_hits:
    first_hit = result
#    print("The type of individual hit is ", type(first_hit), "the size of individual hit is", len(first_hit))
    hit_no = first_hit['num']
    
    description = first_hit['description']
    description_details = description[0]
    org_name = description_details['sciname']

    hsps = first_hit['hsps']
    score_details = hsps[0]
    bit_score = score_details['bit_score']
    score = score_details['score']
    evalue = score_details['evalue']
    identity = score_details['identity']

#   print ("num sciname bit_score score evalue identity")        
    if (identity >= 7):
#    if org_name not in unique_organisms:
        print(hit_no,",",  org_name, ",",bit_score, ",",score, ",",evalue, ",",identity, file=output)
#        unique_organisms.append(org_name)

#print(unique_organisms)
output.close()
#print (len('BlastOutput2'))
#print("the type of results is", type(values['report']['results']))

#df = pd.read_json('furin_blastp.json')
#columns = json_normalize(df['results'])
#print (columns)