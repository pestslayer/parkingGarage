paid = []
# create parking garage class 
class ParkingGarage:
    # must have attributues of ticekts---list,  parkingSpaces.....list,  and currentTicket---- dict
    def __init__(self,ticket,parkingSpace,currentTicket = {'paid':False}):
        self.ticket = ticket
        self.parkingSpace = parkingSpace
        self.currentTicket = currentTicket
    # method take tickets. 
    def takeTickets(self):
    # shoukld decrease tickets by 1
    # should decrease parkingspots by 1 
        pay = input("Would you like to pay now? yes/no ")
        if pay.lower() == 'yes':
            self.payParking()
        elif pay.lower() == 'no':
            print("Please enter quit on the next screen")
        else: 
            print("Please type yes or no")

   
        for i in range(self.ticket):
            self.ticket = self.ticket - 1
            print(f'There are {self.ticket} tickets left')
            for j in range(self.parkingSpace):
                self.parkingSpace = self.parkingSpace - 1
                print(f'There are {self.parkingSpace} parking spaces left')  
                return j
            return i 

# method pay for parking 
    def payParking(self):
    # display an input that waits for a user to enter an amout store as var 
        try:
            msg = int(input("Please enter an amount to pay "))
            print("Your ticket has been paid you have 15 minutes of parking.")
        except:
            print("Please enter a number")
        for i in range(msg):
            paid.append(msg)
            break
# if payment var != 0 display the ticket has been paid and they have 15min to leave. 
# this should update the currentTicket dict key paid to true
# method for leave garage. 
    def leaveGarage(self):
        pay = paid[:]
        if not pay:
            print("You must make a payment")
            payment = input("Please enter an amount")
        else:
            print("Thank you, have a great day")
        for i in range(self.ticket):
            self.ticket = self.ticket +1
            print(f'There are {self.ticket} tickets left')
            for j in range(self.parkingSpace):
                self.parkingSpace = self.parkingSpace + 1
                print(f'There are {self.parkingSpace} parking spaces left')  
                return j
            return i 

garage = ParkingGarage(10,10,1)
# create a run methond outside of the class to run it 
def run():
    while True:
        x = input("\nWhat would you like to do? park, pay, leave, or quit? ")
        if x.lower() == 'park':
            garage.takeTickets()
            print("Here is your ticket")

        elif x.lower() == "pay":
            garage.payParking()

        elif x.lower() == 'leave':
            garage.leaveGarage()
            
        
        elif x.lower() == 'quit':
            print("Thank you!")
            break
        else: 
            print("Please check your spelling or try another command.")


run()
