from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from crum import get_current_user
from datetime import datetime

class Email_template(models.Model):
    template_name = models.CharField(max_length = 150 )
    subject = models.CharField(max_length = 1023)
    content = models.TextField(max_length = 4095)

    def __str__(self):
        return self.template_name

class Email(models.Model):
    template = models.ForeignKey(Email_template, on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add = timezone.now)
    from_email = models.EmailField(max_length=150, blank=True, default=get_current_user())
    subject = models.CharField(max_length = 1023, blank=True, default='Empty field, save the email with a template and user to see the content of this field')
    content = models.TextField(max_length = 4095, blank=True, default='Empty field, save the email with a template and user to see the content of this field')

    def save(self):
        current_user = get_current_user()
        self.from_email = current_user.email
        self.subject = self.template.subject.format(User.get_full_name(self.user))
        inverted_name = self.user.last_name +', '+ self.user.first_name
        formatted_creation_date_time = datetime.now()
        self.content = self.template.content.format(inverted_name,formatted_creation_date_time.strftime('%Y-%m-%d %H:%M:%S'))
        super().save()
        

    def __str__(self):
        text = '{} for {}'
        return text.format(self.template.template_name,self.user.first_name)

    def get_absolute_url(self):
        return reverse('email', args=[str(self.id)])

