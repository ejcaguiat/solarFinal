from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session

from .models import User
from .models import salesProperty
from .models import leaseProperty

# Create your views here.
def index(request):
    

    context = {}
    if request.method == "POST":
        if 'login' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

                request.session['user'] = user.pk
                #request.session['type'] = user.get_type()
                return HttpResponseRedirect('homepage')

            except User.DoesNotExist:
                context['log_error'] = 'Cannot find an account with that combination.'
                
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
            return render(request, 'register.html', context)
                
    return render(request, 'login.html', context)


def register(request):
    context = {}
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
    return render(request, 'register.html', context)

def homepage(request):
    try:
        loggeduser = User.objects.get(id=request.session['user'])
    except(KeyError, User.DoesNotExist):
        loggeduser = 0
    context = {
            'loggeduser':loggeduser,
    }
    return render(request, 'homepage.html', context)

def salesview(request):
    all_properties =salesProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }

    
    return render(request, 'displaysales.html',context)

def leaseview(request):
    all_properties =leaseProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }

    
    return render(request, 'displaylease.html',context)

def leaseregister(request):
    
    if 'leaseproperty' in request.POST:
        property =leaseProperty(region=request.POST['region']
                                            , province=request.POST['province']
                                           
                                            , municipality=request.POST['municipality']
                                            , barangay=request.POST['barangay']
                                           
                                            ,regLandOwner=request.POST['registeredlandowner']
                                            , representative=request.POST['representative']
                                           
                                           , Address=request.POST['address']
                                           , contactNum=request.POST['contactnumber']
                                           
                                           , titleNum=request.POST['titlenumber']
                                           , lotNum=request.POST['lotnumber']
                                        
                                           ,taxDec=request.POST['taxdeclaration']
                                ,leaseamountperyear=request.POST['leaseamountperyear']
                                ,advPaymentDate=request.POST['advancepayment_date']
                                ,advPayment=request.POST['advancepayment_amount']
                                
                                            ,pricePerHectare=request.POST['leasepriceperhectare']
                                            
                                , year1Pay=request.POST['year1Pay']
                                           , year1Date=request.POST['year1Date']
                                , year2Pay=request.POST['year2Pay']
                                           , year2Date=request.POST['year2Date']
                                , year3Pay=request.POST['year3Pay']
                                           , year3Date=request.POST['year3Date']
                                , year4Pay=request.POST['year4Pay']
                                           , year4Date=request.POST['year4Date']
                                , year5Pay=request.POST['year5Pay']
                                           , year5Date=request.POST['year5Date']
                                , year6Pay=request.POST['year6Pay']
                                           , year6Date=request.POST['year6Date']
                                , year7Pay=request.POST['year7Pay']
                                           , year7Date=request.POST['year7Date']
                                , year8Pay=request.POST['year8Pay']
                                          , year8Date=request.POST['year8Date']
                                , year9Pay=request.POST['year9Pay']
                                           , year9Date=request.POST['year9Date']
                                , year10Pay=request.POST['year10Pay']
                                           , year10Date=request.POST['year10Date']
                                
                                
                                , year11Pay=request.POST['year11Pay']
                                           , year11Date=request.POST['year11Date']
                                , year12Pay=request.POST['year12Pay']
                                           , year12Date=request.POST['year12Date']
                                , year13Pay=request.POST['year13Pay']
                                           , year13Date=request.POST['year13Date']
                                , year14Pay=request.POST['year14Pay']
                                           , year14Date=request.POST['year14Date']
                                , year15Pay=request.POST['year15Pay']
                                           , year15Date=request.POST['year15Date']
                                , year16Pay=request.POST['year16Pay']
                                           , year16Date=request.POST['year16Date']
                                , year17Pay=request.POST['year17Pay']
                                           , year17Date=request.POST['year17Date']
                                , year18Pay=request.POST['year18Pay']
                                           , year18Date=request.POST['year18Date']
                                , year19Pay=request.POST['year19Pay']
                                           , year19Date=request.POST['year19Date']
                                , year20Pay=request.POST['year20Pay']
                                           , year20Date=request.POST['year20Date']
                                
                                
                                , year21Pay=request.POST['year21Pay']
                                           , year21Date=request.POST['year21Date']
                                , year22Pay=request.POST['year22Pay']
                                           , year22Date=request.POST['year22Date']
                                , year23Pay=request.POST['year23Pay']
                                           , year23Date=request.POST['year23Date']
                                , year24Pay=request.POST['year24Pay']
                                           , year24Date=request.POST['year24Date']
                                , year25Pay=request.POST['year25Pay']
                                           , year25Date=request.POST['year25Date']
                                , year26Pay=request.POST['year26Pay']
                                           , year26Date=request.POST['year26Date']
                                , year27Pay=request.POST['year27Pay']
                                           , year27Date=request.POST['year27Date']
                                , year28Pay=request.POST['year28Pay']
                                           , year28Date=request.POST['year28Date']
                                , year29Pay=request.POST['year29Pay']
                                           , year29Date=request.POST['year29Date']
                                , year30Pay=request.POST['year30Pay']
                                           , year30Date=request.POST['year30Date']
                                
                                
                                            
                                             , BIRcgt=request.POST['cgt_amount']
                                           
                                           
                                           , BIRdst=request.POST['dst_amount']
                                           
                                           
                                           , LGUtransfer=request.POST['transferfees_amount']
                                           
                                           
                                           , RODlra=request.POST['lrafee_amount']
                                           
                                           
                                           , RODit=request.POST['itfee_amount']
                                            , OTHERSnotorial=request.POST['notarialfee_amount']
                                        ,numofyear=request.POST['numberofyears']
                                        ,totalContractPrice= 0000
                                        
                                        , area =request.POST['size']
                                , balance=request.POST['balance']
                                #not used
                                        , SUMother =0000
                                , TAXother =0000
                                ,dateRelease= "1111-11-11"

    
                           )
        property.save()
        return render(request, 'lease_form.html')
       
    return render(request, 'lease_form.html')

