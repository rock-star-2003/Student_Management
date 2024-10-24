from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout   
from datetime import date
from django.contrib import messages
from .models import Student,Batch,Department,StudentProfileUpdate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import JsonResponse

# import user




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request,'authenticate/login.html',)

        

def index(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            student = request.user.student
            if student.date_of_birth:
                birth_date = student.date_of_birth
                age = (date.today() - birth_date).days // 365
            else:
                age = "Unknown"  # Default value if date_of_birth is None
        except Student.DoesNotExist:
            student = None
            age = "Unknown"  # Default value if student doesn't exist
    else:
        # If the user is not authenticated, redirect to the login page or handle accordingly
        return redirect('login')  # Replace 'login' with your actual login URL pattern

    # Get the count of all Departments
    department_count = Department.objects.count()
    student_count = Student.objects.count()
    # Get the count of all students who have paid their fees
    students_paid_fees = Student.objects.filter(fees='paid').count()
    students_Unpaid_fees = Student.objects.filter(fees='Unpaid').count()
    Attendance = Student.objects.filter(attendence='Present').count()
    absence = student_count - Attendance
    bach_count = Batch.objects.count()
    All_students = Student.objects.all()
    # Create the context dictionary
    context = {
        'age': age,
        'student': student,
        'department_count': department_count,
        'student_count': student_count,
        'students_paid_fees': students_paid_fees,
        'students_Unpaid_fees': students_Unpaid_fees,
        'absence': absence,
        'present':Attendance,
        'bach_count':bach_count,
        'All_students':All_students,
    }

    # Render the template with the context
    return render(request, 'index.html', context)


def fee_payment(request, id):
    user = get_object_or_404(User, id=id)  # Fetch the user

    if request.method == 'POST':
        if user.student.fees == 'Unpaid':
            user.student.fees = 'paid'
            user.student.save()
            messages.success(request, 'Fees paid successfully')  # Save the student instance
            return redirect('index')  # Redirect to index after payment
        
    return render(request, 'fee_payment.html', {'user': user}) 

    

def leave_letter(request,id):
    return render(request, 'leave_letter.html')


def edit_profile(request,id):
    try:
        student = request.user.student  # Get the student object for the logged-in user
    except Student.DoesNotExist:
        student = None

    if request.method == 'POST':
        form = StudentProfileUpdate(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('index')  # Redirect to the profile page after saving
    else:
        form = StudentProfileUpdate(instance=student)

    return render(request, 'edit_profile.html', {'form': form, 'student': student})

def view_student(request,id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'studentprofile.html', {'student': student})


def update_attendance(request):
    # Get all departments and batches
    all_department = Department.objects.all()
    all_batch = Batch.objects.all()
    
    # Default to showing all students
    all_students = Student.objects.all()
    
    if request.method == 'POST':
        department_id = request.POST.get('department')
        batch_id = request.POST.get('batch')
        
        if department_id and batch_id:
            # Filter students based on selected department and batch
            all_students = Student.objects.filter(
                department_id=department_id, 
                bach_id=batch_id
            )
    
    context = { 
        'All_students': all_students,
        'All_department': all_department,
        'All_batch': all_batch
    }

    return render(request, 'update_attendance.html', context)

def update_attendance_status(request):
    student_id = request.POST.get('student_id')
    new_status = request.POST.get('status')
    
    try:
        student = Student.objects.get(id=student_id)
        student.attendence = new_status
        student.save()
        response = {
            'status': 'success',
            'new_status': student.attendence
        }
    except Student.DoesNotExist:
        response = {
            'status': 'error',
            'message': 'Student not found'
        }
    
    return JsonResponse(response)