from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import ContactMeForm
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    form = ContactMeForm()
    return render(request, 'index.html', {'form': form})


def new_contact(request):
    if request.method == 'POST':
        print("POST initiated")
        form = ContactMeForm(request.POST)

        # for field in form: # for debugging
        #     print("Field Error:", field.name, field.errors)

        if form.is_valid():
            print('Form valid!')
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            form.save()  # add to database

            # Send email to myself when successful form has been submitted
            # try:  # todo: fix
            #     recipients = ['htorrecasado@gmail.com']
            #     send_mail(subject, message, from_email=email, recipient_list=recipients)
            # except:
            #     pass

            messages.info(request, 'Your message has been sent successfully!')
            # messages.success(request, 'Your message has been sent successfully') # alternative way

            form = ContactMeForm()  # empty form before redirecting

            return render(request, 'resume/new_contact.html', {'form': form})
    else:  # GET
        form = ContactMeForm()

        print('GET method')

        return render(request, 'index.html', {'form': form})




