from django.shortcuts import render

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
