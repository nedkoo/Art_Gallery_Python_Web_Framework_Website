from django.shortcuts import render


# Create your views here.
def main_page(request):
    context = {
        'current_page': 'home'
    }
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        'current_page': 'about'
    }
    return render(request, 'about.html', context)
