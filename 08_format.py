letter = '''Dear <|NAME|> ,
Greeting from LWF company.
You are selected!
Have a great day ahead!
Thanks and regards ,
Prince jaiswal
Date : <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("|NAME|", name)
letter = letter.replace("|DATE|", date)
print(letter)