from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Grocery import settings
from GroceryPrivate import views

urlpatterns = [

    #User Urls
    path("Index/", views.Index,name="Index"),
    path("user_entry/",views.user_entry,name="userentry"),
    path("User_service/", views.user_service, name="user"),
    path("User_update/<id>/",views.user_update,name="user_update"),
    path("user_delete/<id>/",views.userdelete,name="userdelete"),

    #Category Urls
    path("category_entry/",views.category_entry,name="catentry"),
    path("category_service/" ,views.category_service,name="category"),
    path("category_update/<iid>/",views.category_update ,name="categoryupdate"),
    path("category_delete/<iid>/",views.categorydelete,name="categorydelete"),

    #Customer Urls
    path("customer_entry/",views.customer_entry,name="customerentry"),
    path("customer_service/" ,views.customer_service,name="customer"),
    path("customer_update/<iid>/",views.customer_update,name="customerupdate"),

    #Order Urls
    path("order_entry/",views.order_entry,name="orderentry"),
    path("order_service/",views.order_service,name="order"),
    path("order_update/",views.order_update),
    path("order_Item_entry/",views.order_item_entry,name="orderitementry"),
    path("order_Item_service/",views.order_item_service,name="orderitem"),
    path("order_Item_update/",views.order_item_update),
    path("order_payment_entry/",views.order_payment_entry,name="orderpaymententry"),
    path("order_payment_service/",views.order_payment_service,name="orderpayment"),
    path("order_payment_update/",views.order_payment_update),

    #Product Urls
    path("Product_entry/",views.Product_entry,name="productentry" ),
    path("Product_service/",views.Product_service,name="product"),
    path("Product_update/",views.Product_update),

    #Purchase Urls
    path("Purchase_entry/",views.Purchase_entry,name="purchaseentry"),
    path("Purchase_service/",views.Purchase_service,name="purchase"),
    path("Purchase_update/",views.Purchase_update),

    #Purchase Item Urls
    path("Purchase_Item_entry/",views.Purchase_Item_entry,name="purchaseitementry"),
    path("Purchase_Item_service/",views.Purchase_Item_service,name="purchase_item"),
    path("Purchase_Item_update/",views.Purchase_Item_update),

    #Supplier Urls
    path("Supplier_entry/",views.Supplier_entry,name="suppentry"),
    path("Supplier_service/",views.Supplier_service,name="supplier"),
    path("Supplier_update/<iid>/",views.Supplier_update,name="supplierupdate"),

    #User Payment Urls
    path("User_payment_entry/",views.User_payment_entry,name="userpaymententry"),
    path("User_payment_update/<id>/",views.userpaymentupdate,name="user_payment_update"),
    path("user_payment_delete/<id>/",views.userpaymentdelete,name="userpaymentdelete"),
    path("User_payment_service/",views.User_payment_service ,name="userpayment"),

    #add ons-- for admin panel Urls
    path("page_account/",views.page_account,name="pageaccount"),
    path("page_notification/",views.page_notification, name="pagenotification"),
    path("page_connection/",views.page_connection,name="pageconnection"),

    # Author Urls
    path("auth_login/",views.auth_login,name="authlogin"),
    path("auth_registration/",views.auth_registration,name="authregister"),
    path("auth_forgot/",views.auth_forgot,name="authforgot"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)