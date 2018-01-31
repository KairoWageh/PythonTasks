#names = ["kairo","ali","hoda"]
#i = 0
#key = ""
#value = ""
#while i < len(names):
#    key = names[i][0]
##    print(key + " : [" +value+"]")
#    i += 1

def dic(names):
    names.sort()
    result = {}
    for name in names:
        if name[0] in result :
            result[name[0]].append(name)
        else:
            result[name[0]] = [name]
    return result

names = ['kairo','wageh','koko']

print(dic(names))
