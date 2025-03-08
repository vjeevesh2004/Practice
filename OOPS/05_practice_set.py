''' write a class Train which has methods to book a ticket, 
get Status(no. of seats) and get fare infromation 
of trains running under Indian Railways ''' 

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getstatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats available in this train is {self.seats}")
    
    def fareinfo(self):
        print(f"the price of the ticket is : {self.fare}")

    def booktickets(self):
        if (self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Try in tatkal")
           
    def cancelTicket(self):
        pass


intercity = Train("Intercity Express", 90, 2)
intercity.getstatus()
intercity.booktickets()
intercity.getstatus() 
intercity.booktickets()
intercity.getstatus()
intercity.booktickets()
intercity.getstatus()