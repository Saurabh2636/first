from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyzer(request):
    text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    upper=request.POST.get('upper','off')
    print(text)
    print(removepunc)
    print(upper)
    if removepunc=="on":
        string="AEIOU"
        new=""
        for i in text:
            if i is not string:
                new=new+i
            params={'purpose':"removed punctuation",'analyzed_text':new}
            return render (request,'analyzer.html',params)
    elif upper=='on':
        new=''
        for i in text:
            new=new+i.upper()
        params={'purpose':"removed punctuation",'analyzed_text':new}
        return render (request,'analyzer.html',params)
       
            
