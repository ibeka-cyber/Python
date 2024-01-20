#Girilen ilk sayının x, ikincisinin y kabul edildiği bir polinomda
#P(x)=y ise True değilse false Döndüren programı yazınız.

# Sample input
#1 4
# x**3 + x**2 + x + 1
#****************************
#Sample Output
#True
if __name__ == "__main__":
    entry_value, exit_value = map(int, input().split(' ')) 
    polynom = input()
    
    p_function_text = 'lambda x:' + polynom
    p_function = eval(p_function_text)
    
    print(p_function(entry_value) == exit_value)