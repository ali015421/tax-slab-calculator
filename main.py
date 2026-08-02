
#first version of tax  calculator for  Pakistani users.

income= int(input("HELLO, Enter Your Income:"));

if income <= 600000:
     tax_owed= 0;
     print ("You owe no tax")

elif income <= 1200000:
     tax_owed = (income-600000)/100;
     print ("The tax you owe is:", tax_owed)

elif income <= 2200000:
     tax_owed = 6000+((income-1200000)/100)*11 ;
     print ("The tax you owe is:",tax_owed)

elif income <= 3200000:
     tax_owed = 116000+((income-2200000)/100)*23;
     print ("The tax you owe is:", tax_owed)

elif income <= 4100000:
     tax_owed = 346000+((income-3200000)/100)*30;
     print ("The tax you owe is:",tax_owed)

else:
     tax_owed = 616000+((income-4100000)/100)*35 ; 
     print ("The tax you owe is:",tax_owed)