from django.shortcuts import render
from .models import Contact
# Create your views here.
def healthCare(request):
    return render(request, 'healthCare.html')

def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        bg = request.POST['bg']
        email = request.POST['email']
        address = request.POST['address']
        age = request.POST['age']
        contact = Contact(name=name,phone=phone,bg=bg,email=email,address=address,age=age)
        contact.save()
        print('----------------gone--------------------')

    return render(request, 'reg.html')

def faq(request):
    return render(request, 'faqs.html')

def date(request):
    details = Contact.objects.first()

    return render(request, 'datepicker.html',{'details':details})

def date2(request):
    details = Contact.objects.first()

    return render(request, 'doc2.html',{'details':details})

def date3(request):
    details = Contact.objects.first()

    return render(request, 'doc3.html',{'details':details})

def date4(request):
    details = Contact.objects.first()

    return render(request, 'doc4.html',{'details':details})


def pay(request):
    return render(request, 'payment.html')



# # speech to text testing--------------------------
# import speech_recognition as sr
# from django.shortcuts import render

# def speech_to_text_view(request):
#     if request.method == 'POST':
#         # create a recognizer instance
#         r = sr.Recognizer()

#         # get the audio file uploaded by the user
#         audio_file = request.FILES.get('audio_file')

#         # open the audio file and extract the audio data
#         with sr.AudioFile(audio_file) as source:
#             audio_data = r.record(source)

#         try:
#             # recognize speech using Google Speech Recognition
#             text = r.recognize_google(audio_data)
#             print("------working-----")

#             # pass the recognized text to the template
#             return render(request, 'speech_to_text.html', {'text': text})
#         except sr.UnknownValueError:
#             # if the recognizer could not understand the audio, return an error message
#             return render(request, 'speech_to_text.html', {'error': 'Could not understand audio'})
#         except sr.RequestError as e:
#             # if there was a problem with the API request, return an error message
#             return render(request, 'speech_to_text.html', {'error': f"API Error: {e}"})

#     # if the request method is GET, just render the template
#     return render(request, 'speech_to_text.html')
