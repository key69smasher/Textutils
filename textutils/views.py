
from django.http import HttpResponse
from django.shortcuts import render

def index(response):
    return render(response, 'index.html')

def analyse(response):
    # get the text
    djtext = response.POST.get('text', 'default')
    analysed = djtext

    # check box value
    removepunc = response.POST.get('removepunc', 'off')
    fullupper = response.POST.get('uppercase', 'off')

    extraspaceremover = response.POST.get('extraspaceremover', 'off')
    newline = response.POST.get('newline', 'off')

    # know applying the changes
    if removepunc=="on":
        analysed1 = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in analysed:
            if char not in punctuations:
                analysed1 += char
        analysed = analysed1

    if (fullupper=="on"):
        analysed2 = ""
        for char in analysed:
            analysed2 += char.upper()
        analysed = analysed2

    if(newline=="on"):
        analysed3 = ""
        print(newline)
        for char in analysed:
            if char != "\n" and char!="\r":
                analysed3 += char
        analysed = analysed3

    if(extraspaceremover=="on"):
        analysed4 = ""
        for index , char in enumerate(analysed):
            if not(analysed[index] == " " and analysed[index+1]==" "):
                analysed4 += char
        analysed = analysed4

    if(removepunc !="on" and fullupper !="on" and newline !="on" and extraspaceremover !="on"):
        return HttpResponse("error")

    params = {'purpose' : 'according to the marking in checkbox ', 'analysed_text': analysed}
    return render(response, 'analyse.html', params)


