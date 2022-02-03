from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from tienda.models import Category, Product, Client
from tienda.cart import Cart
from tienda.forms import ClientForm

# 1 Create your views here.
def index(request):
    listCategorys = Category.objects.all()
    listProducts = Product.objects.all()
    context = {
        'products': listProducts,
        'categorys': listCategorys
    }
    return render(request, 'index.html', context)

def productsByCategory(request, category_id):
    objCategory = Category.objects.get(pk=category_id)
    listCategorys = Category.objects.all()
    listProducts = objCategory.product_set.all()
    context = {
        'products': listProducts,
        'categorys': listCategorys
    }
    return render(request, 'index.html', context)

def product(request, product_id):
    objProduct = Product.objects.get(pk=product_id)
    context = {
        'product': objProduct,
    }
    return render(request, 'product.html', context)

def cart(request):
    return render(request, 'cart.html')

def addCart(request, product_id):
    objProduct = Product.objects.get(id=product_id)
    CartProduct = Cart(request)
    CartProduct.add(objProduct, 1)
    print(request.session.get('cart'))
    return render(request, 'cart.html')

def deleteCart(request, product_id):
    objProduct = Product.objects.get(id=product_id)
    CartProduct = Cart(request)
    CartProduct.remove(objProduct)
    return render(request, 'cart.html')

def clearCart(request):
    CartProduct = Cart(request)
    CartProduct.clear()
    return render(request, 'cart.html')

######################### LOGIN Y REGISTER USERS

def loginUser(request):
    context = {}
    if request.method == 'POST':
        dataUser = request.POST['username']
        dataPassword = request.POST['password']
        userAuth = authenticate(request, username=dataUser, password=dataPassword)
        if userAuth is not None:
            login(request, userAuth)
            return redirect('/profile')
        else:
            context ={
                'error': 'Invalid username or password',
            }
    return render(request, 'login.html', context)

def acountUsers(request):
    try:
        clienteEditar = Client.objects.get(usuario = request.user)
        dataClient = {'first_name':request.user.first_name,
                    'last_name':request.user.last_name,
                    'email':request.user.email,
                    'direction':clienteEditar.direction,
                    'phone':clienteEditar.phone,
                    'username':request.user.username}
    except:
        dataClient = {'first_name':request.user.first_name,
                    'last_name':request.user.last_name,
                    'email':request.user.email,
                    'username':request.user.username}
    
    frmClient = ClientForm(dataClient)
    
    context = {
        'frmClient':frmClient
    }
    return render(request,'profile.html',context)

def createUser(request):
    if request.method == 'POST':
        dataUser = request.POST['newUser']
        dataPassword = request.POST['newPassword']
        newUser = User.objects.create_user(username=dataUser,password=dataPassword)
        login(request,newUser)
        return redirect('/profile')
