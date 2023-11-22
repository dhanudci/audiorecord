from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.voice_response import Gather, VoiceResponse
from twilio.rest import Client
from .forms import AudioRecordForm
from .models import AudioRecord

account_sid = "ACf1a498b26cacb62bbe689adf0697130d"
auth_token = "d8e546a1597143d56b9063002a7923a7"

client = Client(account_sid, auth_token)

from_phone_number = "+14423334087"  

def upload_audio(request): 
    if request.method == 'POST':
        form = AudioRecordForm(request.POST)
        if form.is_valid():
            raw_phone_number = form.cleaned_data['phonenumber']

            phone_number = "+91" + raw_phone_number

            voice_response = VoiceResponse()

            voice_response.say("Welcome to Dci. We are calling from the HR team.")

            questions = [
                "Question 1: May I know your name?",
                "Question 2: Okay, please let me know which domain you want to choose.",
                "Question 3: Please let me know your years of experience.",
            ]

            for question in questions:
                gather = Gather(numDigits=1, action='/process_survey', method='POST')
                gather.say(question)
                voice_response.append(gather)

            voice_response.say("Thanks for your answers. We will get back to you shortly.")

            call = client.calls.create(
                to=phone_number,
                from_=from_phone_number,
                twiml=str(voice_response)
            )

            audio = AudioRecord(phonenumber=phone_number)
            audio.save()

            # Return a response (you can customize this)
            # return HttpResponse(f"Calling {phone_number}...")
    else:
        form = AudioRecordForm()

    return render(request, 'home.html', {'form': form})
