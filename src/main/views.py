from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from contact.models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        m = request.POST.get('message')
        save_it = Contact(name=n, email=e, phone=p, message=m)
        save_it.save();
        return HttpResponseRedirect('/')
    else:
        return render(request, 'index2.html')