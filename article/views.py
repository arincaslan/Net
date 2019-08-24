from django.shortcuts import render, redirect
from .models import Article, Product, Contact
from django.core.paginator import Paginator


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def process(request):
    return render(request,"process.html")

def articles(request):
    articles = Article.objects.all()
    paginator = Paginator(articles,6)
    page = request.GET.get('page')
    makale = paginator.get_page(page)
    return render(request, "articles.html", {'makale' : makale})


def articleDetail(request, articleslug):
    article = Article.objects.get(article_slug= articleslug)
    print(article.article_image)
    return render(request, "article_detail.html", { 'nbar' : 'article_detail', 'article': article })

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products,6)
    page = request.GET.get('page')
    urunler = paginator.get_page(page)
    print(urunler);
    return render(request, "products.html", {'urunler' : urunler})

def productDetail(request, productslug):
    product = Product.objects.get(product_slug= productslug)
    return render(request, "product_detail.html", { 'nbar' : 'product_detail', 'product': product })

def contact(request):
    if request.method == 'POST':
        isim = request.POST.get('isim')
        email = request.POST.get('email')
        mesaj = request.POST.get('mesaj')

        contact = Contact(iletisim_isim=isim, iletisim_mail=email, iletisim_mesaj=mesaj)
        contact.save()
        return render(request,"contact.html")

    return render(request,"contact.html")

# Create your views here.
