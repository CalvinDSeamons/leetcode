# This functions takes in any string of length n containing either null, or a combination of (,),{,},[,].
# The goal is to return true of false if it's a valid nesting of parentheses.


def valid_parentheses(parens):  # Checking valid parentheses 

    counter = 0
    stack = []
    
    for char in parens:
        if counter == 0:
            stack.append(char)
        else:
            if (char == ')' and stack[len(stack)-1] == '(' or
                char == ']' and stack[len(stack)-1] == '[' or
                char == '}' and stack[len(stack)-1] == '{'):
                    
                    stack = stack[:-1] # pop off stack

            else:        
                stack.append(char)
            
        counter+=1
        if len(stack) == 0:
            counter = 0           

    if len(stack)==0:
        #print(f"True Stack:{stack}")
        return True
    else:
        #print(f"False Stack:{stack}")
        return False


tests = [
    "()", "([]){}", "([{}])", "(]", "({[)]}", 
    "((((((((()))))))))", "(((((((()", "))))", 
    "", "{}{}{}{}()()()[]", "()()()((((((((((((((((()))))))))))))))))[]"
]

for t in tests:
    print(f"{t:20} =  {valid_parentheses(t)}")
