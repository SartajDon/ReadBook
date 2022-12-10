#opening humgergamest.txt as list
with open ("hunger_games.txt","r") as file_object:

    word_list = file_object.read().split()
    #lower case list making
    lower_word_list = []
    for word in word_list:
        lower_word_list.append(word.lower())

    #reducing reoeated words from hunger_games.txt
    lower_reduced_set_list=set(lower_word_list)

    #to remove special characters
    import re
    new_hg_list =[re.sub('[^a-zA-Z0-9]+', '', _) for _ in lower_reduced_set_list]


#opening common_words.txt as list
with open ("common_words.txt" , "r") as sec_file_object:
    sec_word_list = sec_file_object.read().split()

    #lowercase list making
    lower_sec_word_list = []
    for word in lower_sec_word_list:
        lower_sec_word_list.append(word.lower())
    #reducing reoeated words from hunger_games.txt
    mew_list =set(lower_word_list)

#identifying common wirds availabke in humger_games.txt
for common_word in lower_sec_word_list:
    while  common_word in new_hg_list:

        #removing commin words feom hunger games
        new_hg_list.remove(common_word)



for words in new_hg_list:
   print(words)

print(len(new_hg_list))
