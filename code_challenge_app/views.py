from django.shortcuts import render, get_object_or_404
from .models import Email


def create_email(request, pk):
    email = get_object_or_404(Email, pk=pk)
    
    subject = email.subject
    content = email.content

    context = {
        
        'subject':subject,
        'content':content,
    }

    return render(request, 'code_challenge_app/email.html', context)


