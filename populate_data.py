import os
import django
import random
from datetime import timedelta
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings') 
django.setup()

from restaurant.models import Menu, Booking  

def populate():
    menu_titles = ['Pasta', 'Burger', 'Pizza', 'Salad', 'Soup', 'Sushi']
    for i in range(10):
        title = random.choice(menu_titles) + f" {i+1}"
        price = round(random.uniform(5.00, 20.00), 2)
        inventory = random.randint(5, 50)
        menu_item = Menu(title=title, price=price, inventory=inventory)
        menu_item.save()
        print(f"Created Menu: {menu_item}")

    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    for i in range(10):
        name = random.choice(first_names)
        no_of_guests = random.randint(1, 8)
        # random booking_date within next 30 days, random time
        booking_date = timezone.now() + timedelta(days=random.randint(0, 30), hours=random.randint(0,23), minutes=random.randint(0,59))
        booking = Booking(name=name, no_of_guests=no_of_guests, booking_date=booking_date)
        booking.save()
        print(f"Created Booking: {booking}")

if __name__ == '__main__':
    populate()
