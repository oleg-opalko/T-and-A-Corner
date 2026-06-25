from django.shortcuts import render

from shop.models import Perfume


def home(request):
    featured_perfumes = (
        Perfume.objects.filter(is_available=True, is_featured=True)
        .select_related('brand', 'category')[:4]
    )
    if not featured_perfumes:
        featured_perfumes = (
            Perfume.objects.filter(is_available=True)
            .select_related('brand', 'category')[:4]
        )
    return render(request, 'pages/home.html', {
        'featured_perfumes': featured_perfumes,
    })


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def fragrance_guide(request):
    return render(request, 'pages/fragrance_guide.html')
