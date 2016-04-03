from django.shortcuts import render, render_to_response, RequestContext

from .forms import ContactForm, userform
from .models import Contact
# Create your views here.


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()

        else:
            print form.errors
        form = ContactForm()
    else:
        form=ContactForm()

    return render(request, "contact/contact.html",{'form':form},)

def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    save_it = Contact(name=name, email=email, phone=phone)
    save_it.save();
    return render(request, 'main/index2.html')