from django.db import models

class Account(models.Model):
    accountName = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    login = models.BooleanField()                 # false: default shell account, true: can log in
    
    STATUS_LABELS = (
        ('A', 'applied'),
        ('M', 'member'),
        ('R', 'rejected'),
        ('S', 'spai')
    )
    status = models.CharField(max_length=1, choices=STATUS_LABELS)

    # TO ADD: account auth

    def __unicode__(self):
        return self.accountName

class EveAccount(models.Model):
    account = models.ForeignKey(Account)

    # API key
    keyId = models.IntegerField(default=0)
    keyVerify = models.CharField(max_length=64)

    def __unicode__(self):
        return self.id

class Character(models.Model):
    eveaccount = models.ForeignKey(EveAccount)

    name = models.CharField(max_length=50)
    alliance = models.CharField(max_length=50)
    corporation = models.CharField(max_length=50)
    standing = models.DecimalField(max_digits=3, decimal_places=1)
    secStatus = models.DecimalField(max_digits=3, decimal_places=1)
    joinDate = models.DateTimeField()   
    skillPoints = models.IntegerField()

    def __unicode__(self):
        return self.name

