from django.shortcuts import HttpResponse, render


def home(request):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html')


def print_name(request, name, age):
    # return HttpResponse(f'<h1>Name: {name} Age:{age}</h1>')
    print(name, age)
    context = {'name': name, 'age': age}
    return render(request, 'print_name.html', context)
