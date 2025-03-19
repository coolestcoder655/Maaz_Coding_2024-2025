# WAP that checks if a user input is a valid email (contains "@" and ends with ".com")

email_UnVal = input("Welcome to Email Validator \n Please enter the email to be validated:")
email_UnVal_At_Count = email_UnVal.count("@")
email_UnVal_Com_Count = email_UnVal.count(".com")
email_UnVal_2_Dot = email_UnVal.endswith("..com")

if "@" in email_UnVal and email_UnVal_At_Count == 1 and email_UnVal.endswith(".com") and email_UnVal_Com_Count == 1 and email_UnVal_2_Dot != True:
    print("The email entered '", email_UnVal, "' is valid and can be used.")
else:
    print("The email'", email_UnVal, "' is not valid and has to be changed. It has to contain a '@' and end with '.com' to be valid.")