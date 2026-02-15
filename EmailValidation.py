while True: # Loop until a valid email address is entered
   user = input("Enter your email address: ")
   if len(user) < 9: # Check if the email address has at least 9 characters
    print("Invalid email address because email character count is less than 9.")
   elif "@" not in user or "." not in user: # Check if the email address contains both @ and . symbols
    print("Invalid email address because @ or . is missing.")
   elif user.upper() != user and user.lower() != user: # Check if the email address contains both uppercase and lowercase letters
    print("Invalid email address because it contains both uppercase and lower letters.") 
   elif user.count("@") != 1: # Check if the email address contains exactly one @ symbol
    print("Invalid email address because @ symbol is not exactly one.")
   elif " " in user: # Check if the email address contains any spaces
    print("Invalid email address because it contains a space.")
   elif user.startswith("@") or user.endswith("@"): # Check if the email address starts or ends with @ symbol
    print("Invalid email address because @ is at the beginning or end.")
   elif user.startswith(".") or user.endswith("."): # Check if the email address starts or ends with . symbol
    print("Invalid email address because . is at the beginning or end.")
   else: # If all checks are passed, the email address is valid
    print("Congratulations! Your email address is valid.")
    break # Exit the loop if a valid email address is entered
