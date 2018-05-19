from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from .models import Account


def account_create(request):
    data = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, email=email, password=password)
        phone = request.POST.get('phone')
        link1 = request.POST.get('link1')
        link2 = request.POST.get('link2')
        link3 = request.POST.get('link3')

        account = Account(user=user, phone=phone, link1=link1, link2=link2, link3=link3)

        user.save()
        account.save()

        if not username and password:
            data['errors'] = {
                'username': 'Is required',
                'password': 'Is required'
            }
        else:
            user.save()
            account.save()

    data = serializers.serialize('json', Account.objects.all())
    return JsonResponse(data)
