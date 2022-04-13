import ast

reader = open("testfiel.txt",'r')
lines = reader.readlines()

for line in lines:
    book = ast.literal_eval(line)
    print(book,type(book))
    
    


reader.close()