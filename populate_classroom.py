import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()



#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import get_user_model
from users.models import classroom



if __name__ == '__main__':
    """
    with open('classroom.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            classroom.objects.create(roomtype=row[0],capacity=row[1],location=row[2],room_number=row[3],campus=row[4])
            print(row)
    """
    table=classroom.objects.all()
    print(table[0]._meta.fields)
    for row in table:
        print("-"*30)
        print(row.roomtype)
        print(row.capacity)
        print(row.location)
        print(row.room_number)
        print(row.campus)
        print("-"*30)
