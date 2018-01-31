def vowels(name):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    i = 0
    while i < len(name):
        x = name[i]
        if x in vowels:
            name = name.replace(x,"")
            #cotinue   ==> stops script
        #name += x
        i+=1
    return(name)

print(vowels("python"))
