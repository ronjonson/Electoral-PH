from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:year>/President", views.ResultView.as_view(),{'position': 'Pres'}, name='President-Result'),
    path("<int:year>/VicePresident", views.ResultView.as_view(), {'position': 'VicePres'}, name='VicePresident-Result'),       
]