from products.models import Category


def categories(request):
    """Context processor to make categories available globally"""
    return {
        'categories': Category.objects.all()
    }