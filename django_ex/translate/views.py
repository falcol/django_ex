import re
from django.shortcuts import render
from rest_framework.views import APIView
from .trans import translate_text, list_languages
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Create your views here.
def index(request):
    languages = list_languages()
    return render(request, 'translate/index.html', languages)


class TranslateAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        if request.data:
            text = request.data['text']
            target_language_code = request.data['target_language_code']
        if request.query_params:
            text = request.query_params['text']
            target_language_code = request.query_params['target_language_code']
        if text == '' or target_language_code == '':
            return Response(
                {'error': 'Please provide text and target_language_code'})
        translate = translate_text(text=text,
                                   target_language_code=target_language_code)
        return Response(translate)
