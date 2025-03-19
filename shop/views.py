from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Fiyat aralığı filtresi
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Stok durumuna göre filtreleme
    in_stock = request.GET.get('in_stock')
    if in_stock:
        products = products.filter(stock__gt=0)

    # Ürün ismine göre arama
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Ürünleri sıralama
    sort_option = request.GET.get('sort')
    if sort_option == "price_asc":
        products = products.order_by("price")
    elif sort_option == "price_desc":
        products = products.order_by("-price")
    elif sort_option == "date_new":
        products = products.order_by("-created_at")
    elif sort_option == "date_old":
        products = products.order_by("created_at")

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'selected_category': category,
        'query': query,
        'sort_option': sort_option  # HTML tarafına seçili sıralama seçeneğini göndermek için
    })


    

from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Review
from .forms import ReviewForm

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    reviews = Review.objects.filter(product=product)
    average_rating = product.average_rating()
    all_reviews = product.reviews.all()
    total_reviews = all_reviews.count()

    # Eğer 'show_all_reviews' parametresi yoksa sadece ilk 3 yorumu göster
    if not request.GET.get("show_all_reviews"):
        reviews = all_reviews[:3]
    else:
        reviews = all_reviews  # Tüm yorumları göster
    
    # Benzer ürünler (Aynı kategoriye sahip diğer ürünler)
    similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    # Kullanıcı yorum formu
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect("shop:product_detail", product_slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, "shop/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "review_form": form,
        "similar_products": similar_products,
        "average_rating": average_rating,
        'total_reviews': total_reviews  # Toplam yorum sayısını gönderiyoruz
    })

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Favorite

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, "Ürün favorilere eklendi! ❤️")
    else:
        messages.info(request, "Bu ürün zaten favorilerinizde.")

    return redirect("shop:product_detail", product_slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite = Favorite.objects.filter(user=request.user, product=product)
    
    if favorite.exists():
        favorite.delete()
        messages.success(request, "Ürün favorilerden kaldırıldı. ❌")
    else:
        messages.info(request, "Bu ürün favorilerinizde bulunmuyor.")

    return redirect("shop:favorites")


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "shop/favorite_list.html", {"favorites": favorites})
