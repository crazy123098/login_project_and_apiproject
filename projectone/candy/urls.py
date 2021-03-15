from django.urls import path

from . import views
from .views import create_employee, send_mail, manipa, usdeta, home, first, \
    dahbord, searcha, getting_data, filter_record, update_record, delete_record, curent_dataa, \
    curentdelete_dataa

urlpatterns=[

    path('create_employee/',create_employee),
    path('getting_record/', getting_data),
    path('filter/', filter_record),
    path('update_record/', update_record),
    path('delete_record/',delete_record),
    path('curentdelete_dataa/', curentdelete_dataa),
    path('curent_dataa/',curent_dataa),

    path('home/',home),
    path('first/',views.first,name='Creating_Account'),
    path('trainerlog/', views.trainerlog, name='Trainer'),
    path('usdeta/',usdeta),
    path('send_mail/', send_mail),
    path('manipa/', manipa),
    path('management/',views.management,name='Admin_Login'),
    path('dahbord/',dahbord),
    path('searcha/',searcha),
    path('manipa/',views.manipa,name='back')
]