from django.contrib.auth.models import User
from django.shortcuts import render

from users.models import Person
from users.user_factory import UserFactory
from users.user_handler import UserHandler, UsernameHandler, EmailHandler, PasswordHandler, BirthDayHandler
from datetime import date
import datetime

class UserBuilder:
    def __init__(self, request):
        self.request = request



    def register_account(self):
        self.register_user()

        self.register_person()

        user_factory = UserFactory(self.request, self.request.POST['is_student'])

        user_factory.register_user()

    def register_user(self):
        first_name = self.request.POST['first_name'].capitalize()
        last_name = self.request.POST['last_name'].capitalize()
        username = self.request.POST['username']
        email = self.request.POST['email']
        password = self.request.POST['password']
        password2 = self.request.POST['password2']

        all_users = User.objects.all()

        user_handler = UserHandler()

        user_handler.add_handler(UsernameHandler(username, all_users, self.request))
        user_handler.add_handler(EmailHandler(email, all_users, self.request))
        user_handler.add_handler(PasswordHandler(password, password2, all_users, self.request))
        user_handler.handle()

        if user_handler.error != 0:
            return

        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email)
        user.set_password(password)
        user.save()

    def register_person(self):
        try:
            user = User.objects.get(username=self.request.POST['username'])
        except:
            return render(self.request, 'users/register.html')

        photo = self.request.FILES['photo']
        phone = self.request.POST['phone']
        country = self.request.POST['country']
        address = self.request.POST['address']
        birth_date = self.request.POST['birth_date']
        gender = self.request.POST['gender']

        birthdate = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        age = (datetime.datetime.now() - birthdate).days / 365

        user_handler = UserHandler()
        user_handler.add_handler(BirthDayHandler(user, age, self.request))
        user_handler.handle()

        person = Person.objects.create(user=user, photo=photo, phone=phone,
                                       country=country, address=address, birth_date=birth_date, gender=gender)
        person.save()
