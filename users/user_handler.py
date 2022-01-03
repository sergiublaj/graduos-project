from django.contrib import messages
from django.shortcuts import render, redirect


class Handler:
    def __init__(self):
        pass

    def handle(self):
        pass


class UserHandler(Handler):
    def __init__(self):
        super(UserHandler, self).__init__()
        self.handlers = []
        self.error = 0

    def handle(self):
        for handler in self.handlers:
            handler.handle()

    def add_handler(self, handler):
        self.handlers.append(handler)


class UsernameHandler(Handler):
    def __init__(self, username, all_users):
        super(UsernameHandler, self).__init__()
        self.username = username
        self.all_users = all_users
        self.error=0

    def handle(self):
        if self.all_users.filter(username=self.username).exists():
            self.error = -1



class EmailHandler(Handler):
    def __init__(self, email, all_users):
        super(EmailHandler, self).__init__()
        self.email = email
        self.all_users = all_users
        self.error = 0

    def handle(self):
        if self.all_users.filter(email=self.email).exists():
            self.error = -2


class PasswordHandler(Handler):
    def __init__(self, password, password2):
        super(PasswordHandler, self).__init__()
        self.password = password
        self.password2 = password2
        self.error = 0

    def handle(self):
        if self.password != self.password2:
            self.error=-3


class BirthDayHandler(Handler):
    def __init__(self, age):
        super(BirthDayHandler, self).__init__()
        self.age = age
        self.error=0

    def handle(self):
        if self.age<18:
            self.error=-4


