from django.contrib.auth.models import User

from users.models import Person, Professor, Student


class UserFactory:
    def __init__(self, request, is_student):
        self.request = request
        self.is_student = is_student

    def register_user(self):
        if self.is_student == 'True':
            self.register_student()
        else:
            self.register_professor()

    def register_student(self):
        try:
            person = Person.objects.get(user=User.objects.get(
                username=self.request.POST['username']))
        except:
            return render(request, 'users/register.html')

        identification_no = self.request.POST['identification_no']
        university = self.request.POST['university']
        faculty = self.request.POST['faculty']
        study_level = self.request.POST['study_level']
        study_year = self.request.POST['study_year']

        student = Student.objects.create(person=person, identification_no=identification_no,
                                         university=university, faculty=faculty, study_level=study_level,
                                         study_year=study_year)
        student.save()

    def register_professor(self):
        try:
            person = Person.objects.get(user=User.objects.get(
                username=self.request.POST['username']))
        except:
            return render(request, 'users/register.html')

        department = self.request.POST['department']
        rank = self.request.POST['rank']
        office_address = self.request.POST['office_address']
        website = self.request.POST['website']

        professor = Professor.objects.create(
            person=person, department=department, rank=rank, office_address=office_address, website=website)
        professor.save()
