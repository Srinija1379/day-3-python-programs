def editDistance(str1, str2, m, n):
 
    
    if m == 0:
        return n
 
   
    if n == 0:
        return m
 
    
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
 
    
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
 
 

str1 = input("word1=")
str2 = input("word2=")
print (editDistance(str1, str2, len(str1), len(str2)))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
St
