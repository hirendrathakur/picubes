from django.shortcuts import render
from contact.models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        save_it = Contact(name=n, email=e, phone=p)
        save_it.save();
        return render(request, 'index2.html')
    else:
        return render(request, 'index2.html')