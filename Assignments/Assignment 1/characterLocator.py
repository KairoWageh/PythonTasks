def location(string,letter):
    locations = []
    i = 0
    while i<len(string):
        l = string[i]
        if letter in string:
            if l== letter:
                locations.append(i)
        else:
            print("not found")
        i+=1
    return(locations)
print(location("kairo is a clever girl","i"))
