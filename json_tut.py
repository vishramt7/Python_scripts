import json

with open ('source-data.json') as input:
    content = json.load (input)

value = content['results']
#print("The type of value is", type(value), "The size of value is", len(value))
save_names = []
for parts in value:
    Individual_values = parts['replies']
#    print("Individual values",type (Individual_values))
    for details in Individual_values:
        names = details['user']['display_name']
        print("details are ", names)
        save_names.append(names)

with open('output.json','w') as output:
    json.dump(save_names,output)