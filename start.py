def myPrint(s):
    print(s)
    
    def printTab(text, n=0):
        print('\t'*n + text)    
        
    printTab('Hello', 1)
    printTab('World', 2)