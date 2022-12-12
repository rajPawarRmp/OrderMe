from django.shortcuts import render
from hotel.models import Dish

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def cart(request):
    if not request.session.get('cart'):
         messages.error(request, 'cart is empty ! please add dishes to cart')
         return redirect("/menu/")
    names=list(request.session.get('cart').keys())
    dishes=Dish.get_dish_by_name(names)
    
    return render(request,'cart.html',{'dishes':dishes})
def register(request):

    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST["password"]
        email = request.POST["email"]
        if User.objects.filter(username=username):
            messages.error(
                request, 'username is already taken try different username')
            return redirect('/register/')

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        user.save()
        messages.error(request, 'Registration Successsfull !, please Login')
        return redirect('/login/')
    else:
        return render(request, 'register.html')


def login(request):
		if request.method == 'POST':
				username = request.POST["username"]
				password = request.POST["password"]
				user = authenticate(username=username, password=password)
				if user is not None:
					print("login success")
					auth.login(request, user)
					if user.is_superuser:
						return redirect('/addDish/')
					else:
						return redirect('/menu/')
				else:
					messages.error(request, 'user not found , Please Register first')
					return redirect('/register/')

		else:
			return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'log out ')
    return redirect('/login/')

def thankyou(request):
    auth.logout(request)
    # messages.success(request, 'log out ')
    return render(request, 'thankyou.html')


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        type = request.POST.get('type')
        img = request.FILES.get('img')

        dish = Dish(
            dname=name,
            price=price,
            type=type,
            img=img,

        )
        dish.save()
        messages.success(request, 'dish added')
        return redirect('/addDish/')
    return render(request, 'addDish.html')


def addDish(request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                dish = Dish.objects.all()
                contest = {
                    'dish': dish,
                }
                return render(request, 'addDish.html', contest)
            else:
                 return redirect('/menu/')
                   
        return redirect('/login/')

def menu(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                    product=request.POST.get('product')
                    cart=request.session.get('cart')
                    if cart:
                        quantity=cart.get(product)
                        if quantity:
                            cart[product]=quantity+1
                        else:
                            cart[product]=1
                    else:
                        cart={}
                        cart[product]=1  
                    request.session['cart']=cart
                    # print(cart)  
                    messages.success(request, 'dish added')   
                    return redirect('/menu/')
            else:  
                    print('get request')
                    dish = Dish.objects.all()
                    contest = {
                            'dish': dish,
                        }
                    return render(request, 'menu.html', contest)
        return redirect('/login/')

def edit(request):

    dish = Dish.objects.all()
    contest = {
        'dish': dish,
    }
    return render(request, 'addDish.html', contest)


def update(request, dname):
    if request.method == 'POST':
        dishname = request.POST.get('dname')
        price = request.POST.get('price')
        type = request.POST.get('type')
        # img=request.POST.get('img')

        dish = Dish.objects.get(dname=dname)
        # dish = Dish.objects.get(dname=dishname)
        dish.dname = dishname
        dish.price = price
        dish.type = type

        dish.save()
        return redirect('/addDish/')

    return render(request, 'addDish.html')


def delete(request, dname):
    if request.method == 'POST':

        Dish.objects.filter(dname=dname).delete()

        return redirect('/addDish/')

    return render(request, 'addDish.html')
