"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import ProductsView,MorningView,EveningView,AddView,SubView,MultiView,DivisionView
from api.views import CubeView,NumCheckView,FactorialView,WordCountView,AmstrongView,\
    PalindromeView,PrimeView,ProductsView,ProductDetailsView,ReviewsView,ReviewDetailsView,\
    ProductsViewSetView,ProductModelViewsetView,ReviewModelViewsetView,UsersView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("api/v1/products",ProductsViewSetView,basename="products")
router.register("api/v2/products",ProductModelViewsetView,basename="Books")
router.register("api/v1/reviews",ReviewModelViewsetView,basename="reviews")
router.register("register",UsersView,basename="users")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("cube",CubeView.as_view()),
    path("numcheck",NumCheckView.as_view()),
    path("factorial",FactorialView.as_view()),
    path("wordcount",WordCountView.as_view()),
    path('amstrong',AmstrongView.as_view()),
    path('palindrome',PalindromeView.as_view()),
    path('prime',PrimeView.as_view()),
    path('products',ProductsView.as_view()),
    path('products/<int:id>',ProductDetailsView.as_view()),
    path('reviews',ReviewsView.as_view()),
    path('reviews/<int:id>',ReviewDetailsView.as_view()),
    # path('token/',ObtainAuthToken.as_view())
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
    
#     path('products',ProductsView.as_view()),
#     path('morning',MorningView.as_view()),
#     path('evening',EveningView.as_view()),
#     path('sum',AddView.as_view()),
#     path('difference',SubView.as_view()),
#     path('product',MultiView.as_view()),
#     path('division',DivisionView.as_view())
]+ router.urls
