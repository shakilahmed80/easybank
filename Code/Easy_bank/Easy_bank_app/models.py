
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import  EmailField
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
class Loan(models.Model):
  
    types_of_loan = models.CharField(max_length=40, null=False)
    bank_name= models.CharField(max_length=70, null=False)
    interest_rate = models.CharField(max_length=30,null=False)
    processing_fee_range = models.CharField(max_length=40)
    loan_amount= models.CharField(max_length=50, null=False)
    tenure_range= models.CharField(max_length=70, null=False)
    class meta: 
        db_table="Easy_bank_app_loan"
    
class Credit_card(models.Model):
 
    bank_name = models.CharField(max_length=50, null=False)
    card_type= models.CharField(max_length=50, null=False)
    first_year_fee= models.CharField(max_length=50, null=False)
    rewards= models.CharField(max_length=50, null=False)
    joining_perks= models.CharField(max_length=50, null=False)
    class meta: 
        db_table="Easy_bank_app_credit_card"

class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=11)
    message=models.CharField(max_length=500)
    class meta:
        db_table="Easy_bank_app_contact_us"

class Carloaneligibility(models.Model):
    bangladeshi = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    age	= models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    net_income = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class meta:
        db_table="easy_bank_app_car_loan_eligibility"


class hloanform(models.Model): 
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_hloanform"

class hloanform2(models.Model): 
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_hloanform2"


class hloanform3(models.Model): 
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_hloanform3"

class hloanform4(models.Model): 
    home_area=models.CharField(max_length=100)
    loan_requested= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_hloanform4"

class hloanform5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_hloanform5"
    
class brac_home_loan_form1(models.Model): 
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_home_loan_form1"

class brac_home_loan_form2(models.Model): 
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_home_loan_form2"


class brac_home_loan_form3(models.Model): 
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_home_loan_form3"

class brac_home_loan_form4(models.Model): 
    home_area=models.CharField(max_length=100)
    loan_requested= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_home_loan_form4"

class brac_home_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_home_loan_form5"

class brac_loan_against_property_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_loan_against_property_form1"

class brac_loan_against_property_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_loan_against_property_form2"

class brac_loan_against_property_form3(models.Model):
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_loan_against_property_form3"

class brac_loan_against_property_form4(models.Model):
    home_area=models.CharField(max_length=100)
    other_expenses= models.CharField(max_length=100)
    dues= models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_loan_against_property_form4"

class brac_loan_against_property_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_loan_against_property_form5"

class brac_personal_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_personal_loan_form1"

class brac_personal_loan_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_personal_loan_form2"

class brac_personal_loan_form3(models.Model):
    property_type=models.CharField(max_length=100)
    no_of_property =models.CharField(max_length=100)
    property_details=models.CharField(max_length=100)
    others=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_personal_loan_form3"

class brac_personal_loan_form4(models.Model):
    loan_requested= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_personal_loan_form4"

class brac_personal_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_personal_loan_form5"

class brac_startup_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_startup_loan_form1"

class brac_startup_loan_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_startup_loan_form2"

class brac_startup_loan_form3(models.Model):
    startup_type=models.CharField(max_length=100)
    idea_type =models.CharField(max_length=100)
    loan_tenure_time=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_startup_loan_form3"

class brac_startup_loan_form4(models.Model):
    loan_amount=models.CharField(max_length=100)
    loan_in_word= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_startup_loan_form4"

class brac_startup_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_startup_loan_form5"

class brac_car_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_car_loan_form1"

class brac_car_loan_form2(models.Model):
    present_address= models.CharField(max_length=200)
    permanent_address= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    mobile= models.CharField(max_length=11)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_car_loan_form2"

class brac_car_loan_form3(models.Model):
    model= models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    cc_type =models.CharField(max_length=100)
    manufacturing_year=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_car_loan_form3"

class brac_car_loan_form4(models.Model):
    total_amount=models.CharField(max_length=100)
    reffered_amount= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_car_loan_form4"

class brac_car_loan_form5(models.Model): 
    own_house= models.CharField(max_length=100)
    total_monthly_expenses= models.CharField(max_length=100)
    home_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_car_loan_form5"

class brac_education_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_education_loan_form1"

class brac_education_loan_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_education_loan_form2"

class brac_education_loan_form3(models.Model):
    course_name=models.CharField(max_length=100)
    total_duration =models.CharField(max_length=100)
    date_of_complete=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    yearly_expenses=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_education_loan_form3"

class brac_education_loan_form4(models.Model):
    tution_fees=models.CharField(max_length=100)
    exam_fees= models.CharField(max_length=100)
    book_expense= models.CharField(max_length=100)
    scholarship= models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_education_loan_form4"

class brac_education_loan_form5(models.Model): 
    ssc_gpa= models.CharField(max_length=100)
    school= models.CharField(max_length=100)
    hsc_gpa= models.CharField(max_length=200)
    college= models.CharField(max_length=100,null=True)
    other_qualification= models.CharField(max_length=100,null=True)
    
    class meta:
        db_table="easy_bank_app_brac_education_loan_form5"

class city_credit_card_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    credit_card_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_credit_card_form1"


class city_credit_card_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_credit_card_form2"

class city_credit_card_form3(models.Model):
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form3"

