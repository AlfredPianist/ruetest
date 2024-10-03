from django.db import models

from app.permissions import IsAdmin, IsStaff


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsStaff]
        return super().get_permissions()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    logo = models.ImageField(upload_to="supplier_logos/")

    def get_permissions(self):
        if self.action in ["destroy"]:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsStaff]
        return super().get_permissions()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    sku = models.CharField(max_length=100, unique=True)
    images = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    suppliers = models.ManyToManyField(
        Supplier, through="UserSupplier", related_name="users"
    )

    def __str__(self):
        return self.username


class UserSupplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_username = models.CharField(max_length=255)
    supplier_password = models.CharField(max_length=128)

    class Meta:
        unique_together = ("user", "supplier")

    def __str__(self):
        return f"{self.user.username} - {self.supplier.name}"
