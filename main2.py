students=[
    [1,"sukhit",6],
    [2,"max",5],
    [3,"jack",3],
    [4,"veer",4],
    [5,"reyansh",2]
]
dict={}
for item in students:
    dict[item[0]]=item[1:3]
print(dict)