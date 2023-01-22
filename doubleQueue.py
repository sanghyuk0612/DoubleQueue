operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
answer = []
i = 0

while i<len(operations):
    
    if operations[i][0] == "I":
       j = 2
       string = ''
       while j<len(operations[i]):
           string += operations[i][j]
           j +=1
       answer.append(int(string))
    else:
        if len(answer)==0:
            pass
        
        elif operations[i][2] == "-":
            answer.remove(min(answer))
        else:
            answer.remove(max(answer))
    i+=1
if len(answer)==0:
    print("0 , 0")
else:
    print(min(answer))
    print(max(answer))
    

