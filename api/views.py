from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books
from api.models import Reviews
from api.serializer import BookSerializer,ReviewSerializer,UserSerializer,CartSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from api.models import Carts
#
# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"Good Morning"})
#
# class EveningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"Good Evening"})
#
# # class AddView(APIView):
# #     def get(self,request,*args,**kwargs):
# #         num1 = int(input("enter first number"))
# #         num2 = int(input("enter second number"))
# #         res = num1 + num2
# #         return Response({"result":res})
#
# class SubView(APIView):
#     def get(self,request,*args,**kwargs):
#         num1 = int(input("enter the first number"))
#         num2 = int(input("enter the second number"))
#         res = num1 - num2
#         return Response({"result":res})
#
# class MultiView(APIView):
#     def get(self,request,*args,**kwargs):
#         num1 = int(input("enter the first number"))
#         num2 = int(input("enter the second number"))
#         res = num1 * num2
#         return Response({"result":res})
#
# class DivisionView(APIView):
#     def get(self,request,*args,**kwargs):
#         num1 = int(input("enter the first number"))
#         num2 = int(input("enter the second number"))
#         res = num1 / num2
#         return Response({"result":res})
#
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1 = request.data.get("num1")
#         n2 = request.data.get("num2")
#         res = int(n1) + int(n2)
#         return Response({"result":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get("num"))
        res = n**3
        return Response({"result":res})

class NumCheckView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get("num"))

        if n%2 == 0:
            res = "number is even"
        else:
            res = "number is odd"
        return Response({"result":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get("num"))
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return Response(data = fact)

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        txt = request.data.get("text")
        words = txt.split(" ")
        wc = {}
        for w in words:
            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1
        return Response(data = wc)

class AmstrongView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get("num"))
        count = 0
        num = num1 = n
        sum = 0
        while n > 0:
            n = n // 10
            count  += 1
        #print("number of digits=", count)
        while num > 0:
            d = num % 10
            sum +=  pow(d, count)
            num = num // 10
        if num1 == sum:
            res = "armstrong"
        else:
            res = "not armstrong"
        return Response(data = res)

class PalindromeView(APIView):
    def post(self,request,*args,**kwargs):
        n = request.data.get("num")
        str1 = n[::-1]
        #print(str1)
        if n == str1:
            res = "palindrome"
        else:
            res = "not palindrome"
        return Response(data = res)

class PrimeView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get('num'))
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            res = "prime number"
        else:
            res = "not a prime"
        return Response(data = res)

class ProductsView(APIView):

    def get(self,request,*args,**kwargs):
        qs = Books.objects.all()
        serializer = BookSerializer(qs,many=True)
        return Response(data = serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)

class ProductDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        book = Books.objects.get(id = id)
        serializer = BookSerializer(book,many=False)
        return Response(data = serializer.data)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data = "deleted")

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data = serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response(data = serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)

class ReviewDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Reviews.objects.get(id = id)
        serializer = ReviewSerializer(qs,many = False)
        return Response(data = serializer.data)

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Reviews.objects.get(id = id)
        serializer = ReviewSerializer(instance=object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Reviews.objects.get(id = id).delete()
        return Response(data="deleted")


class ProductsViewSetView(ViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs = Books.objects.all()
        serializer = BookSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        book = Books.objects.get(id = id)
        serializer = BookSerializer(book,many = False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Books.objects.get(id=id)
        serializer = BookSerializer(instance=object,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

class ProductModelViewsetView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        book = Books.objects.get(id=id)
        user = request.user
        Reviews.objects.create(book=book,user=user,comment=request.data.get("comment"),rating=request.data.get("rating"))
        return Response(data="created")

    @action(methods=["GET"],detail=True)
    def get_reviews(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        book =Books.objects.get(id=id)
        reviews = book.reviews_set.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    @action(methods=["POST"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book = Books.objects.get(id = id)
        Carts.objects.create(book=book, user=request.user)
        return Response(data="created")

    @action(methods=["GET"],detail=True)
    def cart_list(self,request,*args,**kwargs):
        cart = Carts.objects.all()
        cart_list = cart.books_set.all()
        serializer = CartSerializer(cart_list,many=True)
        return Response(data= serializer.data)


class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self,request,*args,**kwargs):
        all_reviews = Reviews.objects.all()
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer = ReviewSerializer(all_reviews,many=True)
        return Response(data=serializer.data)

class UsersView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
