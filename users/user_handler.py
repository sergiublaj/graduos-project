from django.contrib import messages
from django.shortcuts import render


class Handler:
    def __init__(self):
        pass

    def handle(self):
        pass


class UserHandler(Handler):
    def __init__(self):
        super(UserHandler, self).__init__()
        self.handlers = []

    def handle(self):
        for handler in self.handlers:
            handler.handle()

    def add_handler(self, handler):
        self.handlers.append(handler)


class UsernameHandler(Handler):
    def __init__(self, username, all_users, request):
        super(UsernameHandler, self).__init__()
        self.username = username
        self.all_users = all_users
        self.request = request

    def handle(self):
        if self.all_users.filter(username=self.username).exists():
            messages.error(self.request, 'Username already taken!')

            return render(self.request, 'users/register.html')


class EmailHandler(Handler):
    def __init__(self, email, all_users, request):
        super(EmailHandler, self).__init__()
        self.email = email
        self.all_users = all_users
        self.request = request

    def handle(self):
        if self.all_users.filter(email=self.email).exists():
            messages.error(self.request, 'Email already taken!')

            return render(self.request, 'users/register.html')


class PasswordHandler(Handler):
    def __init__(self, password, password2, all_users, request):
        super(PasswordHandler, self).__init__()
        self.password = password
        self.password2 = password2
        self.all_users = all_users
        self.request = request

    def handle(self):
        if self.password != self.password2:
            messages.error(self.request, 'Passwords do not match!')

            return render(self.request, 'users/register.html')

class BirthDayHandler(Handler):
    def __init__(self, age, request):
        super(BirthDayHandler, self).__init__()
        self.age = age
        self.request = request

    def handle(self):
        if age<18:
            user.delete()
            messages.error(request, 'You must be at least 18 years old!')
            return render(self.request, 'users/register.html')
