def count_words(string):
    count_dictionary = {}
    for i in range(len(string)):
        count_dictionary[string[i]] = count_dictionary.get(string[i], 0)+1
    result = 0
    for value in count_dictionary.values():
        if value==2:
            result+=1
    return result

# s = ["hate", "love", "peace", "love",
#       "peace", "hate", "love", "peace",
#                 "love", "peace"]
s = ["Om", "Om", "Shankar", "Tripathi", 
                "Tom", "Jerry", "Jerry"]
print(count_words(s))