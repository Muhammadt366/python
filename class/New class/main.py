my_dict = {}
print("empty dictonary", my_dict)

my_dict ={1:'apple',2:'ball'}
print('dict 1',my_dict)

my_dict = {'name': 'Ali',1:[2 , 4 , 3]}
print('dict 2', my_dict)

my_dict = {'name': 'Muhammad', 'age': 9}
print('dict 3', my_dict)

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 10
print('dictionary after age update', my_dict)

my_dict['address'] = 'Taxila'
print('dictionary after insert', my_dict)

my_dict.pop('age')
print('dictionary after removing age', my_dict)

print('address :',my_dict.get('address'))
print('dictionary after address', my_dict)

my_dict.clear()
print(my_dict)



