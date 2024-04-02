from Classes import * # importing the file with all classes

# creating Try-except blocks for getting user input for each class

# For class Visitor
try:
    # Getting user input for Visitor 1
    print("Visitor 1:")
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    age = int(input("Enter age: "))
    id = int(input("Enter ID number: "))
    email = str(input("Enter email: "))
    phone_number = int(input("Enter phone number: "))
    visitor_type = VisitorType(input("Enter visitor's type (Individual/Group): "))

    visitor1 = Visitor(first_name, last_name, age, id, email, phone_number, visitor_type) # object for visitor

    # Getting user input for Visitor 2
    print("\nVisitor 2:")
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    age = int(input("Enter age: "))
    id = int(input("Enter ID number: "))
    email = str(input("Enter email: "))
    phone_number = int(input("Enter phone number: "))
    visitor_type = VisitorType(input("Enter visitor's type (Individual/Group): "))

    visitor2 = Visitor(first_name, last_name, age, id, email, phone_number, visitor_type) # object for visitor

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class TourGroup
try:
    # Getting user input for Tour group
    print("\nTour Group:")
    guideName = str(input("Enter the guide name: "))
    selectedDate = date.today()

    tour_group = TourGroup(guideName, selectedDate) # object for tour group

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class Ticket
try:
    # Getting user input for tickets
    print("\nPurchasing First Ticket:")
    ticketNum = int(input("Enter ticket number: "))
    purchaseChoice = PurchaseChoice(input("Enter your purchase choice (Exhibition/Tour/Special Event): "))
    date = date.today()
    time = float(input("Enter time: "))
    location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))

    ticket1 = Ticket(ticketNum, purchaseChoice, date, time, location) # object for ticket
    price = ticket1.calculate_total_price() # gets the calculated price in the ticket class based on certain conditions that the user will input

    print("\nPurchasing Second Ticket:")
    ticketNum = int(input("Enter ticket number: "))
    purchaseChoice = PurchaseChoice(input("Enter your purchase choice (Exhibition/Tour/Special Event): "))
    date = date.today()
    time = float(input("Enter time: "))
    location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))

    ticket2 = Ticket(ticketNum, purchaseChoice, date, time, location) # object for ticket
    price = ticket2.calculate_total_price() # gets the calculated price in the ticket class based on certain conditions that the user will input

    print("\nPurchasing Third Ticket:")
    ticketNum = int(input("Enter ticket number: "))
    purchaseChoice = PurchaseChoice(input("Enter your purchase choice (Exhibition/Tour/Special Event): "))
    date = date.today()
    time = float(input("Enter time: "))
    location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))

    ticket3 = Ticket(ticketNum, purchaseChoice, date, time, location) # object for ticket
    price = ticket3.calculate_total_price() # gets the calculated price in the ticket class based on certain conditions that the user will input

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class Artwork
try:
    # Getting user input for artworks
    print("\nAdding Artworks to the Exhibition:")
    title = str(input("Enter artwork title: "))
    artist = str(input("Enter artist name: "))
    date_of_creation = int(input("Enter date of creation: "))
    historical_significance = str(input("Enter historical significance: "))
    exhibition_location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))

    artwork1 = Artwork(title, artist, date_of_creation, historical_significance, exhibition_location) # object for artwork

    print("\nAdding Artworks to the Exhibition:")
    title = str(input("Enter artwork title: "))
    artist = str(input("Enter artist name: "))
    date_of_creation = int(input("Enter date of creation: "))
    historical_significance = str(input("Enter historical significance: "))
    exhibition_location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): ")) # object for artwork

    artwork2 = Artwork(title, artist, date_of_creation, historical_significance, exhibition_location) # object for artwork

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class Exhibition
try:
    # Getting input for exhibitions
    print("\nAdding Exhibitions to the Museum:")
    name = str(input("Enter exhibition name: "))
    date = date.today()
    location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))
    duration = "2 months"

    exhibition1 = Exhibition(name, date, location, duration) # object for exhibition

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class SpecialEvent
try:
    # Getting input for special events
    print("\nAdding Special Events to the Museum: ")
    eventName = str(input("Enter event name: "))
    eventPurpose = EventPurpose(input("Enter the event purpose(Fundraising, Musical Concerts, Light Shows: "))
    location = Location(input("Enter the location(Exhibition Halls/Permanent Galleries/Outdoor Spaces): "))
    duration = "1 month"

    event1 = SpecialEvent(eventName, eventPurpose, location, duration) # object for special event

except ValueError as e: # raise an exception if an error occurs
    print("ValueError:", e)

# For class Museum
try:
    # Getting user input for Museum
    print("\nMuseum Details:")
    museumName = str(input("Enter the museum name: "))

    museum1 = Museum(museumName)

except Exception as e: # raise an exception if an error occurs
    print("An error occurred while inputting the museum name:", e)

else:
    # display visitor information
    print("\nRegistered Museum Visitors: ")
    print(visitor1)
    print(visitor2)

    # display artwork information
    print("\nArtworks Information:")
    print(artwork1)
    print(artwork2)

# Testing the relationship implemented between the classes (unary association, aggregation, composition)

# Unary association - Adding tickets to visitors
visitor1.purchase_tickets(ticket1)
visitor1.purchase_tickets(ticket3)
visitor2.purchase_tickets(ticket2)
visitor2.purchase_tickets(ticket2)

print("\nPurchased tickets of each Visitor: ")
visitor1.get_tickets()
visitor2.get_tickets()

print("\nReceipt of each visitor:")  # Displaying total bill for each visitor as their receipt
total_bill1 = ticket1 + ticket3
total_bill2 = ticket2 + ticket2
print(f"Total bill for visitor 1 tickets: {total_bill1} AED")
print(f"Total bill for visitor 2 tickets: {total_bill2} AED")



# Aggregation - Adding visitors to the tour group
tour_group.add_visitors(visitor1)
tour_group.add_visitors(visitor2)

# display visitors associated with the tour group
print("\nTour Group:")
print(tour_group)

print("\n")
del tour_group # test if visitors will still exist if the tour group gets destroyed (aggregation)
print(visitor1)
print(visitor2)



# Aggregation - Adding artworks to exhibitions
exhibition1.add_artworks(artwork1)
exhibition1.add_artworks(artwork2)

# Composition - Adding tickets to exhibitions
exhibition1.add_tickets(4, PurchaseChoice.Exhibitions, date.today(), 12.00, Location.ExhibitionHalls)
exhibition1.add_tickets(5, PurchaseChoice.Tours, date.today(), 3.00, Location.PermanentGalleries)

# display both artworks and tickets associated with the exhibition
print("\nExhibitions Information:")
print(exhibition1)




# Composition - Adding tickets to special events
event1.add_tickets(6, PurchaseChoice.Tours, date.today(), 12.00, Location.OutdoorSpaces)
event1.add_tickets(7, PurchaseChoice.SpecialEvent, date.today(), 1.00, Location.PermanentGalleries)

# display tickets associated with the special event
print("\nSpecial Events Information:")
print(event1)



# Composition - Adding exhibitions and special events to the museum
museum1.add_exhibitions("Travelling through Fables", date.today(), Location.ExhibitionHalls, "2 months")
museum1.add_specialEvents("Concert", EventPurpose.MusicalConcerts, Location.OutdoorSpaces, "2 hours")
print("\nMuseum Information:")
print(museum1)