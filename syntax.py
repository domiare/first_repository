                          #         PRINT
words = ["Welcome",'to','Python']

print(words)
# ['Welcome','to','Python']
print(*words,end="!\n")
# Welcome to Python!
print(*words,sep='\n')
# Welcome
# to
# Python
                       #        LEN

print(len(words))
# 3
word = "Welcome"
print(len(word))
# 7
