from django.http import HttpResponse
import emoji

def index(request):
    result = emoji.emojize('Python is :thumbs_up:')
    return HttpResponse(f"Hello, world. You're at the polls index.{result}")

