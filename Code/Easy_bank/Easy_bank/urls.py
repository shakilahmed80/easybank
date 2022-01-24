

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Easy_bank_app import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='Easy_bank_app/adminlogin.html')),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('customerclick', views.customerclick_view),
    path('customersignup', views.customer_signup_view),  
    path('customerlogin', LoginView.as_view(template_name='Easy_bank_app/userlogin.html'),name='customerlogin'), 
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('customer-home', views.customer_home_view,name='customer-home'), 
    path('logout', LogoutView.as_view(template_name='Easy_bank_app/logout.html'), name='logout'),
    path('homebase', LoginView.as_view(template_name='Easy_bank_app/homebase.html'), name='homebase'),
    path('loan/', views.showdata),
    path('slider/', views.slider_view),
    path('compareandapply/',views.compare_view),
    path('contactus/',views.contactus_view),
    path('brac/',views.brac_view),
    path('contactusview/', views.view_feedback_view),
    path('carloan/', views.car_loan_view),
    path('educationloan/', views.education_loan_view),
    path('homeloan/', views.home_loan_view),
    path('startuploan/', views.startup_loan_view),
    path('loanagainstproperty/', views.loan_ag_pro_view),
    path('personalloan/', views.personal_loan_view), 
    path('emicalculator/', views.emi_calculator_view),
    path('loancalculator/', views.loan_calculator_view),
    path('comparecreditcard/', views.credit_card_compare_view),
    path('compareloan/', views.compare_loan_view),
    path('Credit_card/', views.credit_card_view),
    #path('Insertcareligibility/', views.Insertcareligibility),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    ###  PATH FOR HOME LOAN ###
    path('homeloaneligibility/', views.homeloaneligibility_view ),

    ### BRAC BANK ###

    path('brachf1/', views.brac_home_loan_1, name='brachf1'),
    path('brachf2/', views.brac_home_loan_2, name='brachf2'),
    path('brachf3/', views.brac_home_loan_3, name='brachf3'),
    path('brachf4/', views.brac_home_loan_4, name='brachf4'),
    path('brachf5/', views.brac_home_loan_5, name='brachf5'),

    ### CITY BANK ###
    path('homeloaneligibility2/', views.homeloaneligibility2_view ),

    path('cityhf1/', views.city_home_loan_1, name='cityhf1'),
    path('cityhf2/', views.city_home_loan_2, name='cityhf2'),
    path('cityhf3/', views.city_home_loan_3, name='cityhf3'),
    path('cityhf4/', views.city_home_loan_4, name='cityhf4'),
    path('cityhf5/', views.city_home_loan_5, name='cityhf5'),


    ###  PATH FOR CAR LOAN ###
    path('carloaneligibility/', views.carloaneligibility_view),
  
    ### BRAC BANK ###

    path('braccl1/', views.brac_car_loan_1, name='braccl1'),
    path('braccl2/', views.brac_car_loan_2, name='braccl2'),
    path('braccl3/', views.brac_car_loan_3, name='braccl3'),
    path('braccl4/', views.brac_car_loan_4, name='braccl4'),
    path('braccl5/', views.brac_car_loan_5, name='braccl5'),

    ### CITY BANK ###  
    path('carloaneligibility2/', views.carloaneligibility2_view),

    path('citycl1/', views.city_car_loan_1, name='citycl1'),
    path('citycl2/', views.city_car_loan_2, name='citycl2'),
    path('citycl3/', views.city_car_loan_3, name='citycl3'),
    path('citycl4/', views.city_car_loan_4, name='citycl4'),
    path('citycl5/', views.city_car_loan_5, name='citycl5'),


    ###  PATH FOR LOAN AGAINST PROPERTY ###
    path('loanagainsteligibility/', views.loanagainstpropertyeligibility_view),
  
    ### BRAC BANK ###

    path('braclap1/', views.brac_loan_against_property_view1, name='braclap1'),
    path('braclap2/', views.brac_loan_against_property_view2, name='braclap2'),
    path('braclap3/', views.brac_loan_against_property_view3, name='braclap3'),
    path('braclap4/', views.brac_loan_against_property_view4, name='braclap4'),
    path('braclap5/', views.brac_loan_against_property_view5, name='braclap5'),

    ### CITY BANK ###
    path('loanagainsteligibility2/', views.loanagainstpropertyeligibility2_view),

    path('citylap1/', views.city_loan_against_property_view1, name='citylap1'),
    path('citylap2/', views.city_loan_against_property_view2, name='citylap2'),
    path('citylap3/', views.city_loan_against_property_view3, name='citylap3'),
    path('citylap4/', views.city_loan_against_property_view4, name='citylap4'),
    path('citylap5/', views.city_loan_against_property_view5, name='citylap5'),

    ###  PATH FOR EDUCATION LOAN ###
    path('educationloaneligibility/', views.educationloaneligibility_view ),

    ### BRAC BANK ###

    path('braced1/', views.brac_edu_loan_1, name='braced1'),
    path('braced2/', views.brac_edu_loan_2, name='braced2'),
    path('braced3/', views.brac_edu_loan_3, name='braced3'),
    path('braced4/', views.brac_edu_loan_4, name='braced4'),
    path('braced5/', views.brac_edu_loan_5, name='braced5'),

    ### CITY BANK ###
    path('educationloaneligibility2/', views.educationloaneligibility2_view ),

    path('cityed1/', views.city_edu_loan_1, name='cityed1'),
    path('cityed2/', views.city_edu_loan_2, name='cityed2'),
    path('cityed3/', views.city_edu_loan_3, name='cityed3'),
    path('cityed4/', views.city_edu_loan_4, name='cityed4'),
    path('cityed5/', views.city_edu_loan_5, name='cityed5'),


    ###  PATH FOR PERSONAL LOAN ###

    path('personalloaneligibility/', views.personalloaneligibility_view),

    ### BRAC BANK ###

    path('bracpl1/', views.brac_personal_loan_1, name='bracpl1'),
    path('bracpl2/', views.brac_personal_loan_2, name='bracpl2'),
    path('bracpl3/', views.brac_personal_loan_3, name='bracpl3'),
    path('bracpl4/', views.brac_personal_loan_4, name='bracpl4'),
    path('bracpl5/', views.brac_personal_loan_5, name='bracpl5'),
    
    ### CITY BANK ###
    path('personalloaneligibility2/', views.personalloaneligibility2_view),

    path('citypl1/', views.city_personal_loan_1, name='citypl1'),
    path('citypl2/', views.city_personal_loan_2, name='citypl2'),
    path('citypl3/', views.city_personal_loan_3, name='citypl3'),
    path('citypl4/', views.city_personal_loan_4, name='citypl4'),
    path('citypl5/', views.city_personal_loan_5, name='citypl5'),
    

    ###  PATH FOR STARTUP LOAN ###

    path('startuploaneligibility/', views.startuploaneligibility_view),

    ### BRAC BANK ###

    path('bracsl1/', views.brac_startup_loan_1, name='bracsl1'),
    path('bracsl2/', views.brac_startup_loan_2, name='bracsl2'),
    path('bracsl3/', views.brac_startup_loan_3, name='bracsl3'),
    path('bracsl4/', views.brac_startup_loan_4, name='bracsl4'),
    path('bracsl5/', views.brac_startup_loan_5, name='bracsl5'),

    ### BRAC BANK ###
    path('startuploaneligibility2/', views.startuploaneligibility2_view),

    path('citysl1/', views.city_startup_loan_1, name='citysl1'),
    path('citysl2/', views.city_startup_loan_2, name='citysl2'),
    path('citysl3/', views.city_startup_loan_3, name='citysl3'),
    path('citysl4/', views.city_startup_loan_4, name='citysl4'),
    path('citysl5/', views.city_startup_loan_5, name='citysl5'),



    ###  PATH FOR CREDIT CARD ###
    
    ### BRAC BANK ###
    path('braccc1/', views.brac_credit_card_1, name='braccc1'),
    path('braccc2/', views.brac_credit_card_2, name='braccc2'),
    path('braccc3/', views.brac_credit_card_3, name='braccc3'),
    path('braccc4/', views.brac_credit_card_4, name='braccc4'),
    path('braccc5/', views.brac_credit_card_5, name='braccc5'),

    ### CITY BANK ###
    path('citycc1/', views.city_credit_card_1, name='citycc1'),
    path('citycc2/', views.city_credit_card_2, name='citycc2'),
    path('citycc3/', views.city_credit_card_3, name='citycc3'),
    path('citycc4/', views.city_credit_card_4, name='citycc4'),
    path('citycc5/', views.city_credit_card_5, name='citycc5'),


    path('showcontacts', views.show_contacts, name='showcontacts'),
    path('createpdf',views.pdf_report_create, name='createpdf'),
    path('showcus', views.show_customer, name='showcus'),
    #path('testhloan', views.testhloan_view, name='testhloan'),
    #path('hform1', views.homeloan_one_view, name='hform1'),
    #path('hform2', views.homeloan_two_view, name='hform2'),
    #path('hform3', views.formthreedata, name='hform3'),
    #path('hform4', views.homeloan_four_view, name='hform4'),
    #path('hform5', views.homeloan_five_view, name='hform5'),
    #path('brachf1', views.brac_home_loan_1, name='brachf1'),
    #path('brachf2', views.brac_home_loan_2, name='brachf2'),
    #path('brachf3', views.brac_home_loan_3, name='brachf3'),
    #path('brachf4', views.brac_home_loan_4, name='brachf4'),
    #path('brachf5', views.brac_home_loan_5, name='brachf5'),

    #path('brac_edu_loan', views.brac_edu_loan_view, name='brac_edu_loan'),

    path('showform', views.show_brac_home_loan_form, name='showform'),
    path('createpdf2',views.pdf_report_create2, name='createpdf2'),
    path('createpdf4',views.pdf_report_create4, name='createpdf4'),
   


    #### URL PATH STARTED FOR APPLICATION FORM OF CAR LOAN
    
    path('citybank/', views.city_bank_form_view),
    path('dhakabank/', views.dhaka_bank_form_view),
    path('easternbank/', views.eastern_bank_form_view),
    path('grameenbank/', views.grameen_bank_form_view),
    path('habibbank/', views.habib_bank_form_view),
    path('hsbcbank/', views.hsbc_bank_form_view),
    path('jamunabank/', views.jamuna_bank_form_view),
    path('janatabank/', views.janata_bank_form_view),
    path('mitbbank/', views.mitb_bank_form_view),
    path('onebank/', views.one_bank_form_view),
    path('primebank/', views.prime_bank_form_view),
    path('sonalibank/', views.sonali_bank_form_view),
    path('standardbank/', views.standard_bank_form_view),
    path('ucbbank/', views.ucb_bank_form_view),
    path('uttarabank/', views.uttara_bank_form_view),

    #### URL PATH ENDED FOR APPLICATION FORM OF CAR LOAN
  

    #### URL PATH STARTED FOR APPLICATION FORM OF EDUCATION LOAN

   # path('bracbankedu/', views.brac_bank_edu_form_view),
    #path('citybankedu/', views.city_bank_edu_form_view),
    #path('dhakabankedu/', views.dhaka_bank_edu_form_view),
    #path('easternbankedu/', views.eastern_bank_edu_form_view),
    #path('grameenbankedu/', views.grameen_bank_edu_form_view),
    #path('habibbankedu/', views.habib_bank_edu_form_view),
   # path('hsbcbankedu/', views.hsbc_bank_edu_form_view),
   # path('jamunabankedu/', views.jamuna_bank_edu_form_view),
    #path('janatabankedu/', views.janata_bank_edu_form_view),
    #path('mitbbankedu/', views.mitb_bank_edu_form_view),
    #path('onebankedu/', views.one_bank_edu_form_view),
    #path('primebankedu/', views.prime_bank_edu_form_view),
    #path('dutchbanglabankedu/', views.dbbl_bank_edu_form_view),
    #path('standardbankedu/', views.standard_bank_edu_form_view),
    #path('ucbbankedu/', views.ucb_bank_edu_form_view),
    #path('uttarabankedu/', views.uttara_bank_edu_form_view),

    #### URL PATH ENDED FOR APPLICATION FORM OF EDUCATION LOAN

    #### URL PATH STARTED FOR APPLICATION FORM OF HOME LOAN

    
   # path('dutchbanglabankhome/', views.dbbl_home_form_view),
   # path('dhakabankhome/', views.dhaka_bank_home_form_view),
   # path('easternbankhome/', views.eastern_bank_home_form_view),
   # path('grameenbankhome/', views.grameen_bank_home_form_view),
   # path('habibbankhome/', views.habib_bank_home_form_view),
   # path('hsbcbankhome/', views.hsbc_bank_home_form_view),
   # path('jamunabankhome/', views.jamuna_bank_home_form_view),
   # path('janatabankhome/', views.janata_bank_home_form_view),
   # path('mitbbankhome/', views.mitb_bank_home_form_view),
   # path('onebankhome/', views.one_bank_home_form_view),
   # path('primebankhome/', views.prime_bank_home_form_view),
    #path('sonalibankhome/', views.sonali_bank_home_form_view),
   # path('standardbankhome/', views.standard_bank_home_form_view),
   # path('ucbbankhome/', views.ucb_bank_home_form_view),
   # path('uttarabankhome/', views.uttara_bank_home_form_view),


    #### URL PATH ENDED FOR APPLICATION FORM OF HOME LOAN


    #### URL PATH STARTED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY
    #path('bracbanklap/', views.brac_bank_lap_form_view),
    #path('citybanklap/', views.city_bank_lap_form_view),
    #path('dutchbanglabanklap/', views.dbbl_lap_form_view),
    #path('dhakabanklap/', views.dhaka_bank_lap_form_view),
    #path('easternbanklap/', views.eastern_bank_lap_form_view),
    #path('grameenbanklap/', views.grameen_bank_lap_form_view),
    #path('habibbanklap/', views.habib_bank_lap_form_view),
    #path('hsbcbanklap/', views.hsbc_bank_lap_form_view),
    #path('jamunabanklap/', views.jamuna_bank_lap_form_view),
    #path('janatabanklap/', views.janata_bank_lap_form_view),
    #path('mitbbanklap/', views.mitb_bank_lap_form_view),
    #path('onebanklap/', views.one_bank_lap_form_view),
    #path('primebanklap/', views.prime_bank_lap_form_view),
    #path('sonalibanklap/', views.sonali_bank_lap_form_view),
    #path('standardbanklap/', views.standard_bank_lap_form_view),
    #path('ucbbanklap/', views.ucb_bank_lap_form_view),
    #path('uttarabanklap/', views.uttara_bank_lap_form_view),
    #### URL PATH ENDED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY

    #### URL PATH STARTED FOR ELIGIBILITY CHECK FORM OF HOME LOAN
   




]
