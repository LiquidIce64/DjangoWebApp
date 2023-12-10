from django.shortcuts import render
from .forms import ExampleForm


def form_example(request):
    for name in request.POST:
        print(f"{name}: {request.POST.getlist(name)}")
    return render(request, 'form-example.html', {
        "method": request.method,
        "form": ExampleForm()
    })
