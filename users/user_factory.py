from django.contrib.auth.models import User
from django.shortcuts import render

from users.models import Person, Professor, Student
from users.user_handler import UserHandler, IdentificationNoHandler


class UserFactory:
    def __init__(self, request, is_student):
        self.request = request
        self.is_student = is_student

    def register_user(self):
        if self.is_student == 'True':
            error, message = self.register_student()
            return (error,message)
        else:
            error, message = self.register_professor()
            return (error,message)

    def register_student(self):
        try:
            user=User.objects.get(username=self.request.POST['username'])
            person = Person.objects.get(user=User.objects.get(
                username=self.request.POST['username']))
        except:
            print("Register student")
            return render(self.request, 'users/register.html')

        identification_no = self.request.POST['identification_no']
        university = self.request.POST['university']
        faculty = self.request.POST['faculty']
        study_level = self.request.POST['study_level']
        study_year = self.request.POST['study_year']

        all_students = Student.objects.all()

        user_handler = UserHandler()
        user_handler.add_handler(IdentificationNoHandler(identification_no,all_students,user,person))
        user_handler.handle()
        for handler in user_handler.handlers:
            if handler.error == -5:
                message = 'There is already a student with this identification number!'
                return (handler.error, message)

        student = Student.objects.create(person=person, identification_no=identification_no,
                                         university=university, faculty=faculty, study_level=study_level,
                                         study_year=study_year)
        student.save()
        return (0,"Student creation succesfull")

    def register_professor(self):
        try:
            person = Person.objects.get(user=User.objects.get(
                username=self.request.POST['username']))
        except:
            print("Except professor")
            return render(self.request, 'users/register.html')

        department = self.request.POST['department']
        rank = self.request.POST['rank']
        office_address = self.request.POST['office_address']
        website = self.request.POST['website']

        professor = Professor.objects.create(
            person=person, department=department, rank=rank, office_address=office_address, website=website)
        professor.save()

        return (0,"Professor creation succesfull")
