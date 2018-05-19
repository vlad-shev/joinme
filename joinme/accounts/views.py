from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from .models import Account
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def account_create(request):
    data = []
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=username)
            data = serializers.serialize('json', [user])
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, first_name=first_name,
                                            last_name=last_name, email=email, password=password)
            phone = request.POST.get('phone')
            link = request.POST.get('link')
            account = Account(user=user, phone=phone, link=link)
            user.save()
            data = serializers.serialize('json', Account.objects.all())
        return JsonResponse(data, safe=False)
