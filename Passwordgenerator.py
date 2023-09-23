import random
def genepass(length,char=None):
    if char==None:
        char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_/*<>'"
    password=""
    for i in range(length):
     password+=random.choice(char)
    return password
print(genepass(10))
