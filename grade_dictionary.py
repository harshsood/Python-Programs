dict1={11210112:'Rohan',11210113:'Mohan',11210114:'Mandeep'}
dict2={11210112:85,11210113:88,11210114:90}
dict3={}
for keys in dict1.keys():
    marks=dict2.get(keys)
    if marks>=90 and marks<=100:
        dict3[keys]='O'
       
    if marks>=80 and marks<90:
        dict3[keys]='A+'
        
    if marks>=70 and marks<80:
        dict3[keys]='A'
        
    if marks>=60 and marks<70:
        dict3[keys]='B+'
       
print(dict3)
