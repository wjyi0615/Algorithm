word = input()
word = word.upper()
word_list = list(set(word)) #set으로 중복제거한 글자 리스트

#print(word)
cnt_list = []  
cnt = 0

for i in word_list:
    cnt = word.count(i)
    cnt_list.append(cnt)
    
#print(cnt_list)

if cnt_list.count(max(cnt_list))>1:
    print("?")
else: 
    print(word_list[cnt_list.index(max(cnt_list))])