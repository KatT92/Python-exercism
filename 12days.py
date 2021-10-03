ong = [['first ', 'a Partridge in a Pear Tree. '],
         ['second ', 'two Turtle Doves, and '],
         ['third ', 'three French Hens, '],
         ['fourth ', 'four Calling Birds, '],
         ['fifth ', 'five Gold Rings, '],
         ['sixth ', 'six Geese-a-Laying, '],
         ['seventh ', 'seven Swans-a-Swimming, '],
         ['eighth ', "eight Maids-a-Milking, "],
         [' ninth ', "nine Ladies Dancing, "],
         [' tenth ', "ten Lords-a-Leaping, "],
         [' eleventh ', "eleven Pipers Piping, "],
         [' twelfth ', "twelve Drummers Drumming, "]]


result = []
j = []
l = 1

for i in range(len(song)):
    result.append("On the " + song[i][0] + "day of christmas, my true love gave to me: " + song[i][1])
    m = i
    while i >= 1:
        result.append(song[i - 1][1])
        j.append(i)
        i = i - 1
    l = l + 1
    #print(m)
    #print(l)
    result[m:(m+l)] = [''.join(result[m:(m+l)])]
print(result[12])


#result = result.split('a Partridge in a Pear Tree. ')


#k = (sum(set(j)))
#m += 1
#l = k + m + i
#print(k, l)
#result[k:l] = [''.join(result[k:l])]
#print(result)

