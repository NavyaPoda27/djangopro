from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm
def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                'navyapoda@zohomail.in',
                [form.cleaned_data['recipient_email']],
                fail_silently=False, )
            return render(request, 'email_sent.html')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})


# Create your views here.
