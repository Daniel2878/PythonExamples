# Outputting menu so user knows what program is
mainmenu = "MacLaine Design Invoice System"
print(mainmenu.center(60, '~'))

# Showing the Login screen where the user is asked for EmployeeID and password in order to get into the system
loginscreen = "Please input your Employee ID and password when prompted:"
print(loginscreen.center(60))

#creating a line spacer
spacer = '-'
print(spacer.center(60, '-'))

#creating blank spacer
spacer2 = " "


#Asking for the input for the employee's ID
employee_id = input("Employee ID(Letters only!): ")

#While loop that will repeat until an ID that is all alphabetical is entered
while (not employee_id.isalpha()):
  print("ID Rejected, try again!")
  employee_id = input("Employee ID(Letters only!): ")

#Asking for the input for the employee's password
employee_pass = input("Password: ")

#While loop that will repeat until digits are entered
while (not employee_pass.isalnum()):
  print ("Password Rejected, try again!")
  employee_pass = input("Password: ")
#Once the user inputs a proper ID and password, the log in will be successful
print("Login Successful!")

#line spacer
print(spacer.center(60, '-'))

#Once logged in, the employee will be asked to input data
trans_id = input("Now, input the transaction ID: ")

while (not trans_id.isdigit()):
  print ("Transaction ID rejected, try again!")
  trans_id = input("Input transaction ID: ")

#line spacer
print(spacer.center(60, '-'))

print ("Creating Invoice file with Transaction ID: " + trans_id)

#line spacer
print(spacer.center(60, '-'))

#asking the employee for more information
cust_name = input("Please type in the Customer Name: ")
date = input("Input sale date: ")


item_id = input("Input the Item ID #: ")
while (not item_id.isdigit()):
  print("Item ID not found, try again!")
  item_id = input("Input the Item ID #: ")

item_quantity = input("Input the item quantity: ")

subtotal = input("Please input the total $ amount for the sale: ")


#time to figure out if the customer is tax exempt or not
tax_ex = input("Is the customer tax exempt? Y for yes, N for no: ")

#setting the sales tax
salestax = 0.08

#while loop to determine tax exempt status and also the total of the customer's order
while not (tax_ex == "Y" or tax_ex == "y" or tax_ex == "N" or tax_ex == "n"):
  print("Invalid character")
  tax_ex = input("Is the customer tax exempt? Y for yes, N for no: ")
else:
  if tax_ex == "Y" or tax_ex == "y":
      tax_ex = tax_ex.upper()
      print("Customer will be exempt from sales tax.")
      total = float(subtotal)
  elif tax_ex == "N" or tax_ex == "n":
      print("Customer will not be exempt from sales tax.")
      tax_ex = tax_ex.upper()
      tax = (float(subtotal) * (salestax))
      total = float(tax) + float(subtotal)

#line spacer
print(spacer.center(60, '-'))

#printing the customer's total in $, either exempt from tax or not exempt
print("Customer Total: $%.2f" % (total))

#message to let the user know the invoice is being created and info is being submitted
print("Invoice #" + trans_id + " is being created.")

#all information is gathered to write up the invoice
invoices = open("invoices", "a")

#writing the information to the invoice file
invoice_title = (" MacLaine Design Invoice #: " + trans_id + " ")
invoices.write(invoice_title.center(125, '-'))
invoices.write("\n")
invoices.write("Customer Name: " + cust_name)
invoices.write("\n")
invoices.write("Sale Date: " + date)
invoices.write("\n")
invoices.write("Item ID: " + item_id + spacer2 * 5 + "Item Quantity: " + item_quantity)
invoices.write("\n")
invoices.write("Customer is exempt from sales tax(Y/N): " + tax_ex)
invoices.write("\n")
invoices.write("Sale Total: $%.2f" % (total))
invoices.write("\n")
invoices.write("Employee ID: " + employee_id + " created this invoice.")
invoices.write("\n")

#closing the invoice file
invoices.close()

