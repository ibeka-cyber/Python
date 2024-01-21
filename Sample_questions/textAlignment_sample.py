#Çalıştır gör :)
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
    
# ************************************************
# Aynı teknik ile kalp çizdirmek
# ************************************************
#♥thickness = int(input()) 
c = 'İ'
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness ) + (c * i).rjust(thickness) + c + (c * i).ljust(thickness))

for i in range((thickness*2)-1):
    print((c*((thickness*2)-i-1)).rjust(thickness*2)+(c*((thickness*2)-i-1)).ljust(thickness*2))