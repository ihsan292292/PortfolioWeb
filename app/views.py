from django.shortcuts import render,redirect
from .models import messages as clientmessage
from django.contrib import messages
from .models import *
import os
# Create your views here.

def index(request):
    pdtl = personal_dtl.objects.get(name="Ihsan K")
    profile=(pdtl.profile_photo.url)
    print(profile[4:])
    
    about = aboutme.objects.all()
    edu = education.objects.order_by('-end_year')
    exp = experience.objects.all()
    skl = skill.objects.all()
    
    djpro = projects.objects.filter(category='django')
    # For Projects
    tit = []
    cat = []
    des = []
    link = []
    img = []
    for i in djpro:
        tit.append(i.title)
        cat.append(i.category)
        des.append(i.description)
        link.append(i.link)
        img.append(i.image.url[4:])
    djp = zip(tit,cat,des,link,img)
    
    mlpro = projects.objects.filter(category='ml')
    # For Projects
    titl = []
    cata = []
    desc = []
    lin = []
    imag = []
    for i in mlpro:
        titl.append(i.title)
        cata.append(i.category)
        desc.append(i.description)
        lin.append(i.link)
        imag.append(i.image.url[4:])
    mlp = zip(titl,cata,desc,lin,imag)
    
    certi = certificates.objects.all()
    # get_in_touch
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        a = clientmessage(snder_name=name,sndr_mail=email,message=message)
        a.save()
        messages.success(request, "Thank you for reaching out! 🌟 I'll read your message and get back to you via email as soon as possible.")
        return redirect('index')
    return render(request,'index.html',{
        'pdtl':pdtl,
        'about':about,
        'edu':edu,
        'exp':exp,
        'skl':skl,
        'djpro':djp,
        'mlp':mlp,
        'certi':certi,
        'profile':profile[4:]
    })