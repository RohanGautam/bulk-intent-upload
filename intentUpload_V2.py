import re, csv, json
from copy import deepcopy
from pprint import pprint


with open(r'fake.json') as f:
    template_question=json.loads(f.read())
with open(r'fake_usersays_en.json') as f:
    template_userSays=json.loads(f.read())


pattern=r'[Ww]hat does (.*) mean' # some regular expressions to extract the meat of the question, to be used in the title of the intent
with open('bulk-acronym-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count!=0:
            intentName= 'F&B - '+re.findall(pattern,row[0])[0]
            trainingPhrase = row[0]
            response = row[1]
            q_copy=deepcopy(template_question)
            u_copy=deepcopy(template_userSays)

            q_copy['name']=intentName
            q_copy['responses'][0]['messages'][0]['speech']= response
            u_copy[0]['data'][0]['text']=trainingPhrase

            with open(f'acronyms/{intentName}.json','w') as f:
                f.write(json.dumps(q_copy))
            with open(f'acronyms/{intentName}_usersays_en.json','w') as f:
                f.write(json.dumps(u_copy))
            
        line_count+=1
