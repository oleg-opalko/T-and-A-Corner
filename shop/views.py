from django.shortcuts import get_object_or_404, render

from .models import Category, Perfume


def catalog(request):
    perfumes = (
        Perfume.objects.filter(is_available=True)
        .select_related('brand', 'category')
    )
    categories = Category.objects.all()
    return render(request, 'shop/catalog.html', {
        'perfumes': perfumes,
        'categories': categories,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    perfumes = category.perfumes.filter(is_available=True).select_related('brand')
    return render(request, 'shop/category.html', {
        'category': category,
        'perfumes': perfumes,
    })


def perfume_detail(request, slug):
    perfume = get_object_or_404(
        Perfume.objects.select_related('brand', 'category'),
        slug=slug,
        is_available=True,
    )
    return render(request, 'shop/perfume_detail.html', {'perfume': perfume})