class city_credit_card_form4(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    credit_card_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_credit_card_form4"

class city_credit_card_form5(models.Model): 
    account_no= models.CharField(max_length=100)
    account_type= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=200)
    contact_no_2= models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    
    class meta:
        db_table="easy_bank_app_city_credit_card_form5"

class brac_credit_card_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    credit_card_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form1"

class brac_credit_card_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form2"

class brac_credit_card_form3(models.Model):
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form3"

class brac_credit_card_form4(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    credit_card_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form4"

class brac_credit_card_form5(models.Model): 
    account_no= models.CharField(max_length=100)
    account_type= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=200)
    contact_no_2= models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    
    class meta:
        db_table="easy_bank_app_brac_credit_card_form5"


class city_home_loan_form1(models.Model): 
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_home_loan_form1"

class city_home_loan_form2(models.Model): 
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_home_loan_form2"


class city_home_loan_form3(models.Model): 
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_home_loan_form3"

class city_home_loan_form4(models.Model): 
    zip_code=models.CharField(max_length=100)
    neutral_landmark= models.CharField(max_length=100)
    city_code= models.CharField(max_length=100)
    area_code= models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_home_loan_form4"

class city_home_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_home_loan_form5"

class city_car_loan_form1(models.Model): 
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_car_loan_form1"

class city_car_loan_form2(models.Model): 
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_car_loan_form2"


class city_car_loan_form3(models.Model): 
    amount_of_loan=models.CharField(max_length=100)
    loan_in_word =models.CharField(max_length=100)
    no_of_month_to_close=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_car_loan_form3"

class city_car_loan_form4(models.Model): 
    car_model=models.CharField(max_length=100)
    manufacturing_year= models.CharField(max_length=100)
    loan_percentage= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_car_loan_form4"

class city_car_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_car_loan_form5"
    
class city_education_loan_form1(models.Model): 
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_education_loan_form1"

class city_education_loan_form2(models.Model): 
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_education_loan_form2"


class city_education_loan_form3(models.Model): 
    ssc_result=models.CharField(max_length=100)
    hsc_result =models.CharField(max_length=100)
    ielts_result=models.CharField(max_length=100)
    extracuricular_activity=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_education_loan_form3"

class city_education_loan_form4(models.Model): 
    amount_of_loan=models.CharField(max_length=100)
    amount_of_loan_in_word= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_education_loan_form4"

class city_education_loan_form5(models.Model): 
    institute_name= models.CharField(max_length=100)
    loan_duration= models.CharField(max_length=100)
    institution_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    scholarship= models.CharField(max_length=100,null=True)
    scholarship_in_words= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_education_loan_form5"

class city_loan_against_property_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_loan_against_property_form1"

class city_loan_against_property_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_loan_against_property_form2"

class city_loan_against_property_form3(models.Model):
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_loan_against_property_form3"

class city_loan_against_property_form4(models.Model):
    home_area=models.CharField(max_length=100)
    loan_requested= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_loan_against_property_form4"

class city_loan_against_property_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_loan_against_property_form5"

class city_startup_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_startup_loan_form1"

class city_startup_loan_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_startup_loan_form2"

class city_startup_loan_form3(models.Model):
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality_2=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_startup_loan_form3"

class city_startup_loan_form4(models.Model):
    home_area=models.CharField(max_length=100)
    loan_requested= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    payment_source= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_startup_loan_form4"

class city_startup_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_startup_loan_form5"
    
class city_personal_loan_form1(models.Model):
    applicants_name = models.CharField(max_length=250)
    applicants_full_name= models.CharField(max_length=200)
    applicants_father_name= models.CharField(max_length=200)
    applicants_mother_name= models.CharField(max_length=200)
    nationality= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contatct_no= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    loan_type= models.CharField(max_length=200)
    
    class meta:
        db_table="easy_bank_app_city_personal_loan_form1"

class city_personal_loan_form2(models.Model):
    full_address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    postal_code= models.CharField(max_length=100)
    p_address= models.CharField(max_length=200)
    second_contact_no= models.CharField(max_length=100)
    second_email= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_personal_loan_form2"

class city_personal_loan_form3(models.Model):
    property_type=models.CharField(max_length=100)
    floor_size =models.CharField(max_length=100)
    flat_no=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    expected_possesion=models.CharField(max_length=100)
    date_expected=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_personal_loan_form3"

class city_personal_loan_form4(models.Model):
    amount_of_loan= models.CharField(max_length=100)
    loan_in_word= models.CharField(max_length=100)
    balance_amount= models.CharField(max_length=100)
    due_time= models.CharField(max_length=100)
    property_selected=models.CharField(max_length=100)
    contact_2=models.CharField(max_length=100)
    email_3=models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_personal_loan_form4"

class city_personal_loan_form5(models.Model): 
    organisation_name= models.CharField(max_length=100)
    designation_department= models.CharField(max_length=100)
    office_address= models.CharField(max_length=200)
    allowness= models.CharField(max_length=100,null=True)
    additional_income= models.CharField(max_length=100,null=True)
    salary_total= models.CharField(max_length=100,null=True)
    office_no= models.CharField(max_length=100)
    
    class meta:
        db_table="easy_bank_app_city_personal_loan_form5"
