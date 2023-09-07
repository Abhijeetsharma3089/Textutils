
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
# i have created this file ---> Abhijeet

from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse("<h1> Hello Abhijeet </h1>")


# def about(request):
#     return HttpResponse("about Abhijeet")

def index(request):
    # params={'name':'Abhijeet','place':'mars'}

    # return render(request,"htmlfile/index.html",params)
    return render(request,"htmlfile/index.html")
    # return HttpResponse("Home")



# def ex1(request):
#     s='''<h2> Navigation Bar <br></h2>
#                 <a href="https://www.youtube.com/watch?v=BsDoLVMnmZs">Html with Harry </a><br>
#                  <a href="https://getbootstrap.com/">Bootstrap website </a><br>
#                  <a href="https://www.codewithharry.com/">code with harry website </a><br>
#                  <a href="https://www.google.com/">Google search engine </a><br>
#                  <a href="https://chat.openai.com/?model=text-davinci-002-render-sha">chatgpt website </a><br>
#                       '''
#     return HttpResponse(s)

def analyze(request):
    # get the text
    djtext =(request.POST.get('text','default'))

    # checkboxes values

    # removepunc =(request.GET.get('removepunc','default'))
    removepunc =(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    lowercaps=(request.POST.get('lowercaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    
    # print(removepunc)
    # print(djtext)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

    # check which checkbox is on

    if removepunc == "on":
            # analyzed= djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        classmate={'purpose':'Removed punctuations' , 'analyzed_text':analyzed}
        # analyze the text
        # return HttpResponse("remove punc")
        return render(request,'htmlfile/analyze.html',classmate)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------


    elif(fullcaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        classmate={'purpose':'Changed to Uppercase' , 'analyzed_text':analyzed}
        return render(request,'htmlfile/analyze.html',classmate)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

    elif(lowercaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.lower()
        
        classmate={'purpose':'Changed to lowercase','analyzed_text':analyzed}
        return render(request,'htmlfile/analyze.html',classmate)


# --------------------------------------------------------------------------------------------------------------------------------------------------

    elif(newlineremover =="on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char
        
        classmate={'purpose':'Removed New Lines','analyzed_text':analyzed}
        return render(request,'htmlfile/analyze.html',classmate)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

    elif(extraspaceremover == "on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed+char
        
        classmate={'purpose':'Removed space','analyzed_text':analyzed}
        return render(request,'htmlfile/analyze.html',classmate)



#----------------------------------------------------------------------------------------------------------------------------------------------------------

    else:
        return "error"
