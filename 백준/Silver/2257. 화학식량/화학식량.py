chemical = input()

HCO = {'H': 1, 'C': 12, 'O': 16}  
stack = [] 

for i in range(len(chemical)):
  if chemical[i] in HCO:  
      stack.append(HCO[chemical[i]])
  elif chemical[i].isdigit(): 
      stack[-1] *= int(chemical[i])
  elif chemical[i] == '(': 
      stack.append('(')  
  elif chemical[i] == ')':
      temp = 0
      while stack and stack[-1] != '(':
          temp += stack.pop()
      stack.pop() 
      stack.append(temp) 

print(sum(stack))
