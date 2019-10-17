# importing the functions that are needed
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Tesla import *

# creating the inventory for Rochester, New York
inv1 = TeslaInventory("Rochester", "New York")
# creating the stafflist
stafflist = []
# creating 3 new instances for existing staff members
emp1 = StaffMember("Daniel", "Pierson", "Manager")
emp2 = StaffMember("William", "Johnson", "Salesman")
emp3 = StaffMember("Giovanni", "Carlisle", "Salesman")

# adding the employees I created to the list
stafflist.append(emp1)
stafflist.append(emp2)
stafflist.append(emp3)

# creating the existing cars for the car inventory
car1 = TeslaCar("Blue", 2019, "Roadster", 23345)
car2 = TeslaCar("Red", 2018, "Model 3", 45200)
car3 = TeslaCar("Black", 2019, "Model Y", 12000)
car4 = TeslaCar("Silver", 2018, "Model X", 5000)
car5 = TeslaCar("Silver", 2019, "Model Y", 56000)
car6 = TeslaCar("Black", 2019, "Roadster", 0)

# adding the existing cars to the inventory
inv1.addCar(car1)
inv1.addCar(car2)
inv1.addCar(car3)
inv1.addCar(car4)
inv1.addCar(car5)
inv1.addCar(car6)

# print function for the staff members, with their first name, last name, and position
def printStaff():
    for member in stafflist:
        print(member.displayStaffMember())

# creating the class for the root of the GUI
class TeslaManagementSystem(tk.Tk):

    # defining the class for the root of the GUI
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand=True)
        # adding the title to the top of the frame that shows first
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry('600x500')
        self.title('Tesla Management System')

        # New Menu Code Here
        # create a toplevel menu
        menubar = tk.Menu(self)
        menubar.add_command(label="Quit!", command=self.quit)
        # display the menu
        self.config(menu=menubar)

        # creating a dictionary for the frames that are stored in the root
        self.frames = {}
        # looping through the frame dictionary
        for F in (StartPage, VehicleMenu, StaffMenu, InventoryMenu, addVehicle, removeVehicle, showInvent
                  , addStaff, removeStaff, showStaff):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# creating a frame for the starting page that the user first sees
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tesla Inventory Management")
        label.pack(pady=10, padx=10)
        # buttons for the different menus/frames
        button = tk.Button(self, text="Vehicle Menu", width='15', height='2',
                           command=lambda: controller.show_frame(VehicleMenu))
        button.pack()

        button2 = tk.Button(self, text="Staff Menu", width='15', height='2',
                            command=lambda: controller.show_frame(StaffMenu))
        button2.pack()

        button3 = tk.Button(self, text="Inventory Menu", width='15', height='2',
                            command=lambda: controller.show_frame(InventoryMenu))
        button3.pack()

# defining the class(frame) for the vehicle menu
class VehicleMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Vehicle Menu")
        label.pack(pady=10, padx=10)
        # creating the buttons for the different options on the vehicle menu
        # add vehicle to inventory button which takes the user to the add vehicle frame
        button1 = tk.Button(self, text="Add Vehicle to Inventory", width='25', height='2',
                            command=lambda: controller.show_frame(addVehicle))
        button1.pack()
        # remove vehicle to inventory button which takes the user to the remove vehicle frame
        button2 = tk.Button(self, text="Remove Vehicle from Inventory", width='25', height='2',
                            command=lambda: controller.show_frame(removeVehicle))
        button2.pack()
        # main menu button which takes the user to the main menu frame
        button3 = tk.Button(self, text="Back to Main Menu", width='25', height='2',
                            command=lambda: controller.show_frame(StartPage))
        button3.pack()

