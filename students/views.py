from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from .models import Dish
from .forms import DishForm
def add_person(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons_list')
    else:
        form = StudentForm()
    return render(request, 'add_person.html', {'form': form})

def persons_list(request):
    students = Student.objects.all()
    return render(request, 'persons_list.html', {'students': students})

def give_points(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        points = int(request.POST['points'])
        student.points += points
        student.save()
        return redirect('view_points', student_id=student.id)
    return render(request, 'give_points.html', {'student': student})

def view_points(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'view_points.html', {'student': student})




def view_schedule(request, faculty):
    template_mapping = {
        'sest': 'sest_schedule.html',
        'ecol': 'ecol_schedule.html',
        'ehi': 'ehi_schedule.html',
        'dht': 'dht_schedule.html'
    }

    schedule_info = {
        'title': f'{faculty.upper()} Schedule',
        'subjects': [
            {'name': 'Math', 'time': '8:00 AM - 9:20 AM'},
            {'name': 'ML', 'time': '9:30 AM - 10:50 AM'},
            {'name': 'AVD', 'time': '11:40 AM - 1:00 PM'},
            {'name': 'Software Development', 'time': '1:10 PM - 2:30 PM'},
        ]  # Default schedule, you can replace it with actual schedule if available

    }

    template_name = template_mapping.get(faculty)
    if template_name:
        return render(request, template_name, schedule_info)
    else:
        return render(request, 'faculty_not_found.html', {'faculty': faculty})



def dish_list(request):
    dishes = Dish.objects.all()  # Retrieve all dishes from the database
    return render(request, 'dish_list.html', {'dishes': dishes})

def add_dishes(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')  # Redirect to the dish_list page
    else:
        form = DishForm()
    return render(request, 'add_dishes.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404

def persons_list(request):
    students = Student.objects.all()  # Your logic to get students
    return render(request, 'persons_list.html', {'students': students})

def remove_person(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('persons_list')


from .models import Order
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list') 
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


def view_orders(request):
    orders = Order.objects.all()  # Query all orders from the database
    return render(request, 'view_orders.html', {'orders': orders})