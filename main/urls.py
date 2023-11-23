from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop_view'),
    path('products/', views.products_view, name='products_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('register/address/', views.address_view, name = 'address_view'),
    path('register/address/credit_card/', views.credit_card_view, name='credit_card_view'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('api/v1/address/', views.AddressAPIList.as_view(),),
    path('api/v1/address_upd/<int:pk>', views.AddressAPIUpdate.as_view(),),
    path('api/v1/address_details/<int:pk>', views.AddressDetailsView.as_view(),),
    path('api/v1/people/', views.PeopleAPIList.as_view(),),
    path('api/v1/people_upd/<int:pk>', views.PeopleAPIUpdate.as_view(),),
    path('api/v1/people_details/<int:pk>', views.PeopleDetailsView.as_view(),),
    path('api/v1/category/', views.CategoryAPIList.as_view(),),
    path('api/v1/category_upd/<int:pk>', views.CategoryAPIUpdate.as_view(),),
    path('api/v1/category_details/<int:pk>', views.CategoryDetailsView.as_view(),),
    path('api/v1/store/', views.StoreAPIList.as_view(),),
    path('api/v1/store_upd/<int:pk>', views.StoreAPIUpdate.as_view(),),
    path('api/v1/store_details/<int:pk>', views.StoreDetailsView.as_view(),),
    path('api/v1/product/', views.ProductAPIList.as_view(),),
    path('api/v1/product_upd/<int:pk>', views.ProductAPIUpdate.as_view(),),
    path('api/v1/product_details/<int:pk>', views.ProductDetailsView.as_view(),),
]