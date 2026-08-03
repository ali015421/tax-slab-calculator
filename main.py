
#first version of tax  calculator for  Pakistani users.

income= int(input("Hello, Enter Your Income:"))

if income > 0:
    income_type = input("Is this Monthly or Annual? Enter M or A: ")

    if income_type == "M":
        income = income * 12 

    if income <= 600000:
        tax_owed = 0
        print ("You owe no tax")

    elif income <= 1200000:
        tax_owed = (income-600000)/100
        print ("The tax you owe is:", int(tax_owed))

    elif income <= 2200000:
        tax_owed = 6000+((income-1200000)/100)*11 
        print ("The tax you owe is:",int(tax_owed))

    elif income <= 3200000:
        tax_owed = 116000+((income-2200000)/100)*23
        print ("The tax you owe is:", int(tax_owed))

    elif income <= 4100000:
        tax_owed = 346000+((income-3200000)/100)*30
        print ("The tax you owe is:", int(tax_owed))

    else:
        tax_owed = 616000+((income-4100000)/100)*35  
       
        if income > 10000000:

         tax_owed = tax_owed + (tax_owed * 0.09)
        print("The tax you owe is:",int(tax_owed))
        
    
    tax_rate = int(tax_owed/income * 100)
    print("The tax rate is:", tax_rate)

    take_home_pay = int(income - tax_owed)
    print("The take home pay is:", take_home_pay)

else:
    print("Income cannot be zero or negative")



