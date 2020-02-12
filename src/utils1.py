from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('web_clm')
password = urllib.parse.quote_plus('cisco123')

#uri = "mongodb://web_clm:cisco123@192.168.110.208/?authSource=clm&authMechanism=SCRAM-SHA-1"

client = MongoClient('mongodb://%s:%s@192.168.110.208/?authSource=clm&authMechanism=SCRAM-SHA-1' % (username, password))
# client = MongoClient("mongodb://web_clm:cisco123@192.168.110.208")
# client = MongoClient(uri)

db = client.clm

# csv_file = open('mongo_output.csv', 'w')

csv_record = []

try: 
     col = db.textfsm_all_record_1
     for x in col.find({"PARSE_OUTPUT" : True, "COMMAND_OUTPUT" : True},{"template":-1, "output":-1}):
         csv_record.append([x['output'], x['template']])
         
except Exception as e:
    raise e

else:
    print("Connected Succesfully")

client.close()

