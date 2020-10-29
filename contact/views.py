from django.shortcuts import render, redirect, reverse
from django.contrib import  messages


from .models import Contact

def contact(request):
    if request.method == 'POST':
        realtor_email = request.POST['realtor_email']
        user_id    = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing    = request.POST['listing'] # which is title 
        name       = request.POST['name']
        email      = request.POST['email']
        phone      = request.POST['phone']
        message    = request.POST['message']

        contact = Contact(user_id=user_id, listing_id=listing_id,listing=listing,\
            name=name,email=email,phone=phone, message=message)
        contact.save()
        messages.success(request, "your request has been submitted, our realtor wil get back you soon")

        return redirect(reverse("realstate:home_detail", kwargs={
            'list_id': listing_id})
            )
