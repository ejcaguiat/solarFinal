from django.db import models
from datetime import datetime 


# Create your models here.
class salesProperty(models.Model):
    #Location Details
    region = models.CharField(max_length = 255, default = "")
    province = models.CharField(max_length = 255, default = "")
    municipality = models.CharField(max_length = 255, default = "")
    barangay = models.CharField(max_length = 255, default = "")
    #End of Location Details
    
    #Property Owner's Details
    regLandOwner = models.CharField(max_length = 255, default = "")
    contactNum = models.CharField(max_length = 255, default = "")
    Payee = models.CharField(max_length = 255, default = "")
    #End of Property Owner's Details
    
    #Property Details
    titleNum = models.CharField(max_length = 255, default = "")
    
    areaHectares = models.FloatField(default = None)
    
    #End of Property Details
    
    #Payment Details
    pricePerHectare = models.FloatField(default = None)
    totalContractPrice = models.FloatField(default = None)
    #End of Payment Details
    
    #Released Pxyments
    firstPayAmount = models.FloatField(default = None)
    firstPayDate = models.CharField( max_length = 255, default = "")
    
    secPayAmount = models.FloatField(default = 0)
    secPayDate = models.CharField( max_length = 255, default = "")
    
    thirdPayAmount = models.FloatField(default = 0)
    thirdPayDate = models.CharField(max_length = 255, default = "")
    
    fourthPayAmount = models.FloatField(default = 0)
    fourthPayDate = models.CharField(max_length = 255, default = "")
    
    fifthPayAmount = models.FloatField(default = 0)
    fifthPayDate = models.CharField(max_length = 255, default = "")
    
    sixthPayAmount = models.FloatField(default = 0)
    sixthPayDate = models.CharField(max_length = 255, default = "")
    
    seventhPayAmount = models.FloatField(default = 0)
    seventhPayDate = models.CharField(max_length = 255, default = "")
    
    eigthPayAmount = models.FloatField(default = 0)
    eigthPayDate = models.CharField(max_length = 255, default = "")
    
    ninthPayAmount = models.FloatField(default = 0)
    ninthPayDate = models.CharField(max_length = 255, default = "")
    
    tenthPayAmount = models.FloatField(default = 0)
    tenthPayDate = models.CharField(max_length = 255, default = "" )
    
    releasedPayment = models.FloatField(default=None)
    balance = models.FloatField(default=None)
    #End of Released Payments
    
    #Taxes and Registration Fees
    BIRcgt = models.FloatField(default=None)
    BIRdst = models.FloatField(default=None)
    LGUtransfer = models.FloatField(default=None)
    RODlra = models.FloatField(default=None)
    RODit = models.FloatField(default=None)
    OTHERSnotorial = models.FloatField(default=None)
    SUMother = models.FloatField(default=None)
    #missing LBP column
    TAXother = models.FloatField(default=None)
    #End of Taxes and Registration Fees
    
    
    
    area = models.FloatField(default = None)
    
    
    
    
