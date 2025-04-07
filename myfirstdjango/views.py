from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def aboutUs(request):
    output = 0
    if request.method =="GET":
        output = request.GET.get('output')
    # return HttpResponse("Welcome to ducat")
    return render(request,"about.html",{'output':output})
def contact(request):
    return render(request,"contact.html")
def course(request):
    return HttpResponse("another function data")
def CourseById(request,courseid):
    return HttpResponse(courseid)
def homePage(request):
    num=["this is a footer data","and this is the second value of a list wow"]
    data={
        "title":"this is project title from key 1",
        "bdata":"courses: data from key 2",
        "clist":["php","python","java"],
        "student_details":[{'name':"aman",'phone':542352352},
                           {'name':"aman-kumar",'phone':52352},],
        'numbers':[10,20,40,50],
        "num":num
        }
    # how to insert the static files
    return render(request,"index.html",data)
def userForm(request):

    finalans = 0
    try:
        if request.method == "POST":
            
            n1= (int )(request.POST['num1'])
            n2= (int )(request.POST['num2'])
            finalans = n1+n2
            print("final ans is ", finalans)
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
                }
            url = "/about-us/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        print("error in data")   
    return render(request,"userform.html")