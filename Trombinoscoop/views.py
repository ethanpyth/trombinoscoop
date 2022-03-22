from datetime import datetime, date
from django.shortcuts import render, redirect
from Trombinoscoop.forms import LoginForm, StudentProfileForm, EmployeeProfileForm, AddFriendForm
from Trombinoscoop.models import Person, Student, Employee, Message


def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Student.objects.filter(id=logged_user_id)) == 1:
            return Student.objects.get(id=logged_user_id)
        elif len(Employee.objects.filter(id=logged_user_id)):
            return Employee.objects.get(id=logged_user_id)
        else:
            return None
    else:
        return None


def welcome(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if 'newMessage' in request.GET and request.GET['newMessage'] != '':
            new_message = Message(author=logged_user, content=request.GET['newMessage'], publication_date=date.today())
            new_message.save()
        friend_messages = Message.objects.filter(author__friends=logged_user).order_by('-publication_date')
        return render(request, 'welcome.html', {'logged_user': logged_user, 'friendMessages': friend_messages})
    else:
        return redirect('/login/')


def login(request):
    if len(request.POST):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Person.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        student_form = StudentProfileForm(prefix="st")
        employee_form = EmployeeProfileForm(prefix="em")
        if request.GET['profileType'] == 'student':
            student_form = StudentProfileForm(request.GET, prefix="st")
            if student_form.is_valid():
                student_form.save()
                return redirect('/login/')
        elif request.GET['profileType'] == 'employee':
            employee_form = EmployeeProfileForm(request.GET, prefix="em")
            if employee_form.is_valid():
                employee_form.save()
                return redirect('/login/')
        return render(request, 'user_profile.html', {'studentForm': student_form, 'employeeForm': employee_form})
    else:
        student_form = StudentProfileForm(prefix="st")
        employee_form = EmployeeProfileForm(prefix="em")
        return render(request, 'user_profile.html', {'studentForm': student_form, 'employeeForm': employee_form})


def add_friend(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if len(request.GET) > 0:
            form = AddFriendForm(request.GET)
            if form.is_valid():
                new_friend_email = form.cleaned_data['email']
                new_friend = Person.objects.get(email=new_friend_email)
                logged_user.friends.add(new_friend)
                logged_user.save()
                return redirect('/')
            else:
                return render(request, 'add_friend.html', {'form': form})
        else:
            form = AddFriendForm()
            return render(request, 'add_friend.html', {'form': form})
    else:
        return redirect('/login/')


def show_profile(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if 'userToShow' in request.GET and request.GET['userToShow'] != '':
            user_to_show_id = int(request.GET['userToShow'])
            results = Person.objects.filter(id=user_to_show_id)
            if len(results) == 1:
                if Student.objects.filter(id=user_to_show_id):
                    user_to_show = Student.objects.get(id=user_to_show_id)
                else:
                    user_to_show = Employee.objects.get(id=user_to_show_id)
                return render(request, 'show_profile.html', {'user_to_show': user_to_show})
            else:
                return render(request, 'show_profile.html', {'user_to_show': logged_user})
        else:
            return render(request, 'show_profile.html', {'user_to_show': logged_user})
    else:
        return redirect('/login')
