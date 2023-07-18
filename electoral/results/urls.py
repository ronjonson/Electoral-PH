from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("2004/President", views.result_2004, name="Pres_2004"),
    path("2010/President", views.result_Pres_2010, name="Pres_2010"),
    path("2010/Vice", views.result_VicePres_2010, name="VicePres_2010"),
    path("2016/President", views.result_Pres_2016, name="Pres_2016"),
    path("2016/Vice", views.result_VicePres_2016, name="VicePres_2016"),
    path("2022/President", views.result_Pres_2022, name="Pres_2022"),
    path("2022/Vice", views.result_VicePres_2022, name="VicePres_2022"),
        
]