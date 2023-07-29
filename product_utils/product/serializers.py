from rest_framework import serializers

from product_utils.product.models import Image


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "id", "product_name", "price", "main_image", "average_rating", "total_reviews"
        ]


class ProductRetrivSerializer(serializers.ModelSerializer):
    additional_images = serializers.SerializerMethodField()

    class Meta:
        fields = ProductListSerializer.Meta.fields + [
            "product_description", "SKU", "additional_images", "condition", "warranty",
        ]

    def get_additional_images(self, product):
        image_ids = product.additional_images.values_list('id', flat=True)
        images = Image.objects.filter(id__in=image_ids)
        return [image.image.url for image in images]