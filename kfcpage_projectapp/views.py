from django.http import HttpResponse
from django.template import loader
from . models import *

# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def menu(request):
    my_orders1=INTERNATIONAL_BURGER_FEST.objects.all().values()
    my_orders2=MATCH_DAY_COMBOS.objects.all().values()
    my_orders3=VALUE_LUNCH_SPECIALS.objects.all().values()
    my_orders4=BOX_MEAL.objects.all().values()
    my_orders5=BURGERS.objects.all().values()
    my_orders6=CHICKEN_BUCKETS.objects.all().values()
    my_orders7=RICE_BOWLZ.objects.all().values()
    my_orders8=SNACKS.objects.all().values()
    template=loader.get_template('menu.html')
    context={
        'my_orders1':my_orders1,
        'my_orders2':my_orders2,
        'my_orders3':my_orders3,
        'my_orders4':my_orders4,
        'my_orders5':my_orders5,
        'my_orders6':my_orders6,
        'my_orders7':my_orders7,
        'my_orders8':my_orders8,
    }
    return HttpResponse(template.render(context,request))

def signin(request):
    template=loader.get_template('signin.html')
    return HttpResponse(template.render())

def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())

def orders1(request,id):
    my_orders1=INTERNATIONAL_BURGER_FEST.objects.get(id=id)
    template=loader.get_template('orders1.html')
    context={
        'my_orders1':my_orders1,
    }
    return HttpResponse(template.render(context,request))

def orders2(request,id):
    my_orders2=MATCH_DAY_COMBOS.objects.get(id=id)
    template=loader.get_template('orders2.html')
    context={
        'my_orders2':my_orders2,
    }
    return HttpResponse(template.render(context,request))

def orders3(request,id):
    my_orders3=VALUE_LUNCH_SPECIALS.objects.get(id=id)
    template=loader.get_template('orders3.html')
    context={
        'my_orders3':my_orders3,
    }
    return HttpResponse(template.render(context,request))

def orders4(request,id):
    my_orders4=BOX_MEAL.objects.get(id=id)
    template=loader.get_template('orders4.html')
    context={
        'my_orders4':my_orders4,
    }
    return HttpResponse(template.render(context,request))

def orders5(request,id):
    my_orders5=BURGERS.objects.get(id=id)
    template=loader.get_template('orders5.html')
    context={
        'my_orders5':my_orders5,
    }
    return HttpResponse(template.render(context,request))

def orders6(request,id):
    my_orders6=CHICKEN_BUCKETS.objects.get(id=id)
    template=loader.get_template('orders6.html')
    context={
        'my_orders6':my_orders6,
    }
    return HttpResponse(template.render(context,request))

def orders7(request,id):
    my_orders7=RICE_BOWLZ.objects.get(id=id)
    template=loader.get_template('orders7.html')
    context={
        'my_orders7':my_orders7,
    }
    return HttpResponse(template.render(context,request))

def orders8(request,id):
    my_orders8=SNACKS.objects.get(id=id)
    template=loader.get_template('orders8.html')
    context={
        'my_orders8':my_orders8,
    }
    return HttpResponse(template.render(context,request))

def abc(request):
    template=loader.get_template('abc.html')
    context={
        'my_name':'username1',
        'eligible': 18,
        'a':['a','b','c'],
        'b':['a','b','c'],

    }
    return HttpResponse(template.render(context,request))