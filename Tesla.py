# creating the class for the instance of a Tesla Car
class TeslaCar:
    # definining the parameters that make up a car in the inventory
    def __init__(self, colorp, yearp, modelp, mileagep):
        self.year = int(yearp)
        self.model = modelp
        self.color = colorp
        self.mileage = int(mileagep)
    # creating a function that displays the cars information, then returns the statement
    def displayCar(self):
        return('%s %d %s with %d miles' % (self.color, int(self.year), self.model, self.mileage))
# creating the class for the instance of a staff member
class StaffMember:
    # definine the parameters that make up a staff member
    def __init__(self, firstp, lastp, positionp):
        self.first = firstp
        self.last = lastp
        self.position = positionp
    # creaitng a function that displays the staff members information, then returns the statement
    def displayStaffMember(self):
        return "Employee: " + self.first + " " + self.last + "\t\tPosition: " + self.position
# creating the class for the instance of a tesla inventory
class TeslaInventory:
    # defining the parameters that make up a tesla inventory
    def __init__(self, cityp, statep):
        self.city = cityp
        self.state = statep
        self.carlist = []
    # fucntion that adds a new car instance to the carlist
    def addCar(self, newcarp):
        self.carlist.append(newcarp)
    # function that prints the total amount of cars in the inventory
    def printInventory(self):
        print('There are %d cars in the %s,%s inventory!' % (len(self.carlist), self.city, self.state))
    # function used to print the updated amount of cars in the inventory after one is added/removed
    def printUpdatedInventory(self):
        print('There is now %d car(s) in the %s, %s inventory!' % (len(self.carlist), self.city, self.state))
    # function that prints each one of the cars in the inventory in a list
    def printCars(self):
        carNum = 1
        for car in self.carlist:
            print(str(carNum) + ".) " + car.displayCar() + "\n")
            carNum += 1
    # function that checks the parameters of user entries and sees if they match an already existing
    # car in the inventory
    # if the user entries match with a car, the car is removed
    # if the user entries don't match, a statement is printed telling the user the car wasn't found
    def removeCar(self, teslaCar):
        carFound = False
        index = 0
        for car in self.carlist:
            if ((car.year == teslaCar.year) and
                    (car.model == teslaCar.model) and
                    (car.color == teslaCar.color) and
                    (car.mileage == teslaCar.mileage)):
                index = self.carlist.index(car)
                carFound = True
                break
            else: #Do nothing, cars do not match
                pass
        if carFound:
            self.carlist.pop(index)
        else:
            print("Specified car not found.")
            pass

