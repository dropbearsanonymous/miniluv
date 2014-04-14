from django.shortcuts import render
from django.http import HttpResponse, Http404

from recruit.models import Account, EveAccount

def index(request):
    return HttpResponse("working")

def account(request, accountName):
    try:
        requestedAccount = Account.objects.get(accountName__iexact=accountName)
        eveaccounts = requestedAccount.eveaccount_set.all()
    except Account.DoesNotExist:
        raise Http404
    return render(request, 'recruit/account.html', {'account': requestedAccount, 'eveaccounts': eveaccounts})

def accountsList(request):
    accounts = Account.objects.order_by('accountName')
    context = {'accounts': accounts}
    return render(request, 'recruit/accounts.html', context) 
