from enum import Enum #import enum
from datetime import date #import date

class VisitorType(Enum): #defines an enumeration for visitor type with two options
    INDIVIDUAL = "Group"
    GROUP = "Individual"

class PurchaseChoice(Enum):  #defines an enumeration for purchase choices of visitors with three options
    Exhibitions = "Exhibition"
    Tours = "Tour"
    SpecialEvent = "Special Event"

class EventPurpose(Enum): #defines an enumeration for event choices of visitors with three options
    Fundraising = "Fundraising"
    MusicalConcerts = "Musical Concerts"
    LightShows = "Light Shows"

class Location(Enum): #defines an enumeration for location with three options
    PermanentGalleries = "Permanent Galleries"
    ExhibitionHalls = "Exhibition Halls"
    OutdoorSpaces = "Outdoor Spaces"

class Person:  # create a parent class that the child class (visitor) would inherit attributes and functions from.
    def __init__(self, firstName, lastName, age, id, email, phoneNumber): #define a constructor method to initialize the attributes of the Person class.
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__id = id
        self.__email = email
        self.__phoneNumber = phoneNumber

    def setFirstName(self, firstName): #setter method for updating the firstName
        self.__firstName = firstName

    def setLastName(self, lastName): #setter method for updating the lastName
        self.__lastName = lastName

    def setAge(self, age): #setter method for updating the birthDate
        self.__age = age

    def setID(self, id): #setter method for updating the id
        self.__id = id

    def setEmail(self, email): #setter method for updating the email
        self.__email = email

    def setPhoneNumber(self, phoneNumber): #setter method for updating the phoneNumber
        self.__phoneNumber = phoneNumber

    def getFirstName(self): #getter method for receiving the first name
        return self.__firstName

    def getLastName(self): #getter method for receiving the last name
        return self.__lastName

    def getAge(self): #getter method for receiving the birth date
        return self.__age

    def getID(self): #getter method for receiving the id
        return self.__id

    def getEmail(self): #getter method for receiving the email
        return self.__email

    def getPhoneNumber(self): #getter method for receiving the phone number
        return self.__phoneNumber

    def __str__(self): #define a function to display information about the person.
        return f"Name: {self.__firstName} {self.__lastName}, Age: {self.__age}, ID: {self.__id}, Email: {self.__email}, PhoneNumber: {self.__phoneNumber}"

class Visitor(Person): #inheritance with Person
    def __init__(self, firstName, lastName, age, id, email, phoneNumber, visitorType):
        Person.__init__(self, firstName, lastName, age, id, email, phoneNumber)
        self.__visitorType = visitorType
        self.__tickets = [] #list to store all tickets associated with one visitor

    def setVisitorType(self, visitorType): #setter method for updating the visitor type
        self.__visitorType = visitorType

    def getVisitorType(self): #getter method for receiving the visitor type
        return self.__visitorType

    def purchase_tickets(self, tickets): # unary association with tickets class
        self.__tickets.append(tickets) # add tickets to the list

    def get_tickets(self): #getter method for receiving the tickets associated with a visitor
        print(f"{self.getFirstName()} {self.getLastName()}'s tickets:")
        for ticket in self.__tickets:
            print(ticket)

    def __str__(self): # define a function to display information about the visitor, which is also an operator overriding
        return super().__str__() + f", VisitorType: {self.__visitorType.value}"

class TourGroup: # create a class for the tour group
    def __init__(self, guideName, selectedDate): #define a constructor method to initialize the attributes of the tour group class.
        self.__guideName = guideName
        self.__selectedDate = date.today()
        self.__visitors = [] #list to store all visitors associated with one tour group

    def setGuideName(self, guideName): # setter method for updating the guide name
        self.__guideName = guideName

    def setSelectedDate(self, selectedDate): # setter method for updating the selected date of the tour
        self.__selectedDate = selectedDate

    def getGuideName(self): # getter method for receiving the guide name
        return self.__guideName

    def getSelectedDatee(self): # getter method for receiving the selected date
        return self.__selectedDate

    def add_visitors(self, visitors_list): # aggregation with visitors class
        self.__visitors.append(visitors_list) # add visitors to the list

    def get_visitors(self): # getter method for receiving the visitors added to the tour group
        visitors_group = ""
        for visitor in self.__visitors:
            visitors_group += str(visitor)
        return visitors_group

    def __str__(self): # define a function to display information about the tour group
        return f"Guide Name: {self.__guideName}, Selected Date: {self.__selectedDate}\nGroup of visitors:\n{self.get_visitors()}"
