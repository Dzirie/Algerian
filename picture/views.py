from django.shortcuts import render,redirect,get_object_or_404
from .forms import PictureForm
from .models import Picture
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def pictures(request):
    pictures = Picture.objects.all()
    return render(request,'picture/pictures.html',{'pictures':pictures})

@login_required
def add_picture(request):
    if request.method=='POST':
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.created_by=request.user
            image.save()
            return redirect(reverse('picture:details',kwargs={'image_id':image.id}))
    else:
        form = PictureForm()
    return render(request,'picture/add_picture.html',{'form':form})


def details(request,image_id):
    picture = get_object_or_404(Picture,id=image_id)
    return render(request,'picture/details.html',{'picture':picture})


def edit_picture(request,pk):
    picture = get_object_or_404(Picture,pk=pk)
    if request.method=='POST':
        form = PictureForm(request.POST,request.FILES,instance=picture)
        if form.is_valid():
            form.save()
            return redirect('picture:details',image_id=picture.pk)
    else:
        form = PictureForm(instance=picture)
    return render(request,'picture/edit.html',{'form':form})


def delete(request,pk):
    picture = get_object_or_404(Picture,pk=pk)
    if request.method == 'POST':
        picture.delete()
        return redirect('picture:your_pictures')


def your_pictures(request):
    user=request.user
    query = request.GET.get('query')
    if query:
        pictures=Picture.objects.filter(created_by=user).filter(
        Q(description__icontains=query) | Q(title__icontains=query)
        )
    else:
        pictures=Picture.objects.filter(created_by=user)
    return render(request,'picture/your_pictures.html',{'pictures':pictures,'query':query})


def search_picture(request):
    query = request.GET.get('query')
    if query:
        pictures=Picture.objects.filter(
        Q(description__icontains=query) | Q(created_by__username__icontains=query) | Q(title__icontains=query)
        )
    else:
        pictures=Picture.objects.all()
    return render(request,'picture/pictures.html',{'pictures':pictures,'query':query})
