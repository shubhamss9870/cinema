from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def first_page(request):
    categorys = video.objects.all()

    # add pagination
    posts = video.objects.all()
    p = Paginator(posts, 3)

    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except pagenull:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'list': page_obj}
    return render(request, 'home.html', context)

    #return render(request, 'home.html', {'list': categorys})


def best(request):
    best_video = category.objects.get(category_name="Best")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'best.html', {'har': videos})


def new(request):
    best_video = category.objects.get(category_name="New")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'new.html', {'char': videos})


def hits(request):
    best_video = category.objects.get(category_name="Hits")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'hits.html', {'char': videos})


def images(request):
    best_video = category.objects.get(category_name="Images")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'images.html', {'char': videos})


def pornstar(request):
    best_video = category.objects.get(category_name="Porn-star")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'pornstar.html', {'char': videos})


def exclusive(request):
    best_video = category.objects.get(category_name="Exclusive")
    videos = video.objects.filter(category=best_video.id)

    return render(request, 'exclusive.html', {'char': videos})





# Create your views here.


def index(request):
    posts = video.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except pagenull:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', context)
