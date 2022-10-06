from rest_framework import serializers
from api.models import Books,Reviews,Carts
from django.contrib.auth.models import User

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    publisher = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self,validated_data):
        return Books.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.publisher = validated_data.get("publisher")
        instance.quantity = validated_data.get("quantity")
        instance.save()
        return instance

#object level validation:

    def validate(self, data):
        quantity = data.get("quantity")
        price = data.get("price")
        if quantity not in range(10,100):
            raise serializers.ValidationError("Invalid quantity")
        if price not in range(50,1000):
            raise serializers.ValidationError("Invalid Price")

        return data

#field level validation:

    def validate_price(self,value):
        if value not in range(50,1000):
            raise serializers.ValidationError("Invalid Price")
        return value
    def validate_quantity(self,value):
        if value not in range(10,100):
            raise serializers.ValidationError("Invalid Quantity")
        return value



class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.CharField(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):
    book = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Carts
        fields = ["book","user","status"]