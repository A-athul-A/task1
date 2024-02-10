
# 4 * 7
print(" 4 * 7 ")
for i in range(1,5):
    
    for j in range(1,5):

        if i < 2:
            print(" ___",end='')
            print("  ",end='  ')
        
    print()
    for k in range(1,5):
            
        print("/   \\",end='')
    
        if k < 4:
            print("___",end='')
   
    print()
    for l in range(1,5):
        print("\\___/ ",end='  ')


print("\n")
 

# # 3 * 5
print(" 3 * 5 ")
for i in range(1,4):
    
    for j in range(1,4):

        if i < 2:
            print(" ___",end='')
            print("  ",end='  ')
        
    print()
    for k in range(1,4):
            
        print("/   \\",end='')
    
        if k < 3:
            print("___",end='')
   
    print()
    for l in range(1,4):
        print("\\___/ ",end='  ')



# output
#  4 * 7 
#  ___     ___     ___     ___    
# /   \___/   \___/   \___/   \
# \___/   \___/   \___/   \___/
# /   \___/   \___/   \___/   \
# \___/   \___/   \___/   \___/
# /   \___/   \___/   \___/   \
# \___/   \___/   \___/   \___/
# /   \___/   \___/   \___/   \
# \___/   \___/   \___/   \___/

#  3 * 5
#  ___     ___     ___
# /   \___/   \___/   \
# \___/   \___/   \___/
# /   \___/   \___/   \
# \___/   \___/   \___/
# /   \___/   \___/   \
# \___/   \___/   \___/

