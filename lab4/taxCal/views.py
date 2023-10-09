from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

tax_rate = 0.15  


def home(request):
    return render(request, 'home.html')

def calculate_tax(request, number):
    total_price = number + (number * tax_rate)
    return render(request, 'calculate_tax.html', {'total_price': total_price})

def tax_rate(request):
    return render(request, 'tax_rate.html', {'tax_rate': tax_rate})
