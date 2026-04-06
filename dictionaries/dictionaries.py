# this stores data in key value pair also this can accept list,tupple and set

dic={'ganesh':'frontend','mahesh':'c#','vaibhav':"backend",'sajjan':'AI'}
print("there are two ways to fetch the perticular data from the dictionaries: ","1- ",dic.get('sajjan'),"2- ",dic['vaibhav'])

list=["ind","aus","pak","eng","ind","sa","nz"]
tupple={"virat","smith","babar","ben","virat","ab","michel"}
set=("rcb","csk","mi","srh","kkr","dc","pbks")
cricket=dict(zip(tupple,set))
print("merged two tupple and set: ",cricket)

d={'ganesh':'frontend','mahesh':'c#','vaibahv':['backend','AI','java'],'sajjan':{'class':'management','language':'java'}}
print(d["sajjan"]["class"])