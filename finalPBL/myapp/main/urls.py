from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.healthCare, name='home'),
    path('faqs/',views.faq, name='faq'),
    path('register/',views.reg, name='reg'),
    path('doc1/',views.date, name='doc1'),
    path('doc2/',views.date2, name='doc2'),
    path('doc3/',views.date3, name='doc3'),
    path('doc4/',views.date4, name='doc4'),
    path('payment/',views.pay, name='pay')
    # path('speech-to-text/', views.speech_to_text_view, name='speech_to_text'),
]
