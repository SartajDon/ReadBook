def t2l(filename):
    ''' when given a text file, it remove 
    special characters, combine duolicate words
    and return all words in lower case'''
 
    with open (filename , "r") as f_obj:
        word_list = f_obj.read().split()
    
    lower_w_l = []
    for word in word_list:
        lower_w_l.append(word)
    
    lower_w_l.sort()
    
    for l_word in lower_w_l:
        print (l_word)  
    print(len(lower_w_l))
    import re
    red_sp_chr =[re.sub('[^a-zA-Z]+', '', _) for _ in lower_w_l]

try:    
    t2l(input(str("input your filename with directry "+"if it is somewhere else only  file name if" +
              " it is in same directry: ")))
except:
    print("please enter file directory correctly")


