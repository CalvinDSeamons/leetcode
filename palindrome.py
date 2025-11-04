# Simple but poor palindrome

def is_palindrome(string):
    reverse = string[::-1] # Flip the word and compare, bad if word is 10bil chars long.
    if string==reverse:
        print("True")
    else:
        print("False") 

# Better function.
# This method is slighly better as it can tell if a word isn't 
# a palindrome w/o interating through the whole word. 
def better_is_palindrome(string):
    left, right = 0, len(string)-1 # Two counters one at head, one at tail.
    while left < right:
        if string[left] != string[right]: # Count in, if ever they dont match break with false.
            print("False")
            return
        left +=1
        right -=1
    # If you make it through you have a palindrome.
    print("True")
