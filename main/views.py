from django.shortcuts import render

menu = [{'name': 'Home', 'url': 'index'},
            {'name': 'Shop', 'url': 'shop'},
            {'name': 'FAQ', 'url': 'questions'},
            {'name': 'Contacts', 'url': 'contacts'},
            # {'name': 'Add Product', 'url': 'add_product'},
            # {'name': 'Add Category', 'url': 'add_category'},
            ]

# Create your views here.
def index(request):
    products = [{'id': 1,
                'title': 'T-Shirt 1',
                'articul': '2215',
                'price': 25}]
    context = {
        'menu': menu,
        'title': 'Home Page',
        'products': products
    }
    return render(request, 'index.html', context=context)

def contacts(request):
    context = {
        'menu': menu,
        'title': 'Contacts'
    }
    return render(request, 'contacts.html', context=context)

def questions(request):
    context = {
        'menu': menu,
        'title': 'FAQ'
    }
    return render(request, 'questions.html', context=context)