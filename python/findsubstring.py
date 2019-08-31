def count_substring(string, sub_string):
    count = 0                                          #counter var
    for i in range(len(string)):
        if sub_string == string[i:i+len(sub_string)]:  #slicing the main string
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
   
