import traceback
from django.http import JsonResponse
import json
import re
from bs4 import BeautifulSoup
from django.conf import settings


def process_response(response):
    soup = BeautifulSoup(str(response.content), 'html.parser')
    soup.prettify()
    message=""

    if settings.DEBUG:
        message = soup.p.get_text()
        for li in soup.find_all('li'):
            message+=li.get_text()

        for p in soup.find_all('p'):
            if p == soup.p:
                message+=" "
            else:
                message+=p.get_text()
                message=re.sub(r'\\n',"",str(message))
                message=re.sub(r'\\',"",str(message))
                message=re.sub(r' +'," ",str(message))
    else:
        for p in soup.find_all('p'):
            message+=p.get_text()

    return message

class JsonException:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
                status = response.status_code
                message = process_response(response)
                content = {'statusCode': status, 'errorMessage': message}
        if response.status_code == 500:
            status = response.status_code
            content = {'errorMessage': 'Server Error'}

        return JsonResponse(content, status=status, safe=False)
