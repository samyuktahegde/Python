def reverse_strings_based_on_number_of_words(string):
    string_array = string.split(' ')
    n = len(string_array)
    prefix_array = []
    for i in range(n-1, -1, -2):
        prefix_array.append(''.join(string_array.pop(i)[::-1]))
    prefix_array.extend(string_array)
    return ' '.join(prefix_array)

string = "Ashish Yadav Abhishek Rajput Sunil Pundir"
print(reverse_strings_based_on_number_of_words(string))

        
        
