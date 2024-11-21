def single_root_words(root_word,*other_words):
    same_words=[]
    root_word=root_word.upper()
    for i in other_words:
        other_words=i.upper()
        if root_word in other_words or other_words in root_word:
            same_words.append(i)
    return same_words



result1=single_root_words('rich','richest','orichalcum','cheers','richies')
result2=single_root_words('Disablement','Able','Mable','Disable','Bagel')
print(result1)
print(result2)