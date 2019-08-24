from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "article"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('process/', views.process, name="process"),
    path('articles/', views.articles, name = "articles"),
    path('article/<slug:articleslug>', views.articleDetail, name="articleDetail"),
    path('products/', views.products, name = "products"),
    path('product/<slug:productslug>', views.productDetail, name="productDetail"),
    path('contact/', views.contact, name = "contact"),
]