def salesregister(request):
    
    context = {}
    if 'addproperty' in request.POST:
                property =salesProperty(region=request.POST['region']
                                            , province=request.POST['province']
                                           
                                            , municipality=request.POST['municipality']
                                            , barangay=request.POST['barangay']
                                           
                                            ,regLandOwner=request.POST['registeredlandowner']
                                            , representative=request.POST['representative']
                                           
                                           , Address=request.POST['address']
                                           , contactNum=request.POST['contactnumber']
                                           
                                           , titleNum=request.POST['titlenumber']
                                           , lotNum=request.POST['lotnumber']
                                           
                                           
                                           , surveyNum=request.POST['surveynumber']
                                           
                                           ,pricePerHectare=request.POST['leasepriceperhectare']
                                           ,areaHectares=request.POST['size']
                                           , firstPayAmount=request.POST['1stpayment_amount']
                                           , firstPayDate=request.POST['1stpayment_date']
                                           
                                           , secPayAmount=request.POST['2ndpayment_amount']
                                           , secPayDate=request.POST['2ndpayment_date']
                                           
                                           , thirdPayAmount=request.POST['3rdpayment_amount']
                                           , thirdPayDate=request.POST['3rdpayment_date']
                                           
                                           , fourthPayAmount=request.POST['4thpayment_amount']
                                           , fourthPayDate=request.POST['4thpayment_date']
                                           
                                           
                                           , fifthPayAmount=request.POST['5thpayment_amount']
                                           , fifthPayDate=request.POST['5thpayment_date']
                                           
                                           , sixthPayAmount=request.POST['6thpayment_amount']
                                           , sixthPayDate=request.POST['6thpayment_date']
                                           
                                           , seventhPayAmount=request.POST['7thpayment_amount']
                                           , seventhPayDate=request.POST['7thpayment_date']
                                           
                                           , eigthPayAmount=request.POST['8thpayment_amount']
                                           , eigthPayDate=request.POST['8thpayment_date']
                                           
                                           , ninthPayAmount=request.POST['9thpayment_amount']
                                           , ninthPayDate=request.POST['9thpayment_date']
                                           
                                           , tenthPayAmount=request.POST['10thpayment_amount']
                                           , tenthPayDate=request.POST['10thpayment_date']
                                           
                                           , BIRcgt=request.POST['cgt_amount']
                                           
                                           
                                           , BIRdst=request.POST['dst_amount']
                                           
                                           
                                           , LGUtransfer=request.POST['transferfees_amount']
                                           
                                           
                                           , RODlra=request.POST['lrafee_amount']
                                           
                                           
                                           , RODit=request.POST['itfee_amount']
                                            , OTHERSnotorial=request.POST['notarialfee_amount']
                                           ,totalContractPrice= 0000
                                            , releasedPayment =0000
                                        , balance =0000
                                        , SUMother =0000
                                        , TAXother =0000
                                        , area =0000
                                           
                                           
                
                           )
                property.save()
                return render(request, 'sales_form.html')
       
    return render(request, 'sales_form.html')

def leaseedit(request):
    all_properties =leaseProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }
    return render(request, 'editlease-admin.html', context)

def salesedit(request):
    all_properties =salesProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }
    return render(request, 'editsales-admin.html', context)

def logout(request):
    if 'user' in request.session:
        del request.session['user']

    return render(request, 'login.html')

def ERROR(request):
    return render(request, 'ERROR.html')