class leaseProperty(models.Model):
    #missing   NUMBER OF YEARS FOR ADVANCE PAYMENT
    #representative WALA DAPAT
    
    #Location Details
    region = models.CharField(max_length = 255, default = "")
    province = models.CharField(max_length = 255, default = "")
    municipality = models.CharField(max_length = 255, default = "")
    barangay = models.CharField(max_length = 255, default = "")
    #End of Location Details
    
    #Property Owner's Details
    regLandOwner = models.CharField(max_length = 255, default = "")
    contactNum = models.CharField(max_length = 255, default = "")
    Address = models.CharField(max_length = 255, default = "")
   
    #End of Property Owner's Details
    
     #Payment Details
    pricePerHectare = models.FloatField(default = None)
    
    numofyear = models.FloatField(default = None)
    #End of Payment Details
    
    
    #Taxes and Registration Fees
    BIRcgt = models.FloatField(default=None)
    BIRdst = models.FloatField(default=None)
    LGUtransfer = models.FloatField(default=None)
    RODlra = models.FloatField(default=None)
    RODit = models.FloatField(default=None)
    OTHERSnotorial = models.FloatField(default=None)
    SUMother = models.FloatField(default=None)
    TAXother = models.FloatField(default=None)
    #End of Taxes and Registration Fees
    
    Payee = models.CharField(max_length = 255, default = "")
    area = models.FloatField(default = None)
    taxDec = models.CharField(max_length = 255,   default = "")
    dateRelease = models.DateField(default=None)
    balance = models.FloatField(default = None)
    
    #Property Details
    titleNum = models.CharField(max_length = 255, default = "")
    lotNum = models.CharField(max_length = 255, default = "")
    #Released Payments
    leaseamountperyear= models.FloatField(default = 0)
    advPayment = models.FloatField(default = 0)
    advPaymentDate = models.FloatField(default = 0)
    year1Pay = models.FloatField(default = 0)
    year1Date = models.CharField(max_length = 255,   default = "")
    
    year2Pay = models.FloatField(default = 0)
    year2Date = models.CharField(max_length = 255,   default = "")
    
    year3Pay = models.FloatField(default = 0)
    year3Date = models.CharField(max_length = 255,   default = "")
    
    year4Pay = models.FloatField(default = 0)
    year4Date = models.CharField(max_length = 255,   default = "")
    
    year5Pay = models.FloatField(default = 0)
    year5Date = models.CharField(max_length = 255,   default = "")
    
    year6Pay = models.FloatField(default = 0)
    year6Date = models.CharField(max_length = 255,   default = "")
    
    year7Pay = models.FloatField(default = 0)
    year7Date = models.CharField(max_length = 255,   default = "")
    
    year8Pay = models.FloatField(default = 0)
    year8Date = models.CharField(max_length = 255,   default = "")
    
    year9Pay = models.FloatField(default = 0)
    year9Date = models.CharField(max_length = 255,   default = "")
    
    year10Pay = models.FloatField(default = 0)
    year10Date = models.CharField(max_length = 255,   default = "")
    
    year11Pay = models.FloatField(default = 0)
    year11Date = models.CharField(max_length = 255,   default = "")
    
    year12Pay = models.FloatField(default = 0)
    year12Date = models.CharField(max_length = 255,   default = "")
    
    year13Pay = models.FloatField(default = 0)
    year13Date = models.CharField(max_length = 255,   default = "")
    
    year14Pay = models.FloatField(default = 0)
    year14Date = models.CharField(max_length = 255,   default = "")
    
    year15Pay = models.FloatField(default = 0)
    year15Date = models.CharField(max_length = 255,   default = "")
    
    year16Pay = models.FloatField(default = 0)
    year16Date = models.CharField(max_length = 255,   default = "")
    
    year17Pay = models.FloatField(default = 0)
    year17Date = models.CharField(max_length = 255,   default = "")
    
    year18Pay = models.FloatField(default = 0)
    year18Date = models.CharField(max_length = 255,   default = "")
    
    year19Pay = models.FloatField(default = 0)
    year19Date = models.CharField(max_length = 255,   default = "")
    
    year20Pay = models.FloatField(default = 0)
    year20Date = models.CharField(max_length = 255,   default = "")
    
    year21Pay = models.FloatField(default = 0)
    year21Date = models.CharField(max_length = 255,   default = "")
    
    year22Pay = models.FloatField(default = 0)
    year22Date = models.CharField(max_length = 255,   default = "")
    
    year23Pay = models.FloatField(default = 0)
    year23Date = models.CharField(max_length = 255,   default = "")
    
    year24Pay = models.FloatField(default = 0)
    year24Date = models.CharField(max_length = 255,   default = "")
    
    year25Pay = models.FloatField(default = 0)
    year25Date = models.CharField(max_length = 255,   default = "")
    
    year26Pay = models.FloatField(default = 0)
    year26Date = models.CharField(max_length = 255,   default = "")
    
    year27Pay = models.FloatField(default = 0)
    year27Date = models.CharField(max_length = 255,   default = "")
    
    year28Pay = models.FloatField(default = 0)
    year28Date = models.CharField(max_length = 255,   default = "")
    
    year29Pay = models.FloatField(default = 0)
    year29Date = models.CharField(max_length = 255,   default = "")
    
    year30Pay = models.FloatField(default = 0)
    year30Date = models.CharField(max_length = 255,   default = "")
    
    
    
    
    
class User(models.Model):
    username = models.CharField(max_length = 255,   default = "")
    password = models.CharField(max_length=50)
    choices = ((0, 'Regular User'), (1, 'Admin'))
    accountType = models.IntegerField(choices=choices, default = 0)
    
    
    