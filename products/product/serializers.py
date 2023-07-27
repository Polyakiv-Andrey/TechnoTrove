from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "id", "product_name", "price", "main_image", "average_rating", "total_reviews"
        ]
