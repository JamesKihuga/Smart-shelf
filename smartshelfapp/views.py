from django.shortcuts import render,redirect
from smartshelfapp.models import Shelf, Contact, Customer
from smartshelfapp.forms import ShelfForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        mycontact = Contact(
        name = request.POST['name'],
        email = request.POST['email'],
        subject = request.POST['subject'],
        message = request.POST['message']
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
def teams(request):
    return render(request, 'teams.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')
def pricing(request):
    return render(request, 'pricing.html')
def blog(request):
    return render(request, 'blog.html')
def testimonials(request):
    return render(request,'testimonials.html')
def register(request):
    return render(request,'register.html')


def shelf(request):
    if request.method == "POST":
        myshelf = Shelf(
            number=request.POST['number'],
            location = request.POST['location'],
            date = request.POST['date'],
            due_date = request.POST['due_date'],
            weight = request.POST['weight'],
            price = request.POST['price']
        )
        myshelf.save()
        return redirect('/shelf')
    else:
        return render(request,'shelf.html')




def starter(request):
    return render(request,'starter-page.html')

def bookings(request):
    allbookings = Shelf.objects.all()
    return render(request, 'bookings.html', {'allbookings': allbookings})

def delete(request, id,):
    shelf=Shelf.objects.get(id=id)
    shelf.delete()
    return redirect('/bookings')

def update(request, id):
    update=Shelf.objects.get(id=id)
    return render(request, 'update.html', {'update':update})

def update(request, id):
    updatebookings=Shelf.objects.get(id=id)
    form =ShelfForm(request.POST, instance=updatebookings)
    if form.is_valid():
        form.save()
        return redirect('/bookings')
    else:
        return render(request, 'update.html')

def register(request):
    if request.method == "POST":
        mycustomer = Customer(
        name = request.POST['name'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password']
        )
        mycustomer.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')