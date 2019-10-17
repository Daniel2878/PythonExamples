#calling  the veryprettytable from the plugin
from veryprettytable import VeryPrettyTable

#creating the prettytable
x = VeryPrettyTable()

#creating all of my lists needed
percents = []
salaries = []
employee_code = []
retdollarlist = []
netsalarylist = []

#function to add the employee, ssn, salary, and retirement %
def emp_new():
    name = input("Please input the employee name(First & Last): ")
    #splitting the input to find the last name of the employee
    lastname = name.split(' ')

    ssn = input("Input employee's SSN(###-##-####): ")
    # splitting the input to find the last 4 digits of the ssn
    lastfour = ssn.split('-')

    # combining the last name and last 4 digits of the ssn to make employee code
    employee_code.append(lastname[1] + lastfour[2])

    salary = int(input("Please input the employee's salary: "))
    salaries.append(salary)
# asking for the percent of salary towards the retirement amount
# using a while not loop to determine that the inputted value is between 0 and 40
    perc_salary = int(input("Input the % of salary contributed to retirement: "))
    while not (perc_salary > 0 and perc_salary < 40):
        print("Invalid percentage, please try again: ")
        perc_salary = int((input("Input the % of salary contributed to retirement: ")))
    else:
        percents.append(perc_salary)
        print("Data Accepted!")

# calling the add employee function, which will run 3 times
for k in range(0, 3):
    emp_new()

# zipping the 3 lists together
# to create a value for retirement dollars, net salary, and then also finding max salary and the person
# who has the max salary
for code, salary, ret in zip(employee_code, salaries, percents):
    retdollars = ((salary / 100 * ret))
    netsalary = (salary - retdollars)
    maxsalary = max(salaries)
    maxindex = salaries.index(maxsalary)
    maxemployee = employee_code[maxindex]
    round(retdollars)
    round(netsalary)
    retdollarlist.append(retdollars)
    netsalarylist.append(netsalary)

#created function to find the total for the salary list
def total_sal(salaries):
    saltotal = 0
    for x in salaries:
        saltotal += x
    return saltotal

#created function to find the total for the retirement $ list
def total_ret(retdollarlist):
    rettotal = 0
    for y in retdollarlist:
        rettotal += y
    return rettotal

#created function to find the total for the net salary list
def total_net(netsalarylist):
    nettotal = 0
    for u in netsalarylist:
        nettotal += u
    return nettotal

#rounding all of the totals to 2 decimal places
net_total =  total_net(netsalarylist)
roundednettotal = round(net_total, 2)
sal_total = total_sal(salaries)
roundedsaltotal = round(sal_total, 2)
ret_total = total_ret(retdollarlist)
roundedrettotal = round(ret_total, 2)


#rounding the lists themselves to two decimal places
roundedretdollarlist = [round(x, 2) for x in retdollarlist]
roundednetsalarylist = [round(x, 2) for x in netsalarylist]
roundedsalarieslist = [round(x, 2) for x in salaries]

#defining space as a place holder  to make room in the pretty table
space = ' '

#adding the information to the pretty table column by column
x.add_column("Employee Code", employee_code)
x.add_column("Salary($)", roundedsalarieslist)
x.add_column("Retirement($)", roundedretdollarlist)
x.add_column("Net Salary($)", roundednetsalarylist)

#adding a blank row to created space in the pretty table between the values and the totals
x.add_row([" ",space, space, space])
#adding the last total row to the pretty table
x.add_row(["Total($):", roundednettotal, roundedrettotal, roundedsaltotal])



#printing the pretty table with the title "Title Boxing Franchise"
print(x.get_string(title="Title Boxing Franchise"))

#printing the employee with the largest salary
print("Note! Employee: %s has the largest salary!" % maxemployee)