# Jessica Uriostegui
# June 19, 2024

# Lesson 1: Assignments | Dictionaries
# Task 1: Restaurant Menu Update

restaurant_menu = {
    
    "Starters" : { 
    "Soup": 5.99,
    "Bruschetta": 6.50 
    },
    "Main Course" : {
    "Steak": 15.99, 
    "Salmon": 13.99
    },
    "Desserts" : {
    "Cake": 4.99, 
    "Ice Cream": 3.99
    }
}

print(restaurant_menu)

restaurant_menu ["Beverages"] = {"Bobba" : 7.99 , "Shake": 5.99}
print(restaurant_menu)
restaurant_menu ["Main Course"] = {"Steak": 17.99, "Salmon": 13.99}
print(restaurant_menu)
restaurant_menu ["Starters"] = {"Soup": 5.99}
print(restaurant_menu)   


# Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open" },
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed" }
}
def add_ticket(service_tickets):
    print(f"Here are the current tickets :  \n" )
    for ticket, details in service_tickets.items():
        print(f"Ticket: {ticket} \n")
    new_ticket = input("What ticket # would you like to add:  \n" ).capitalize()
    customer = input ("What is the customers name: \n").capitalize()
    issue = input("What is the issue:  \n")
    status = input("Current status: (Open/Closed)  \n").capitalize()
    service_tickets[new_ticket] = {"Customer" : customer, "Issue": issue, "Status" : status}
    print(f"New ticket: {new_ticket} added successfully.")

def update_tickets(service_tickets):
    ticket_to_update = input("Enter the ticket # you want to update:\n").capitalize()
    if ticket_to_update in service_tickets:
        new_status = input("Enter the new status (Open/Closed):\n").capitalize()
        service_tickets[ticket_to_update]["Status"] = new_status
        print("Ticket status updated successfully.")
    else:
        print("Ticket not found.")

def see_tickets(service_tickets):
    for ticket, details in service_tickets.items():
        print(f"Ticket: {ticket}")
        for key, value in details.items():
            print(f" - {key}: {value}") 

def main(service_tickets):
    a =""" 
    Hello, what would you like to do:
    """
    b = """ 
    1. Add a new customer.
    2. Update a ticket. (Open/Close)
    3. Display all tickets.
    4. Exit
    """
    print(a)
    print(b)
    print("*************************************************** \n")

    while True:
        user = input("What would you like to do?  \n")
       
        if user == "1":
            add_ticket(service_tickets)
            print(b)   
        elif user == "2":
            update_tickets(service_tickets)
            print(b)
        elif user == "3":
            see_tickets(service_tickets)
            print(b)
        elif user == "4":
            print("Good job have a great day, good bye!")
            break
        else:
          print("Invalid choice. Please enter a number between 1 and 3.")
    
main(service_tickets)
