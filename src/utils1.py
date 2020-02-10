from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('web_clm')
password = urllib.parse.quote_plus('cisco123')

uri = "mongodb://web_clm:cisco123@192.168.110.208/?authSource=clm&authMechanism=SCRAM-SHA-1"

client = MongoClient('mongodb://%s:%s@192.168.110.208/?authSource=clm&authMechanism=SCRAM-SHA-1' % (username, password))
# client = MongoClient("mongodb://web_clm:cisco123@192.168.110.208")
# client = MongoClient(uri)
db = client.clm
try: 
     col = db.textfsm_all_record_1
   # print(col.insert_one({'test':"example"}).inserted_id)
     text_file = open("sample.txt", "w")
     for x in col.find({},{"output": 1}):
  #  x = col.find({}, {"output":1})
         n = text_file.write(x['output'])    
         print(x['output'])
     text_file.close()

except Exception as e:
    raise e

else:
    print("Connected Succesfully")

client.close()    

