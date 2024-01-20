#string içerisindeki belli karakteri değiştirmek

# Sample input
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# **********************************************
# Sample Output
# abrackdabra


def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    string="".join(s)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)