# creating the inventory menu(frame)
class InventoryMenu(tk.Frame):
    # defining the class for the inventory menu frame, attaching it to the parent frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Inventory Menu")
        label.pack(pady=10, padx=10)
        # button that takes the user to the current inventory frame
        button1 = tk.Button(self, text="Show current Inventory", width='20', height='2',
                            command=lambda: controller.show_frame(showInvent))
        button1.pack()
        # button that takes the user back to the main menu
        button2 = tk.Button(self, text="Back to Main Menu", width='20', height='2',
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()
# staff menu class/frame being instantiated
class StaffMenu(tk.Frame):
    # attaching the staff menu and defining it
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Staff Menu")
        label.pack(pady=10, padx=10)
        # add staff member button which takes the user to the add staff frame
        button1 = tk.Button(self, text="Add Staff Member", width='20', height='2',
                            command=lambda: controller.show_frame(addStaff))
        button1.pack()
        # remove staff member button which takes the user to the remove staff frame
        button2 = tk.Button(self, text="Remove Staff Member", width='20', height='2',
                            command=lambda: controller.show_frame(removeStaff))
        button2.pack()
        # show staff list button that takes the user to the show staff frame
        button3 = tk.Button(self, text="Show Staff List", width='20', height='2',
                            command=lambda: controller.show_frame(showStaff))
        button3.pack()
        # main menu button
        button4 = tk.Button(self, text="Back to Main Menu", width='20', height='2',
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()
# creating the frame to add the vehicle to the inventory
class addVehicle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Input Information and click 'Add'")
        label.pack(pady=10, padx=10)
        # labeling all of the buttons with the different parameters that the new car needs
        # then creating the text boxes for the different user entries
        label_1 = tk.Label(self, text="Color:")
        label_1.pack()

        self.entry1 = tk.Entry(self, width=20)
        self.entry1.pack()

        label_2 = tk.Label(self, text="Year:")
        label_2.pack()

        self.entry2 = tk.Entry(self, width=20)
        self.entry2.pack()

        label_3 = tk.Label(self, text="Model:")
        label_3.pack()

        self.entry3 = tk.Entry(self, width=20)
        self.entry3.pack()

        label_4 = tk.Label(self, text="Miles:")
        label_4.pack()

        self.entry4 = tk.Entry(self, width=20)
        self.entry4.pack()
        # add button which takes the user entries and forms them into a new car
        # then appends the new car instance to the carlist in the inventory
        # the entries are then deleted from the entry boxes so a new cars information
        # can be entered
        button1 = tk.Button(self, text="ADD!!", width='20', height='2',
                            command=lambda: self.combine_funcs(self.getCarEntry(), self.entry1.delete(0, END),
                                                          self.entry2.delete(0, END), self.entry3.delete(0, END),
                                                          self.entry4.delete(0, END)))
        button1.pack()
        # button that takes you to the vehicle main menu
        button2 = tk.Button(self, text="Back to Vehicle Menu", width='20', height='2',
                            command=lambda: controller.show_frame(VehicleMenu))
        button2.pack()

    # creating the function that takes the user entries and stores them in variables for color,year,model,mileage
    # this function also forms the information into a new TeslaCar instance, then appends it to the carlist
    def getCarEntry(self):
        colorp = self.entry1.get()
        yearp = self.entry2.get()
        modelp = self.entry3.get()
        mileagep = self.entry4.get()

        newcar = TeslaCar(colorp, int(yearp), modelp, int(mileagep))
        inv1.addCar(newcar)
        inv1.printUpdatedInventory()
    # funciton that allows the use of multiple functions on one button
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

# creating the remove vehicle frame
class removeVehicle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_1 = tk.Label(self, text="Enter Vehicle Details to Remove")
        label_1.pack(pady=10, padx=10)
        # labeling all of the buttons with the different parameters that
        # the system needs to identify the car to remove
        # then creating the text boxes for the different user entries
        label_2 = tk.Label(self, text="Color:")
        label_2.pack()

        self.entry1 = tk.Entry(self, width=20)
        self.entry1.pack()

        label_3 = tk.Label(self, text="Year:")
        label_3.pack()

        self.entry2 = tk.Entry(self, width=20)
        self.entry2.pack()

        label_4 = tk.Label(self, text="Model:")
        label_4.pack()

        self.entry3 = tk.Entry(self, width=20)
        self.entry3.pack()

        label_5 = tk.Label(self, text="Miles:")
        label_5.pack()

        self.entry4 = tk.Entry(self, width=20)
        self.entry4.pack()
        # remove button which takes the user entries and checks the inventory for a car instance that matches
        # all the same parameters and then removes that car from the inventory/car list
        #
        # the entries are then deleted from the entry boxes so a new cars information
        # can be entered
        button1 = tk.Button(self, text="Remove!!", width='20', height='2',
                            command=lambda: self.combine_funcs(self.getCarEntry(), self.entry1.delete(0, END),
                                                               self.entry2.delete(0, END), self.entry3.delete(0, END),
                                                               self.entry4.delete(0, END)))
        button1.pack()
        # button that takes the user back to the vehicle main menu
        button2 = tk.Button(self, text="Back to Vehicle Menu", width='20', height='2',
                            command=lambda: controller.show_frame(VehicleMenu))
        button2.pack()
    # same function as up above, getting the user entry and storing the information as color,year,model,mileage
    # then creates an instance and removes the already existing car instance that it matches
    def getCarEntry(self):
        colorp = self.entry1.get()
        yearp = self.entry2.get()
        modelp = self.entry3.get()
        mileagep = self.entry4.get()

        newcar = TeslaCar(colorp, int(yearp), modelp, int(mileagep))
        inv1.removeCar(newcar)
        print("There are now %d cars in the Inventory!" % (len(inv1.carlist)))
        inv1.printCars()
    # function that allows a button to use multiple functions when pressed
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
           for f in funcs:
                f(*args, **kwargs)

        return combined_func
# creating the showinvent frame
class showInvent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Current Inventory List!")
        label.pack(pady=10, padx=10)
        # button that allows the user to show the total # of cars in the inventory
        button1 = tk.Button(self, text='Click to print total cars in inventory list in console', width='40', height='2',
                            command=lambda: inv1.printInventory())
        button1.pack()
        # button that allows the usr to print each of the cars in the inventory
        button2 = tk.Button(self, text='Click to print the list of cars in the inventory in console', width='40',
                            height='2', command=lambda: inv1.printCars())
        button2.pack()
        # button that takes the user back to the inventory main menu
        button3 = tk.Button(self, text="Back to Inventory Menu", width='40', height='2',
                            command=lambda: controller.show_frame(InventoryMenu))
        button3.pack()

# creating the add staff frame
class addStaff(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Staff Member information and click 'Add'")
        label.pack(pady=10, padx=10)
        # creating the labels and entries for the first name, last name, and postion that is needed
        # to create the new staff members
        label_1 = tk.Label(self, text="First Name:")
        label_1.pack()

        self.entry1 = tk.Entry(self, width=20)
        self.entry1.pack()

        label_2 = tk.Label(self, text="Last Name:")
        label_2.pack()

        self.entry2 = tk.Entry(self, width=20)
        self.entry2.pack()

        label_3 = tk.Label(self, text="Position:")
        label_3.pack()

        self.entry3 = tk.Entry(self, width=20)
        self.entry3.pack()
        # button that takes the user entries above, uses them to create a new instance of a staffmember
        # then adds that instance to the staff list
        # the entry fields are then deleted so more entries can be made
        button1 = tk.Button(self, text="ADD!!", width='15', height='2',
                            command=lambda: self.combine_funcs(self.getStaffEntry(), self.entry1.delete(0, END),
                                                          self.entry2.delete(0, END), self.entry3.delete(0, END)))
        button1.pack()
        # button that takes the user back to the staff main menu
        button2 = tk.Button(self, text="Back to Staff Menu", width='15', height='2',
                            command=lambda: controller.show_frame(StaffMenu))
        button2.pack()
    # function that takes the user entries above and creates a new instance of staffMember
    # the function then appends the stafflist with the new instances
    # then prints out that the new staff member was added and prints the current amount of staff
    def getStaffEntry(self):
        first = self.entry1.get()
        last = self.entry2.get()
        position = self.entry3.get()
        newStaff = StaffMember(first, last, position)
        stafflist.append(newStaff)
        print("Staff Member has been added!")
        print("There are now %d staff members!" % len(stafflist))
    # function that allows a button to use more than one command
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func


# creating the removestaff frame
class removeStaff(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select Staff member and click 'Remove'")
        label.pack(pady=10, padx=10)
        # creating the labels and entry fields for the user to input the information of the staff
        # member they would like to remove form the staff list
        label_1 = tk.Label(self, text="First Name:")
        label_1.pack()

        self.entry1 = tk.Entry(self, width=20)
        self.entry1.pack()

        label_2 = tk.Label(self, text="Last Name:")
        label_2.pack()

        self.entry2 = tk.Entry(self, width=20)
        self.entry2.pack()

        label_3 = tk.Label(self, text="Position:")
        label_3.pack()

        self.entry3 = tk.Entry(self, width=20)
        self.entry3.pack()
        # remove button that uses the getstaffentry function which takes the users entries, creates
        # a new instance of a staff member, then removes the staff member in the current staff list that matches those
        # exact parameters
        # the entry fields are then deleted so more entries can be made
        button1 = tk.Button(self, text="REMOVE!!", width='15', height='2',
                            command=lambda: self.combine_funcs(self.getStaffEntry(), self.entry1.delete(0, END),
                                                          self.entry2.delete(0, END), self.entry3.delete(0, END)))
        button1.pack()
        # button that takes the user back to the staff main menu
        button2 = tk.Button(self, text="Back to Staff Menu", width='15', height='2',
                            command=lambda: controller.show_frame(StaffMenu))
        button2.pack()
    # function that takes the user entries from above and creates a new instance of staff member
    # then removes that staff member from the list using the removeStaff function
    def getStaffEntry(self):
        first = self.entry1.get()
        last = self.entry2.get()
        position = self.entry3.get()
        newStaff = StaffMember(first, last, position)
        self.removeStaff(newStaff)
        print("Staff Member has been removed!")
        print("There are now %d staff members!" % (len(stafflist)))
    # function that allows a button to use more than one command
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func
    # remove staff function that loops the new staff instance created above and checks to see if the parameters
    # match, if they do it removes the existing staff member from the list
    # if all of the parameters don't match, then it prints that the staff member was not found
    def removeStaff(self, member):
        for existingMember in stafflist:
            foundmember = 0
            if ((member.first == existingMember.first) and
                    (member.last == existingMember.last) and
                    (member.position == existingMember.position)):
                foundmember = existingMember
                memberFound = True
                if memberFound:
                    index = stafflist.index(existingMember)
                    stafflist.pop(index)
                else:
                    pass
                break
            elif (stafflist.index(existingMember) == (len(stafflist) - 1)):
                print("Staff Member Not Found.")
            else:
                pass


# creates the show staff frame
class showStaff(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Current Staff List")
        label.pack(pady=10, padx=10)
        # button that prints the current staff list in the console (first name, last name, position)
        button1 = tk.Button(self, text='Print Staff list in console', width='25', height='2',
                            command=lambda: printStaff())
        button1.pack()
        # button that takes the user back to the staff main menu
        button2 = tk.Button(self, text="Back to Staff Menu", width='25', height='2',
                            command=lambda: controller.show_frame(StaffMenu))
        button2.pack()

# calling the menu/root frames
app = TeslaManagementSystem()
app.mainloop()