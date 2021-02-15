from django.urls import path


from .views import factorial
urlpatterns = [

    path('',factorial,name='factorial'),


]
