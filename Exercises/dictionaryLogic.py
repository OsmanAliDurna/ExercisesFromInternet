dict = {
    "name" : "Osman",
}
print('\n\n')
print(dict,'\t\t\t is default')
print(dict.items(), '\t is items', )
print(dict.keys(), '\t\t\t is keys')
print(dict.values(), '\t\t\t is values')
print('\n\n')

for i in dict:
    print(i, '\t\t\t is default for "for" loop')

for i in dict.items():
    print(i, '\t is items for "for" loop')

for i in dict.keys():
    print(i, '\t\t\t is keys for "for" loop')

for i in dict.values():
    print(i, '\t\t\t is values for "for" loop')