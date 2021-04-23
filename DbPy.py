#pip install virtualenvwrapper
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user0:gKGDWJlHy6qGZrhx@weathermentsdb.tdbnp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('WeathermentsDB')
test = db.TweetData # tweetData collection

'''
print(test.count_documents({})) #count number of documents, {} can be used to filter ex. 'name':'test'

new_entry = {
    'name':'test1',
    'num':123,
    'branch':'dev'
}

#test.insert_one(new_entry) # one entry

new_list = [
    {
    'name':'test2',
    'num':343
    },
    {
    'name':'test3',
    'num':123
    }
]

#test.insert_many(new_list) #list of dict

# all of these ^ operations make new db entries, they do not overwrite\

#find document
print(list(test.find())) # lsit of everyuthing 
print()
print(test.find_one({'name':'test3'}))

# update document
#update_one or update_many
test_update = {
    'name':'testNEW'
}
#test.update_one({'name':'test3'}, {'$set':test_update}) # or delete many, this will aplly the test_update to all documents FOUND

print(test.find_one({'name':'testNEW'}))

# deleate documents
#test.delete_one() or delete_many
test.delete_one({'name':'testNEW'})
print(test.find_one({'name':'testNEW'})) # returns none. it is deleted
'''
#  -- useful stuff ---------------------------------------------------
# object try
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("mike", 133)


test.insert_one(p1.__dict__)
print(test.find_one({'name':'mike'}))
print("found")

for i in (list(test.find())):
    print (i)
