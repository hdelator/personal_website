from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ContactMeModel
from .forms import ContactMeForm
from django.core.mail import send_mail
from django.contrib import messages
import json


def index(request):
    if request.method == 'POST':
        post_name = request.POST.get('name')
        post_email = request.POST.get('email')
        post_subject = request.POST.get('subject')
        post_message = request.POST.get('message')

        response_data = {}

        post = ContactMeModel(name=post_name,
                              email=post_email,
                              subject=post_subject,
                              message=post_message
                              )
        post.save()

        response_data['result'] = 'Post has been created successfully'
        response_data['name'] = post.name
        response_data['subject'] = post.subject
        response_data['email'] = post.email
        response_data['message'] = post.message
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')

        # try:  # todo: create email routine to get notified
        #     recipients = ['htorrecasado@gmail.com']
        #     send_mail(post_name, post_subject, from_email=post_email, recipient_list=recipients)
        # except:
        #     pass

        print(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )  # notice that we don't redirect here
    else:
        form = ContactMeForm()
        return render(request, 'index.html', {'form': form})

# def new_contact(request):
#     if request.method == 'POST':
#         print("POST initiated")
#         form = ContactMeForm(request.POST)
#
#         # for field in form: # for debugging
#         #     print("Field Error:", field.name, field.errors)
#
#         if form.is_valid():
#             print('Form valid!')
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             subject = form.cleaned_data["subject"]
#             message = form.cleaned_data["message"]
#
#             form.save()  # add to database
#
#             # Send email to myself when successful form has been submitted
#             # try:  # todo: fix
#             #     recipients = ['htorrecasado@gmail.com']
#             #     send_mail(subject, message, from_email=email, recipient_list=recipients)
#             # except:
#             #     pass
#
#             messages.success(request, 'Your message has been sent successfully')
#             form = ContactMeForm()  # empty form before redirecting
#             return render(request, 'index.html', {'form': form})
#         else:
#             messages.error(request, 'Invalid form submission.')
#             messages.error(request, form.errors)
#     else:  # GET
#         form = ContactMeForm()
#
#         print('GET method')
#
#         return render(request, 'index.html', {'form': form})
#



