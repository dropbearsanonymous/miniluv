from django.shortcuts import render
from django.http import HttpResponse, Http404

from recruit.models import Account, EveAccount

def index(request):
    return HttpResponse("working")

def account(request, accountName):
    try:
        requestedAccount = Account.objects.get(accountName__iexact=accountName)
        eveaccounts = requestedAccount.eveaccount_set.all()
	if request.method == "POST":
	    requestedAccount.status = request.POST['status']
	    requestedAccount.save()
    except Account.DoesNotExist:
        raise Http404
    return render(request, 'recruit/account.html', {'account': requestedAccount, 'eveaccounts': eveaccounts})

def accountsList(request, accountType):
    if accountType == "all":
        accounts = Account.objects.order_by('accountName')
    elif accountType == "apps":
        accounts = Account.objects.filter(status__iexact="A").order_by('id')
    elif accountType == "members":
        accounts = Account.objects.filter(status__iexact="M").order_by('accountName')
    elif accountType == "rejects":
        accounts = Account.objects.filter(status__iexact="R").order_by('accountName')
    elif accountType == "spais":
        accounts = Account.objects.filter(status__iexact="S").order_by('accountName')
    else:
        raise Http404
    context = {'accounts': accounts}
    return render(request, 'recruit/accounts.html', context) 
