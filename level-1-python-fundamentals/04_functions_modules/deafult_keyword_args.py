
def book_hotel(name, rooms=1, breakfast=True):
    print(f"Hotel booked for {name}")
    print("Rooms:", rooms)
    print("Breakfast included:", breakfast)

book_hotel("Kannan")
book_hotel("Nandha", rooms=2, breakfast= False)
