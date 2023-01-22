operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
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
    answer = [0,0]
    
else:
    answer = [max(answer),min(answer)]
print(answer)
    

