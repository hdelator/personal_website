from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import ContactMeForm
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    form = ContactMeForm()
    print('GET method')
    return render(request, 'index.html', {'form': form})


def new_contact(request):
    if request.method == 'POST':
        print("POST initiated")
        form = ContactMeForm(request.POST)

        for field in form: # for debugging
            print("Field Error:", field.name, field.errors)

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


        # login_data = request.POST.dict()
        # name = login_data.get("name")
        # email = login_data.get("email")
        # subject= login_data.get("subject")
        # message = login_data.get("message")
        #
        # ContactMeForm.objects.create(name=name,
        #                              email=email,
        #                              subject=subject,
        #                              message=message,
        #                              date=timezone.now())
        #
        # print(login_data)

        # if form.is_valid(): # todo: add sending email when someone contacts me
        #     subject = form.cleaned_data['subject']
        #     message = form.cleaned_data['message']
        #     sender = form.cleaned_data['sender']
        #     cc_myself = form.cleaned_data['cc_myself']
        #
        #     recipients = ['info@example.com']
        #     if cc_myself:
        #         recipients.append(sender)
        #
        #     send_mail(subject, message, sender, recipients)
    #     return render(request, "index.html")
    # else:
    #     return render(request, "index.html")


# def new_contact(request):
#     if request.method == 'POST':
#         form = request.POST.dict()
#         print(form)
#     else:
#         return render(request, "resume/new_contact.html")

    #     login_data = request.POST.dict()
    #     username = login_data.get("username")
    #     password = login_data.get("password")
    #     user_type = login_data.get("user_type")
    #     print(user_type, username, password)
    #     return HttpResponse("This is a post request")
    # #
    # #
    # #
    # #
    # # contact = request.POST.get('contact')
    # # ContactMeForm.objects.create(name=name,
    # #                              email=email,
    # #                              subject=subject,
    # #                              message=message,
    # #                              date=timezone.now())
    # else:
    #     return render(request, "index.html")




