def is_palindrome(name):
   reversed = name[::-1]
   return reversed == name 
name1 = input("Enter the word: ")
print(is_palindrome(name1))
