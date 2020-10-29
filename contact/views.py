from django.shortcuts import render, redirect, reverse
from django.contrib import  messages
from django.core.mail import send_mail


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

        #check if user has made inquiry already 
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,"you have made already an inquiry for this listing")
                return redirect(reverse("realstate:home_detail", kwargs={
                    'list_id':listing_id
                }))

        contact = Contact(user_id=user_id, listing_id=listing_id,listing=listing,\
            name=name,email=email,phone=phone, message=message)
        contact.save()

        send_mail(
            'Property listing inquiry',
            'There is an inquiry for '+listing+' sign in to the admin panel for more.',
            'sh.danishyar@gmail.com', #this one which is in setting also we have it.   
            [realtor_email, 'gulnar.norbeg@yahoo.com','another@email.com','asmany@email.youwant'],
            fail_silently=False,
        )
        messages.success(request, "your request has been submitted, our realtor wil get back you soon")

        return redirect(reverse("realstate:home_detail", kwargs={
            'list_id': listing_id})
            )
