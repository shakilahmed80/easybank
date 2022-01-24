
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group, User, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from io import BytesIO
from django.template import Context, context

from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def home_view(request):
  return render(request,'Easy_bank_app/homebase.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request): 
    if is_customer(request.user):
        return render(request, 'Easy_bank_app/customer_home.html')
    else:
        return render(request, 'Easy_bank_app/admin_dashboard.html')



@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
   # customer=models.Customer.objects.all()
   # customercount=models.Customer.objects.all().count()
    customercount=models.Customer.objects.all().count()
    loancount = models.brac_car_loan_form1.objects.all().filter(status=True).count()
    

    mydict={
    'customercount':customercount,
    #'customer': customer,
    'loancount' : loancount
   # 'data':zip(ordered_products,ordered_bys,orders),
    }
    return render(request,'Easy_Bank_app/admin_dashboard.html',context=mydict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    return render(request,'Easy_bank_app/customer_home.html')
    
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers=models.Customer.objects.all()

    cont={
    'customers': customers, 
    }
    return render(request,'Easy_bank_app/view_customer.html',{cont:customers})


def customerclick_view(request):
    
    return render(request, 'Easy_bank_app/userlogin.html')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()     
    easy_bank_app={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    
    return render(request,'Easy_bank_app/usersignup.html',context=easy_bank_app)


def show_customer(request):
    customer=models.Customer.objects.all()

    context= {
        'customer': customer
    }

    return render(request, 'Easy_bank_app\cus_render.html', context)


def showdata(request): 
    results=models.Loan.objects.all()
    return render(request,'Easy_bank_app/loan.html',{"data": results})

def showdata_credit(request): 
    results=models.Credit_card.objects.all()
    return render(request,'Easy_bank_app/credit_card.html',{"data": results})


def slider_view(request):
    return render(request,'Easy_bank_app/slider.html')
 
def compare_view(request):
    return render(request,'Easy_bank_app/compare.html')

def compare_loan_view(request):
    return render(request, 'Easy_bank_app/allloan.html')

def credit_card_compare_view(request):
    return render(request, 'Easy_bank_app/compareandapply.html')

def contactus_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        message = '''
        New message : {}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['email'], message, '', ['easybank444@gmail.com'])
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            saverecord=models.Contactus()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.message=request.POST.get('message')
            saverecord.save()
        
            return render(request,'Easy_bank_app/contact_us_sent.html')
    else:
            return render(request,'Easy_bank_app/contact_us.html')

def brac_view(request):     
    return render(request,'Easy_bank_app/brac.html')

def view_feedback_view(request):
    feedbacks=models.Contactus.objects.all().order_by('-id')
    return render(request,'Easy_bank_app/contact_us_view.html',{'feedbacks':feedbacks})

def car_loan_view(request):
    return render(request,'Easy_bank_app/carloan1.html')

def education_loan_view(request):   
    return render(request, 'Easy_bank_app/educationloan.html')

def home_loan_view(request):   
    return render(request, 'Easy_bank_app/Home_loan.html')

def emi_calculator_view(request):    
    return render(request, 'Easy_bank_app/emi_calculator.html')

def personal_loan_view(request):   
    return render(request, 'Easy_bank_app/personal.html')

def startup_loan_view(request):   
    return render(request, 'Easy_bank_app/Startup.html')

def loan_ag_pro_view(request):   
    return render(request, 'Easy_bank_app/Loanagainstproperty.html')

def loan_calculator_view(request):   
    return render(request, 'Easy_bank_app/loancalculator.html')

#### VIEWS STARTED FOR APPLICATION FORM OF CAR LOAN

def city_bank_form_view(request):
    return render(request, 'Loan_form/carloan/city.html')

def dhaka_bank_form_view(request):
    return render(request, 'Loan_form/carloan/dhkbank.html')

def eastern_bank_form_view(request):
    return render(request, 'Loan_form/carloan/easternbank.html')

def grameen_bank_form_view(request):
    return render(request, 'Loan_form/carloan/grameenbank.html')

def habib_bank_form_view(request):
    return render(request, 'Loan_form/carloan/habibbank.html')

def hsbc_bank_form_view(request):
    return render(request, 'Loan_form/carloan/hsbcbank.html')

def jamuna_bank_form_view(request):
    return render(request, 'Loan_form/carloan/jamuna.html')

def janata_bank_form_view(request):
    return render(request, 'Loan_form/carloan/janata.html')

def mitb_bank_form_view(request):
    return render(request, 'Loan_form/carloan/mitb.html')

def one_bank_form_view(request):
    return render(request, 'Loan_form/carloan/one.html')

def prime_bank_form_view(request):
    return render(request, 'Loan_form/carloan/prime.html')

def sonali_bank_form_view(request):
    return render(request, 'Loan_form/carloan/sonali.html')

def standard_bank_form_view(request):
    return render(request, 'Loan_form/carloan/standard.html')

def ucb_bank_form_view(request):
    return render(request, 'Loan_form/carloan/ucb.html')

def uttara_bank_form_view(request):
    return render(request, 'Loan_form/carloan/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF CAR LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF EDUCATION LOAN
def brac_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/brac.html')

def city_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/city.html')

def dhaka_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/dhkbank.html')

def eastern_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/eastern.html')

def grameen_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/grameenbank.html')

def habib_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/habib.html')

def hsbc_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/hsbc.html')

def jamuna_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/jamuna.html')

def janata_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/janata.html')

def mitb_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/mitb.html')

def one_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/one.html')

def prime_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/prime.html')

def dbbl_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/dbbl.html')

def standard_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/standard.html')

def ucb_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/ucb.html')

def uttara_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/uttara.html')
  
#### VIEWS ENDED FOR APPLICATION FORM OF EDUCATION LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF HOME LOAN

def brac_bank_home_form_view(request):
     return render(request, 'Loan_form/homeloan/brac.html')

def city_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/city.html')

def dbbl_home_form_view(request):
    return render(request, 'Loan_form/homeloan/dbbl.html')

def dhaka_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/dhkbank.html')

def eastern_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/eastern.html')

def grameen_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/grameenbank.html')

def habib_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/habib.html')

def hsbc_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/hsbc.html')

def jamuna_bank_home_form_view(request):
    return render(request, 'Loan_formhomeloan/jamuna.html')

def janata_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/janata.html')

def mitb_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/mitb.html')

def one_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/one.html')

def prime_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/prime.html')

def sonali_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/sonali.html')

def standard_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/standard.html')

def ucb_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/ucb.html')

def uttara_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF HOME LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY

def brac_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/brac.html')

def city_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/city.html')

def dbbl_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/dbbl.html')

def dhaka_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/dhkbank.html')

def eastern_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/eastern.html')

def grameen_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/grameenbank.html')

def habib_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/habib.html')

def hsbc_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/hsbc.html')

def jamuna_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/jamuna.html')

def janata_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/janata.html')

def mitb_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/mitb.html')

def one_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/one.html')

def prime_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/prime.html')

def sonali_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/sonali.html')

def standard_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/standard.html')

def ucb_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/ucb.html')

def uttara_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF LOAN AGAIST PROPERTY

def homeloaneligibility_view(request):
    return render(request, 'Eligibility_Form/homeloan.html')

def homeloaneligibility2_view(request):
    return render(request, 'Eligibility_Form/homeloan_2.html')

def carloaneligibility_view(request):
    return render(request, 'Eligibility_Form/carloan.html')

def carloaneligibility2_view(request):
    return render(request, 'Eligibility_Form/carloan_2.html')

def educationloaneligibility_view(request):
    return render(request, 'Eligibility_Form/educationloan.html')

def educationloaneligibility2_view(request):
    return render(request, 'Eligibility_Form/educationloan_2.html')   

def personalloaneligibility_view(request):
    return render(request, 'Eligibility_Form/personalloan.html')

def personalloaneligibility2_view(request):
    return render(request, 'Eligibility_Form/personalloan_2.html')

def startuploaneligibility_view(request):
    return render(request, 'Eligibility_Form/startuploan.html')

def startuploaneligibility2_view(request):
    return render(request, 'Eligibility_Form/startuploan_2.html')

def loanagainstpropertyeligibility_view(request):
     return render(request, 'Eligibility_Form/loanagainst.html')

def loanagainstpropertyeligibility2_view(request):
     return render(request, 'Eligibility_Form/loanagainst_2.html')

def credit_card_view(request):
    return render(request,'Easy_bank_app/credit_card.html')


def brac_home_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_home_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/brachf2')
            
    else:
         return render(request, 'brac_bank_home_loan/h1.html')

def brac_home_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_home_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/brachf3')
    
    else:
         return render(request, 'brac_bank_home_loan/h2.html')
    
def brac_home_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.brac_home_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility =request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/brachf4')

    else:
        return render(request,'brac_bank_home_loan/h3.html')

def brac_home_loan_4(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):

            saverecord=models.brac_home_loan_form4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/brachf5')
            
    else:
         return render(request, 'brac_bank_home_loan/h4.html')

def brac_home_loan_5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_home_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/brachf1')
            
    else:
         return render(request, 'brac_bank_home_loan/h5.html')      


def show_contacts(request):
    contacts=models.Contactus.objects.all()

    context= {
        'contacts':contacts
    }

    return render(request, 'Easy_bank_app/showinfo.html', context)


def show_brac_home_loan_form(request):
    brac_home_loan1=models.brac_home_loan_form1.objects.all()
    brac_home_loan2=models.brac_home_loan_form2.objects.all()
    brac_home_loan3=models.brac_home_loan_form3.objects.all()
    brac_home_loan4=models.brac_home_loan_form4.objects.all()
    brac_home_loan5=models.brac_home_loan_form5.objects.all()

    context= {
        'brac_home_loan1':brac_home_loan1,
        'brac_home_loan2':brac_home_loan2,
        'brac_home_loan3':brac_home_loan3,
        'brac_home_loan4':brac_home_loan4,
        'brac_home_loan5':brac_home_loan5
    }

    return render(request, 'All_home_loan/brac_bank_home.html', context)



def pdf_report_create2(request):
    brac_home_loan1=models.brac_home_loan_form1.objects.all()
    brac_home_loan2=models.brac_home_loan_form2.objects.all()
    brac_home_loan3=models.brac_home_loan_form3.objects.all()
    brac_home_loan4=models.brac_home_loan_form4.objects.all()
    brac_home_loan5=models.brac_home_loan_form5.objects.all()
  

    template_path = 'All_home_loan/brac_bank_home_loan_pdf.html'

    context= {
        'brac_home_loan1':brac_home_loan1,
        'brac_home_loan2':brac_home_loan2,
        'brac_home_loan3':brac_home_loan3,
        'brac_home_loan4':brac_home_loan4,
        'brac_home_loan5':brac_home_loan5
    
    }

def pdf_report_create4(request):
    city_car_loan1=models.city_car_loan_form1.objects.all()
    city_car_loan2=models.city_car_loan_form2.objects.all()
    city_car_loan3=models.city_car_loan_form3.objects.all()
    city_car_loan4=models.city_car_loan_form4.objects.all()
    city_car_loan5=models.city_car_loan_form5.objects.all()
  

    template_path = 'All_home_loan/city_bank_car_loan_pdf.html'

    context= {
        'city_car_loan1': city_car_loan1,
        'city_car_loan2': city_car_loan2,
        'city_car_loan3': city_car_loan3,
        'city_car_loan4': city_car_loan4,
        'city_car_loan5': city_car_loan5
    
    }
    

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="car_loan_application.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def pdf_report_create(request):
    contacts=models.Contactus.objects.all()

    template_path = 'Easy_bank_app/contactpdf.html'

    context = {'contacts': contacts}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactus_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
   # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#def brac_edu_loan_view(request):
#    return render(request, 'brac_edu_loan/h1.html')


def brac_car_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_car_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/braccl2')
            
    else:
         return render(request, 'brac_car_loan/h1.html')

def brac_car_loan_2(request):
    if request.method=='POST':
        if request.POST.get('present_address') and request.POST.get('permanent_address') and request.POST.get('postal_code') and request.POST.get('mobile') and request.POST.get('second_email') :

            saverecord=models.brac_car_loan_form2()
            saverecord.present_address=request.POST.get('present_address')
            saverecord.permanent_address=request.POST.get('permanent_address')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.mobile=request.POST.get('mobile')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/braccl3')
    
    else:
         return render(request, 'brac_car_loan/h2.html')
    
def brac_car_loan_3(request):
    if request.method=='POST':
        if request.POST.get('model') and request.POST.get('year') and request.POST.get('cc_type') and request.POST.get('manufacturing_year') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.brac_car_loan_form3()
            save.model =request.POST.get('model')
            save.year =request.POST.get('year')
            save.cc_type =request.POST.get('cc_type')
            save.manufacturing_year=request.POST.get('manufacturing_year')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/braccl4')

    else:
        return render(request,'brac_car_loan/h3.html')

def brac_car_loan_4(request):
    if request.method=='POST':
        if request.POST.get('total_amount') and request.POST.get('reffered_amount') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.brac_car_loan_form4()
            saverecord.total_amount=request.POST.get('total_amount')
            saverecord.reffered_amount=request.POST.get('reffered_amount')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/braccl5')
            
    else:
        return render(request, 'brac_car_loan/h4.html')

def brac_car_loan_5(request):
    if request.method=='POST':
        if request.POST.get('own_house') and request.POST.get('total_monthly_expenses') and request.POST.get('home_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_car_loan_form5()
            saverecord.own_house=request.POST.get('own_house')
            saverecord.total_monthly_expenses=request.POST.get('total_monthly_expenses')
            saverecord.home_address=request.POST.get('home_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/braccl1')
            
    else:
         return render(request, 'brac_car_loan/h5.html')      

def brac_loan_against_property_view1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_loan_against_property_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/braclap2')
            
    else:
         return render(request, 'brac_loanagainstproperty/h1.html')

def brac_loan_against_property_view2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_loan_against_property_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/braclap3')
    
    else:
         return render(request, 'brac_loanagainstproperty/h2.html')
    
def brac_loan_against_property_view3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.brac_loan_against_property_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility=request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/braclap4')

    else:
        return render(request,'brac_loanagainstproperty/h3.html')

def brac_loan_against_property_view4(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('other_expenses') and request.POST.get('dues') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.brac_loan_against_property_form4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.other_expenses=request.POST.get('other_expenses')
            saverecord.dues=request.POST.get('dues')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/braclap5')
            
    else:
        return render(request, 'brac_loanagainstproperty/h4.html')

def brac_loan_against_property_view5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_loan_against_property_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/braclap1')
            
    else:
         return render(request, 'brac_loanagainstproperty/h5.html')     

def brac_edu_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_education_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/braced2')
            
    else:
         return render(request, 'brac_edu_loan/h1.html')

def brac_edu_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_education_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/braced3')
    
    else:
         return render(request, 'brac_edu_loan/h2.html')
    
def brac_edu_loan_3(request):
    if request.method=='POST':
        if request.POST.get('course_name') and request.POST.get('total_duration') and request.POST.get('date_of_complete') and request.POST.get('nationality_2') and request.POST.get('yearly_expenses'):
            save=models.brac_education_loan_form3()
            save.course_name =request.POST.get('course_name')
            save.total_duration =request.POST.get('total_duration')
            save.date_of_complete =request.POST.get('date_of_complete')
            save.nationality_2=request.POST.get('nationality_2')
            save.yearly_expenses =request.POST.get('yearly_expenses')
            save.save()
            return HttpResponseRedirect('/braced4')

    else:
        return render(request,'brac_edu_loan/h3.html')

def brac_edu_loan_4(request):
    if request.method=='POST':
        if request.POST.get('tution_fees') and request.POST.get('exam_fees') and request.POST.get('book_expense') and request.POST.get('scholarship') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.brac_education_loan_form4()
            saverecord.tution_fees=request.POST.get('tution_fees')
            saverecord.exam_fees=request.POST.get('exam_fees')
            saverecord.book_expense=request.POST.get('book_expense')
            saverecord.scholarship=request.POST.get('scholarship')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/braced5')
            
    else:
        return render(request, 'brac_edu_loan/h4.html')

def brac_edu_loan_5(request):
    if request.method=='POST':
        if request.POST.get('ssc_gpa') and request.POST.get('school') and request.POST.get('hsc_gpa') and request.POST.get('college') and request.POST.get('other_qualification') :

            saverecord=models.brac_education_loan_form5()
            saverecord.ssc_gpa=request.POST.get('ssc_gpa')
            saverecord.school=request.POST.get('school')
            saverecord.hsc_gpa=request.POST.get('hsc_gpa')
            saverecord.college=request.POST.get('college')
            saverecord.other_qualification=request.POST.get('other_qualification')
            saverecord.save()
            return HttpResponseRedirect('/braced1')
            
    else:
         return render(request, 'brac_edu_loan/h5.html')      

def brac_personal_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_personal_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/bracpl2')
            
    else:
         return render(request, 'brac_personal_loan/h1.html')

def brac_personal_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_personal_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/bracpl3')
    
    else:
         return render(request, 'brac_personal_loan/h2.html')
    
def brac_personal_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('no_of_property') and request.POST.get('property_details') and request.POST.get('others') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.brac_personal_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.no_of_property =request.POST.get('no_of_property')
            save.property_details =request.POST.get('property_details')
            save.others=request.POST.get('others')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/bracpl4')

    else:
        return render(request,'brac_personal_loan/h3.html')

def brac_personal_loan_4(request):
    if request.method=='POST':
        if request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.brac_personal_loan_form4()
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/bracpl5')
            
    else:
        return render(request, 'brac_personal_loan/h4.html')

def brac_personal_loan_5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_personal_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/bracpl1')
            
    else:
         return render(request, 'brac_personal_loan/h5.html')   

def brac_startup_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_startup_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/bracsl2')
            
    else:
         return render(request, 'brac_startup_loan/h1.html')

def brac_startup_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_startup_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/bracsl3')
    
    else:
         return render(request, 'brac_startup_loan/h2.html')
    
def brac_startup_loan_3(request):
    if request.method=='POST':
        if request.POST.get('startup_type') and request.POST.get('idea_type') and request.POST.get('loan_tenure_time') and request.POST.get('utility') and request.POST.get('expected_possesion') :
            save=models.brac_startup_loan_form3()
            save.startup_type =request.POST.get('startup_type')
            save.idea_type =request.POST.get('idea_type')
            save.loan_tenure_time =request.POST.get('loan_tenure_time')
            save.utility=request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.save()
            return HttpResponseRedirect('/bracsl4')

    else:
        return render(request,'brac_startup_loan/h3.html')

def brac_startup_loan_4(request):
    if request.method=='POST':
        if request.POST.get('loan_amount') and request.POST.get('loan_in_word') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.brac_startup_loan_form4()
            saverecord.loan_amount=request.POST.get('loan_amount')
            saverecord.loan_in_word=request.POST.get('loan_in_word')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/bracsl5')
            
    else:
        return render(request, 'brac_startup_loan/h4.html')

def brac_startup_loan_5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_startup_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/bracsl1')
            
    else:
         return render(request, 'brac_startup_loan/h5.html')

def brac_credit_card_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('credit_card_type') :

            saverecord=models.brac_credit_card_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.credit_card_type=request.POST.get('credit_card_type')
            saverecord.save()
            return HttpResponseRedirect('/braccc2')
            
    else:
         return render(request, 'brac_creditcard/h1.html')

def brac_credit_card_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_credit_card_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/braccc3')
    
    else:
         return render(request, 'brac_creditcard/h2.html')
    
def brac_credit_card_3(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_credit_card_form3()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/braccc4')

    else:
        return render(request,'brac_creditcard/h3.html')

def brac_credit_card_4(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('credit_card_type') :

            saverecord=models.brac_credit_card_form4()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.credit_card_type=request.POST.get('credit_card_type')
            saverecord.save()
            return HttpResponseRedirect('/braccc5')
            
    else:
        return render(request, 'brac_creditcard/h4.html')

def brac_credit_card_5(request):
    if request.method=='POST':
        if request.POST.get('account_no') and request.POST.get('account_type') and request.POST.get('balance_amount') and request.POST.get('contact_no_2') and request.POST.get('email') :

            saverecord=models.brac_credit_card_form5()
            saverecord.account_no=request.POST.get('account_no')
            saverecord.account_type=request.POST.get('account_type')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.contact_no_2=request.POST.get('contact_no_2')
            saverecord.email=request.POST.get('email')
            saverecord.save()
            return HttpResponseRedirect('/braccc1')
            
    else:
         return render(request, 'brac_creditcard/h5.html')
        
def city_credit_card_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('credit_card_type') :

            saverecord=models.city_credit_card_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.credit_card_type=request.POST.get('credit_card_type')
            saverecord.save()
            return HttpResponseRedirect('/citycc2')
            
    else:
         return render(request, 'citybank_creditcard/h1.html')

def city_credit_card_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_credit_card_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/citycc3')
    
    else:
         return render(request, 'citybank_creditcard/h2.html')
    
def city_credit_card_3(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_credit_card_form3()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/citycc4')

    else:
        return render(request,'citybank_creditcard/h3.html')

def city_credit_card_4(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('credit_card_type') :

            saverecord=models.city_credit_card_form4()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.credit_card_type=request.POST.get('credit_card_type')
            saverecord.save()
            return HttpResponseRedirect('/citycc5')
            
    else:
        return render(request, 'citybank_creditcard/h4.html')

def city_credit_card_5(request): 
    if request.method=='POST':
        if request.POST.get('account_no') and request.POST.get('account_type') and request.POST.get('balance_amount') and request.POST.get('contact_no_2') and request.POST.get('email') :

            saverecord=models.city_credit_card_form5()
            saverecord.account_no=request.POST.get('account_no')
            saverecord.account_type=request.POST.get('account_type')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.contact_no_2=request.POST.get('contact_no_2')
            saverecord.email=request.POST.get('email')
            saverecord.save()
            return HttpResponseRedirect('/citycc1')
            
    else:
         return render(request, 'citybank_creditcard/h5.html')

def city_home_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_home_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/cityhf2')
            
    else:
         return render(request, 'city_bank_home_loan/h1.html')

def city_home_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_home_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/cityhf3')
    
    else:
         return render(request, 'city_bank_home_loan/h2.html')
    
def city_home_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.city_home_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility =request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/cityhf4')

    else:
        return render(request,'city_bank_home_loan/h3.html')

def city_home_loan_4(request):
    if request.method=='POST':
        if request.POST.get('zip_code') and request.POST.get('neutral_landmark') and request.POST.get('city_code') and request.POST.get('area_code') and request.POST.get('contact_2') and request.POST.get('email_3'):

            saverecord=models.city_home_loan_form4()
            saverecord.zip_code=request.POST.get('zip_code')
            saverecord.neutral_landmark=request.POST.get('neutral_landmark')
            saverecord.city_code=request.POST.get('city_code')
            saverecord.area_code=request.POST.get('area_code')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/cityhf5')
            
    else:
         return render(request, 'city_bank_home_loan/h4.html')

def city_home_loan_5(request): 
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_home_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/cityhf1')
            
    else:
         return render(request, 'city_bank_home_loan/h5.html')    

def city_car_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_car_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/citycl2')
            
    else:
         return render(request, 'city_car_loan/h1.html')

def city_car_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_car_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/citycl3')
    
    else:
         return render(request, 'city_car_loan/h2.html')
    
def city_car_loan_3(request):
    if request.method=='POST':
        if request.POST.get('amount_of_loan') and request.POST.get('loan_in_word') and request.POST.get('no_of_month_to_close') and request.POST.get('nationality_2') and request.POST.get('area') and request.POST.get('date_expected'):
            save=models.city_car_loan_form3()
            save.amount_of_loan =request.POST.get('amount_of_loan')
            save.loan_in_word =request.POST.get('loan_in_word')
            save.no_of_month_to_close =request.POST.get('no_of_month_to_close')
            save.nationality_2=request.POST.get('nationality_2')
            save.area =request.POST.get('area')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/citycl4')

    else:
        return render(request,'city_car_loan/h3.html')

def city_car_loan_4(request):
    if request.method=='POST':
        if request.POST.get('car_model') and request.POST.get('manufacturing_year') and request.POST.get('loan_percentage') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.city_car_loan_form4()
            saverecord.car_model=request.POST.get('car_model')
            saverecord.manufacturing_year=request.POST.get('manufacturing_year')
            saverecord.loan_percentage=request.POST.get('loan_percentage')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/citycl5')
            
    else:
        return render(request, 'city_car_loan/h4.html')

def city_car_loan_5(request): 
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_car_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/citycl1')
            
    else:
         return render(request, 'city_car_loan/h5.html')   

def city_edu_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_education_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/cityed2')
            
    else:
         return render(request, 'city_edu_loan/h1.html')

def city_edu_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_education_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/cityed3')
    
    else:
         return render(request, 'city_edu_loan/h2.html')
    
def city_edu_loan_3(request):
    if request.method=='POST':
        if request.POST.get('ssc_result') and request.POST.get('hsc_result') and request.POST.get('ielts_result') and request.POST.get('extracuricular_activity') and request.POST.get('utility'):
            save=models.city_education_loan_form3()
            save.ssc_result =request.POST.get('ssc_result')
            save.hsc_result =request.POST.get('hsc_result')
            save.ielts_result =request.POST.get('ielts_result')
            save.extracuricular_activity=request.POST.get('extracuricular_activity')
            save.utility =request.POST.get('utility')
            save.save()
            return HttpResponseRedirect('/cityed4')

    else:
        return render(request,'city_edu_loan/h3.html')

def city_edu_loan_4(request):
    if request.method=='POST':
        if request.POST.get('amount_of_loan') and request.POST.get('amount_of_loan_in_word') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.city_education_loan_form4()
            saverecord.amount_of_loan=request.POST.get('amount_of_loan')
            saverecord.amount_of_loan_in_word=request.POST.get('amount_of_loan_in_word')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/cityed5')
            
    else:
        return render(request, 'city_edu_loan/h4.html')

def city_edu_loan_5(request): 
    if request.method=='POST':
        if request.POST.get('institute_name') and request.POST.get('loan_duration') and request.POST.get('institution_address') and request.POST.get('allowness') and request.POST.get('scholarship') and request.POST.get('scholarship_in_words') and request.POST.get('office_no') :

            saverecord=models.city_education_loan_form5()
            saverecord.institute_name=request.POST.get('institute_name')
            saverecord.loan_duration=request.POST.get('loan_duration')
            saverecord.institution_address=request.POST.get('institution_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.scholarship=request.POST.get('scholarship')
            saverecord.scholarship_in_words=request.POST.get('scholarship_in_words')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/cityed1')
            
    else:
         return render(request, 'city_edu_loan/h5.html')  

def city_personal_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_personal_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/citypl2')
            
    else:
         return render(request, 'city_personal_loan/h1.html')

def city_personal_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_personal_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/citypl3')
    
    else:
         return render(request, 'city_personal_loan/h2.html')
    
def city_personal_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.city_personal_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality=request.POST.get('nationality')
            save.utility=request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/citypl4')

    else:
        return render(request,'city_personal_loan/h3.html')

def city_personal_loan_4(request):
    if request.method=='POST':
        if request.POST.get('amount_of_loan') and request.POST.get('loan_in_word') and request.POST.get('balance_amount') and request.POST.get('due_time') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.city_personal_loan_form4()
            saverecord.amount_of_loan=request.POST.get('amount_of_loan')
            saverecord.loan_in_word=request.POST.get('loan_in_word')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.due_time=request.POST.get('due_time')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/citypl5')
            
    else:
        return render(request, 'city_personal_loan/h4.html')

def city_personal_loan_5(request): 
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_personal_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/citypl1')
            
    else:
         return render(request, 'city_personal_loan/h5.html')

def city_loan_against_property_view1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_loan_against_property_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/citylap2')
            
    else:
         return render(request, 'city_loanagainstproperty/h1.html')

def city_loan_against_property_view2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_loan_against_property_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/citylap3')
    
    else:
         return render(request, 'city_loanagainstproperty/h2.html')
    
def city_loan_against_property_view3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.city_loan_against_property_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility=request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/citylap4')

    else:
        return render(request,'city_loanagainstproperty/h3.html')

def city_loan_against_property_view4(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.city_loan_against_property_form4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/citylap5')
            
    else:
        return render(request, 'city_loanagainstproperty/h4.html')

def city_loan_against_property_view5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_loan_against_property_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/citylap1')
            
    else:
         return render(request, 'city_loanagainstproperty/h5.html')  
        
def city_startup_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.city_startup_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('/citysl2')
            
    else:
         return render(request, 'city_startup_loan/h1.html')

def city_startup_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.city_startup_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('/citysl3')
    
    else:
         return render(request, 'city_startup_loan/h2.html')
    
def city_startup_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected') :
            save=models.city_startup_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility=request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected=request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('/citysl4')

    else:
        return render(request,'city_startup_loan/h3.html')

def city_startup_loan_4(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):
            
            saverecord=models.city_startup_loan_form4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('/citysl5')
            
    else:
        return render(request, 'city_startup_loan/h4.html')

def city_startup_loan_5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.city_startup_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('/citysl1')
            
    else:
         return render(request, 'city_startup_loan/h5.html')