class Ticket: # create a class for the ticket
    def __init__(self, ticketNum, purchaseChoice, date, time, location): #define a constructor method to initialize the attributes of the ticket class.
        self.__ticketNum = ticketNum
        self.__purchaseChoice = purchaseChoice
        self.__date = date.today()
        self.__time = time
        self.__location = location
        self.__price = 0 #Initialize ticket price

    def setTicketNum(self, ticketNum): # setter method for updating the ticket number displayed on the ticket
        self.__ticketNum = ticketNum

    def setPurchase_Choice(self, purchaseChoice): # setter method for updating the purchase choice displayed on the ticket
        self.__purchaseChoice = purchaseChoice

    def setDate(self, date): # setter method for updating the date displayed on the ticket
        self.__date = date

    def setTime(self, time): # setter method for updating the time displayed on the ticket
        self.__time = time

    def setLocation(self, location): # setter method for updating the location displayed on the ticket
        self.__location = location

    def getTicketNum(self): # getter method for receiving the ticket number
        return self.__ticketNum

    def getPurchase_Choice(self): # getter method for receiving the purchase choice
        return self.__purchaseChoice

    def getDate(self): # getter method for receiving the date
        return self.__date

    def getTime(self): # getter method for receiving the time
        return self.__time

    def getLocation(self): # getter method for receiving the location
        return self.__location

    def calculate_total_price(self, is_group=True): # define a function to calculate the total price of purchased tickets with flexible options for different visitor categories
        VAT_RATE = 0.05 # initiate the amount of VAT
        GROUP_DISCOUNT = 0.5 # initiate the amount of discount for groups

        try:
            visitor_age = int(input("Enter your age: ")) # asks the user to input their age
            is_teacher_or_student = input("Are you a teacher or student? (yes/no): ").lower() # asks the user to input yes if they are either a teacher or student and no if not

            if visitor_age < 18 or visitor_age > 60 or is_teacher_or_student == "yes":
                self.__price = 0 # if a user is less than 18 or greater than 60 or is a teacher or student, then their ticket price will be 0
            else:
                self.__price = 63 # else, the ticket price will be 63

            if is_group:
                is_group_input = input("Are you part of a group? (yes/no): ").lower() # asks the user to input yes if they are a group and no if not
                if is_group_input == "yes": # if the user inputs yes, it indicates that they are in a group
                    self.__price *= (1 - GROUP_DISCOUNT)  # groups receive a 50% discount on the ticket's original price

            self.__price *= (1 + VAT_RATE)  # # the system applies a 5% value-added tax (VAT) on the final ticket price

        except ValueError: # raise an exception if a user inputs something other than an integer for age
            return "Value Error: Please enter a valid age as an integer."

        except TypeError: # raise an exception if a user inputs something other than yes or no
            return "Type Error: Invalid value for is_teacher_or_student. Please provide a boolean value (yes or no)"

        else:
            print(f"Your bill for this ticket is: {self.__price} AED") # prints the total ticket price

    def getPrice(self): # getter method to receive the price of the ticket
        return self.__price

    def __add__(self, other): #operator overloading to add the price of tickets based on the number of purchase
        if isinstance(other, Ticket):
            return self.__price + other.__price
        else:
            return f"You have purchased one ticket only"

    def __str__(self): # define a function to display information about the tour group
        return f"Ticket Number: {self.__ticketNum}, Your purchase choice : {self.__purchaseChoice.value}, Date: {self.__date}, Time: {self.__time}, Location in Museum: {self.__location.value}, Price: {self.__price}"

class Artwork: # create a class for the artworks
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location): #define a constructor method to initialize the attributes of the artwork class.
        self.__title = title
        self.__artist = artist
        self.__date_of_creation = date_of_creation
        self.__historical_significance = historical_significance
        self.__exhibition_location = exhibition_location

    def setTitle(self, title): # setter method for updating the title
        self.__title = title

    def setArtist(self, artist): # setter method for updating the artist
        self.__artist = artist

    def setDateOfCreation(self, date_of_creation): # setter method for updating the date of creation
        self.__date_of_creation = date_of_creation

    def setHistoricalSignificance(self, historical_significance): # setter method for updating the historical significance
        self.__historical_significance = historical_significance

    def setExhibitionLocation(self, exhibition_location): # setter method for updating the exhibition location
        self.__exhibition_location = exhibition_location

    def getTitle(self): # getter method for receiving the title
        return self.__title

    def getArtist(self): # getter method for receiving the artist
        return self.__artist

    def getDateOfCreation(self): # getter method for receiving the date of creation
        return self.__date_of_creation

    def getHistoricalSignificance(self): # getter method for receiving the historical significance
        return self.__historical_significance

    def getExhibitionLocation(self): # getter method for receiving the exhibition location
        return self.__exhibition_location

    def __str__(self): # define a function to display information about the tickets
        return f"Title: {self.__title}, Artist: {self.__artist}, Date of Creation: {self.__date_of_creation}, Historical Significance: {self.__historical_significance}, Exhibition Location: {self.__exhibition_location.value}"

