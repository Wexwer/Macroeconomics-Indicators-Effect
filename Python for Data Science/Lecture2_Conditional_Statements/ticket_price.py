STUDENT_TICKET_PRICE = 1.00
REGULAR_TICKET_PRICE = 1.60

ticket_type = input()



if ticket_type == "student":
    print(f"${STUDENT_TICKET_PRICE:.2f}")
elif ticket_type == "regular":
    print(f"${REGULAR_TICKET_PRICE:.2f}")
else:
    print(f"Invalid ticket type!")