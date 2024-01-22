

def minion_game(string):
    kevin_words,kevin_start_let,stuart_words,stuart_start_let=[],[],[],[]
    kevin_score,stuart_score=0,0
    wovels="AEIOU"
    total=0
    count=0
    substring_list=[]
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] not in substring_list:
                substring_list.append(string[i:j])
        
    
    for i in string:
        if i in wovels:
            if i not in kevin_start_let:
                kevin_start_let.append(i)
        else:
            if i not in stuart_start_let:
                stuart_start_let.append(i)
                
                
    for i in kevin_start_let:       
        for j in substring_list:
            if j[0]==i[0] and j not in kevin_words:
                kevin_words.append(j)
    for i in range(len(string)):
        for word in kevin_words: 
            if string[i:i+len(word)]==word:
                kevin_score+=1
       
    for i in stuart_start_let:       
        for j in substring_list:
            if j[0]==i[0] and j not in stuart_words:
                stuart_words.append(j)
    for i in range(len(string)):
        for word in stuart_words: 
            if string[i:i+len(word)]==word:
               stuart_score+=1
    
    
    if stuart_score>kevin_score:
        print("Stuart",stuart_score)
        
    elif stuart_score<kevin_score:
        print("Kevin",kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)                    
                        
                        
# ************************************************************************
# S = input().strip()
# S_length = len(S)
# player1, player2 = 0,0

# for i in range(S_length):
#     if S[i] in "AEIOU":
#         player1 += S_length - i
#         print("p1",player1)
#     else:
#         player2 += S_length - i    
#         print("p2",player2)
        
# if player1 > player2:
#     print ("Kevin", player1)
# elif player1 < player2:
#     print ("Stuart", player2)
# else:
#     print ("Draw")