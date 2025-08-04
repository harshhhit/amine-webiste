from django.db import models
from base.models import BaseModel

# ✅ 1. BaseModel (Imported)

# You imported BaseModel, which is a custom abstract base class. It likely provides common fields to every model that inherits from it:
#     uid — a unique UUID for each record
#     created_at — timestamp when the record is created
#     updated_at — timestamp when the record is last updated
# This helps avoid repeating code in every model.


# 🧠 What Is a Class in Python?
# A class is like a blueprint or template used to create objects.
# You can think of it like a design plan for building something — like a car, a person, or a product. The class defines:
#     What properties (data) it has
#     What actions (methods) it can do
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")


#  2. Category Model
#  What it does:
#     Represents a product category like "Electronics", "Clothing", etc.
#     category_name stores the name of the category.
#     category_image allows you to upload an image to visually represent the category.
#     Inherits from BaseModel, so also has uid, created_at, updated_at.

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

## What it does:
#     Represents an individual product.
#     product_name stores the name of the product (e.g., "iPhone 14").
#     category links the product to a specific Category (e.g., Electronics).
#         Uses a ForeignKey for a many-to-one relationship.
#         on_delete=models.CASCADE: if the category is deleted, the product is too.
#         related_name="products" lets you get all products of a category like:


class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product_images")

    # In Django, a ForeignKey is used to create a relationship between two models — specifically, a many-to-one relationship.
    # CASCADE means:
    # "If the referenced Product is deleted, delete this row too.This is the cascade effect.If you delete a product, all related rows in the other table (e.g., orders or reviews) will be automatically deleted.

