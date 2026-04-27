from django.urls import path
from .views import addproduct,product_list,update_product
from .views import delete_product,dashboard

urlpatterns = [
    path('add_product/',addproduct,name="addproduct"),
    path('product_list/',product_list,name="productlist"),
    path('update_product/<int:id>/',update_product,name="updateproduct"),
    path('delete_product/<int:id>/' , delete_product,name="deleteproduct"),
    path('deshboard/',dashboard,name="dashboard")
]
