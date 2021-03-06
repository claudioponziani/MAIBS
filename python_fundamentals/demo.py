
mydict = {
    'brand' : 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for key in mydict.keys():
    print("%s:%s" % (key, mydict[key]))

mydict['year'] = 2010
mydict['type'] = 'elettric'

cil = mydict.get('engine volume', 'ND')
print(cil)
x = mydict['engine volume'] if 'engine volume' in mydict else None

for k, v in mydict.items():
    print(k, v)

print("The brand of my car is %s and I bought it in %s" % (mydict['brand'], mydict['year']))