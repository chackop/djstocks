from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c6e36757831f4bb287427656aec5840e")

        try:
            api = json.loads(api_request.content)
        except Exception as identifier:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter ticker symbol"})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker':  ticker})