class Exhibition: # create a class for the exhibition
    def __init__(self, name, date, location, duration): # define a constructor method to initialize the attributes of the artwork class
        self.__name = name
        self.__date = date.today()
        self.__location = location
        self.__duration = duration
        self.__artworks = [] # list to store artworks associated with an exhibition
        self.__tickets = [] # list to store tickets associated with an exhibition

    def setName(self, name): # setter method for updating the name
        self.__name = name

    def setDate(self, date): # setter method for updating the date
        self.__date = date

    def setLocation(self, location): # setter method for updating the location
        self.__location = location

    def getName(self): # getter method for receiving the name
        return self.__name

    def getDate(self): # getter method for receiving the date
        return self.__date

    def getLocation(self): # getter method for receiving the location
        return self.__location

    def add_artworks(self, artworks_list): #aggregation with artworks class
        self.__artworks.append(artworks_list)

    def get_artworks(self): # getter method for receiving the artworks that an exhibition has
        total_art=""
        for artwork in self.__artworks:
            total_art+=str(artwork)
        return total_art

    def add_tickets(self, ticketNum, purchaseChoice, date, time, location): #composition with ticket class
        self.__tickets.append(Ticket(ticketNum, purchaseChoice, date, time, location))

    def get_tickets(self): # getter method for receiving the tickets purchased for specific exhibitions
        total_tickets = ""
        for ticket in self.__tickets:
            total_tickets+=str(ticket)
        return total_tickets

    def __str__(self): # define a function to display information about the exhibitions
        return f"Name: {self.__name}, Date: {self.__date}, Location: {self.__location.value}, Duration: {self.__duration} \nArtworks:\n{self.get_artworks()} \nTickets:\n{self.get_tickets()}"

class SpecialEvent: # create a class for the special events
    def __init__(self, eventName, eventPurpose, location, duration): #define a constructor method to initialize the attributes of the special events class
        self.__eventName = eventName
        self.__eventPurpose = eventPurpose
        self.__location = location
        self.__duration = duration
        self.__tickets = [] # list to store tickets associated with a special event

    def setEventName(self, eventName): # setter method for updating the event name
        self.__eventName = eventName

    def setEventPurpose(self, eventPurpose): # setter method for updating the event purpose
        self.__eventPurpose = eventPurpose

    def setLocation(self, location): # setter method for updating the location
        self.__location = location

    def setDuration(self, duration): # setter method for updating the duration
        self.__duration = duration

    def getEventName(self): # getter method for receiving the event name
        return self.__eventName

    def getEventPurpose(self): # getter method for receiving the event purpose
        return self.__eventPurpose

    def getLocation(self):  # getter method for receiving the location
        return self.__location

    def getDuration(self):  # getter method for receiving the duration
        return self.__duration

    def add_tickets(self, ticketNum, purchaseChoice, date, time, location): # composition with tickets class
        self.__tickets.append(Ticket(ticketNum, purchaseChoice, date, time, location))

    def get_tickets(self): # getter method for receiving the tickets purchased for specific special events
        total_tickets = ""
        for ticket in self.__tickets:
            total_tickets+=str(ticket)
        return total_tickets

    def __str__(self):  # define a function to display information about the special events
        return f"Event Name: {self.__eventName}, Purpose: {self.__eventPurpose.value}, Location: {self.__location.value}, Duration: {self.__duration} \nTickets:\n{self.get_tickets()}"

class Museum: # create a class for the museum
    def __init__(self, museumName): #define a constructor method to initialize the attributes of the museum class.
        self.__museumName = museumName
        self.__exhibitions = [] # list to store exhibitions associated with the museum
        self.__specialEvents = [] # list to store special events associated with the museum

    def setMuseumName(self, museumName): # setter method for updating the museum name
        self.__museumName = museumName

    def getMuseumName(self): # getter method for receiving the museum name
        return self.__museumName

    def add_exhibitions(self, name, date, location, duration): # composition with exhibition class
        self.__exhibitions.append(Exhibition(name, date, location, duration))

    def add_specialEvents(self, eventName, eventPurpose, location, duration): # composition with special event class
        self.__specialEvents.append(SpecialEvent(eventName, eventPurpose, location, duration))

    def get_exhibitions(self):  # getter method for receiving the exhibitions associated specifically to the louvre museum
        exhibitions_info = ""
        for exhibition in self.__exhibitions:
            exhibitions_info += str(exhibition)  #ensuring that the artworks and tickets associated with an exhibition is also printed within the composition relationship
        return exhibitions_info

    def get_specialEvents(self): # getter method for receiving the special events associated specifically to the louvre museum
        special_events_info = ""
        for specialEvent in self.__specialEvents:
            special_events_info += str(specialEvent)  #ensuring that the tckets associated with a special event is also printed within the composition relationship
        return special_events_info

    def __str__(self):  # define a function to display information about the museum
        return f"Museum Name: {self.__museumName}\nExhibitions:\n{self.get_exhibitions()}\nSpecial Events:\n{self.get_specialEvents()}"