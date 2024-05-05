"""
Definition of views.
"""

import datetime
from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        self.year = datetime.now().year
        context = {'year': self.year}
        return render(request, 'app/index.html', context)

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            if len(name) < 1 or len(email) < 1 or len(subject) < 1 or len(message) < 1:
                return HttpResponse('Please enter all fields', status=400)
            send_mail(
                f"Someone Contacted Your Email",
                f"{name}\n\n{email}\n\n{message}",
                settings.EMAIL_HOST_USER,
                ["gdsr786@gmail.com"],
                fail_silently=False,
            )
            return HttpResponse("Your Message has been sent.", status=200)
        except Exception as e:
            return HttpResponse(e.args[0], status_code=500)

# class SendEmailView(View):
#     def post(self, request):
#         try:
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             subject = request.POST.get('subject')
#             message = request.POST.get('msg')
#             send_mail(
#                 f"{name}, {subject}",
#                 f"{email}\n\n{message}",
#                 settings.EMAIL_HOST_USER,
#                 ["gdsr786@gmail.com"],
#                 fail_silently=False,
#             )
#             return HttpResponse("Successfully Sent Email")
#         except Exception as e:
#             return HttpResponse(e.args[0])
