from django.contrib import admin
from users.models import Person, Student, Professor

class PersonAdmin(admin.ModelAdmin):
   list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'country', 'address', 'birth_date', 'sex', 'registration_date', 'photo')
   list_display_links = ('id', 'username')
   search_fields = ('username', 'email')
   list_per_page = 25
   
   def username(self, obj):
    return obj.user.username

   def first_name(self, obj):
    return obj.user.first_name

   def last_name(self, obj):
    return obj.user.last_name

   def email(self, obj):
    return  obj.user.email

admin.site.register(Person, PersonAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'identification_no', 'university', 'faculty', 'study_level', 'study_year','final_grade', 'accumulated_credits', 'outstanding_credits')
    list_display_links = ('id', 'username' , 'email')
    search_fields = ('username', 'email')
    list_per_page = 25

    def username(self, obj):
        return obj.person.user.username

    def first_name(self, obj):
        return obj.person.user.first_name

    def email(self, obj):
        return obj.person.user.email

    def last_name(self,obj):
        return obj.person.user.last_name

admin.site.register(Student, StudentAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'department', 'rank', 'office_address', 'website')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')
    list_per_page = 25

    def username(self, obj):
        return obj.person.user.username

    def first_name(self, obj):
        return obj.person.user.first_name

    def email(self, obj):
        return obj.person.user.email

    def last_name(self, obj):
        return obj.person.user.last_name

admin.site.register(Professor, ProfessorAdmin)