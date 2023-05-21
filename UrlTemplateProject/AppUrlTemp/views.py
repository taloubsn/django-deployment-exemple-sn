from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'Hello World', 'number':'100'}
    return render(request, 'AppUrlTemp/index.html', context=context_dict)

def other(request):
    return render(request, 'AppUrlTemp/other.html')

def relative(request):
    return render(request, 'AppUrlTemp/relative_url_template.html')