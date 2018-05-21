from django.urls import path

from . import views

#在根 URLconf 中定义app_name，可以在模板中区分其他应用的重名url
app_name = 'poll'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]