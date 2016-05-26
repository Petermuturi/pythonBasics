seatNumber = [12, 5, 6, 8, 2, 19, 17, 13]

print("Here are the seats available")

for bookSeat in range(1, 20):
    if bookSeat in seatNumber:
        continue
    print(bookSeat)
# If you are booking a seat for an event...skips the booked seats and shows available ones
