from django.shortcuts import render

# Create your views here.
def test(request):
    context={
        'msg': 'hellooooo',
        'title': 'wowowowowow'
    }
    return render(request, 'hello.html', context)
