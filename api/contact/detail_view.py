from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if name and email and message:
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                email,  # Sender's email address
                [settings.EMAIL_HOST_USER],  # List of recipients
                fail_silently=False,
            )
            thank_you_message = (
                "Thank you for contacting the ECDGT,\n\n"
                "We got your message and if it requires a response we will be in touch shortly."
                "\n\n"
                "East Coast Disc Golf Tour"
            )
            send_mail(
                'Thank You!',
                thank_you_message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return JsonResponse({'message': 'Email sent successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Missing required data'}, status=400)
