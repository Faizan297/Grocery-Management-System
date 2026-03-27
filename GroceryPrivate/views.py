from django import http
from django.shortcuts import render
from GroceryPrivate import models
from django.shortcuts import redirect
from django.http import JsonResponse

# Create your views here.
def Index(request):
     return render(request,"index.html")

# USER ENTRY------------------------
def user_entry(request):
    name={
         "title":"User Entry | G-Mart"
    }
#     print(request.META.get('HTTP_X_REQUESTED_WITH'))
    if request.method == "POST":
      if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#      #    print(request.POST)
        try: 
          Entry_Date = request.POST.get('joining_date')
          User_ID = request.POST.get('user_id')
          # CHECK IF DATA ALREADY EXISTS
          if models.user_entry.objects.filter(
               User_ID=User_ID
               ).exists():
                    return JsonResponse({
                    'success': 409,
                    'title': 'Already Exists',
                    'message': 'User with this User ID already exists!',
                    'icon': 'warning'
               })
          user_name = request.POST.get('name')
          father_name = request.POST.get('father_name')
          mother_name = request.POST.get('mother_name')
          Gender = request.POST.get('gender')
          dob = request.POST.get('dob')
          contact_Number = request.POST.get('contact_number')
          alternate_number=request.POST.get('alternate_number')
          Email_ID=request.POST.get('email')
          aadhaar = request.POST.get('aadhaar_number')
          Qualification = request.POST.get('qualification')
          position = request.POST.get('position')
          salary = request.POST.get('salary')
          status = request.POST.get('status')
          State = request.POST.get('state_current')
          District = request.POST.get('district_current')
          Pin = request.POST.get('pin_current')
          Address=request.POST.get('address_current')
          state=request.POST.get('state_permanent')
          district=request.POST.get('district_permanent')
          pin = request.POST.get('pin_permanent')
          address=request.POST.get('address_permanent')
          photo = request.FILES.get('photo')
          Aadhaar_photo = request.FILES.get('aadhaar_photo')
          signature=request.FILES.get('signature')
          certificate=request.FILES.get('certificate')
          # print(photo)
          # print(Aadhaar_photo)
          # print(signature)
          # print(certificate)
          user_obj=models.user_entry()
          user_obj.Joining_date=Entry_Date
          user_obj.User_ID=User_ID
          user_obj.Name=user_name
          user_obj.Father_name=father_name
          user_obj.Mother_name=mother_name
          user_obj.Gender=Gender
          user_obj.DOB=dob
          user_obj.contact_number=contact_Number
          user_obj.Alternate_number=alternate_number
          user_obj.Email_ID=Email_ID
          user_obj.aadhaar_number=aadhaar
          user_obj.highest_qualifiication=Qualification
          user_obj.position=position
          user_obj.salary=salary
          user_obj.status=status
          user_obj.state=State
          user_obj.district=District
          user_obj.pin=Pin
          user_obj.address=Address
          user_obj.Corr_State=state
          user_obj.Corr_District=district
          user_obj.Corr_Pin=pin
          user_obj.corr_address=address
          user_obj.photo=photo
          user_obj.aadhaar_pic=Aadhaar_photo
          user_obj.signature=signature
          user_obj.certificate=certificate
          user_obj.save()
          if user_obj.pk is not None:
                    data={
                         'success' : 200,
                         'title' : 'Success',
                         'message' : 'Inserted Succesfully !',
                         'icon': 'success'
                    }
          else:
               data= {
                         'success' : 500,
                         'title' : 'Error!',
                         'message' : 'something Went Wrong!',
                         'icon': 'error'
                    }    
          return http.JsonResponse(data,safe=False)
        except Exception as error:
          print(error)
          data={
               'success' : 500,
               'title' : 'Error!',
               'message' : str(error),
               'icon' : 'error'
               }
          return http.JsonResponse(data,safe=False)
    return render(request,"User-entry.html",{'name':name})
def user_service(request):
    data = {
        'title': 'User Service'
    }

    user_details = models.user_entry.objects.all()
    filter_data = None

    if request.method == "POST":
        User_ID = request.POST.get('User_ID')
        Name = request.POST.get('Name')
        contact_number = request.POST.get('contact_number')
        status = request.POST.get('status')

        conditions = {}

        if User_ID:
            conditions['User_ID'] = User_ID

        if Name:
            conditions['Name__icontains'] = Name

        if contact_number:
            conditions['contact_number__icontains'] = contact_number

        if status:
            conditions['status'] = status

     #    print("FILTER CONDITIONS:", conditions)

        if conditions:
            filter_data = models.user_entry.objects.filter(**conditions)
        else:
            filter_data = None 
    return render(request,"user-service.html",{'data':data,'user_details':user_details,'filter_data':filter_data})
def user_update(request,id):
     data={
          'title':'User Update'
     }
     print(id)
     try:
        updatedata=models.user_entry.objects.get(User_ID=id)
     #    print(updatedata.Joining_date)
        data['updatedata'] = updatedata
        
     except Exception as e:
          print(e)

     if request.method == 'POST':
          # if request.META.get('HTTP_X_REQUESTED_WITH') =='XMLHttpRequest':
             updatedata=models.user_entry.objects.get(User_ID=id)
             updatedata.Joining_date= request.POST.get('joining_date')
             updatedata.User_ID= request.POST.get('user_id')
             updatedata.Name= request.POST.get('Name')
             updatedata.Father_name= request.POST.get('father_name')
             updatedata.Mother_name= request.POST.get('mother_name')
             updatedata.Gender= request.POST.get('gender')
             updatedata.DOB= request.POST.get('DOB')
             updatedata.contact_number= request.POST.get('contact_number')
             updatedata.Alternate_number= request.POST.get('alternate_number')
             updatedata.Email_ID= request.POST.get('email')
             updatedata.aadhaar_number= request.POST.get('aadhaar_number')
             updatedata.highest_qualifiication= request.POST.get('qualification')
             updatedata.position= request.POST.get('position')
             updatedata.salary= request.POST.get('salary')
             updatedata.status= request.POST.get('status')
             updatedata.state= request.POST.get('state_current')
             updatedata.district= request.POST.get('district_current')
             updatedata.pin= request.POST.get('pin_current')
             updatedata.address= request.POST.get('address_current')
             updatedata.Corr_State= request.POST.get('state_permanent')
             updatedata.Corr_District= request.POST.get('district_permanent')
             updatedata.Corr_Pin= request.POST.get('pin_permanent')
             updatedata.corr_address= request.POST.get('address_permanent')
             # FILE FIELDS (SAFE UPDATE)
             if request.FILES.get('photo'):
               updatedata.photo = request.FILES.get('photo')

             if request.FILES.get('aadhaar_photo'):
               updatedata.aadhaar_pic = request.FILES.get('aadhaar_photo')

             if request.FILES.get('signature'):
               updatedata.signature = request.FILES.get('signature')

             if request.FILES.get('certificate'):
              updatedata.certificate = request.FILES.get('certificate')
             updatedata.save()
             return redirect('user')
             

     return render(request,"User-update.html",{'data':data})
def userdelete(request,id):
    try:
      models.user_entry.objects.get(User_ID=id).delete()
      return redirect('user')
    except Exception as e:
        print(e)
    

# CATEGORY ENTRY----------------------------
def category_entry(request):
     data={
        'title': 'Category Entry | G-Mart '
     }
     # print(request.POST)
     if request.method =='POST':
       if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
               try:
                    Category_ID=request.POST.get("category_ID")
                    if models.category_entry.objects.filter(
                         Category_ID=Category_ID
                    ).exists():
                         return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Category ID already exists!',
                              'icon': 'warning'
                         })
                    category_name = request.POST.get('category_Name')
                    User_ID = request.POST.get('User_ID')
                    Order_ID = request.POST.get('Order_ID')
                    Status = request.POST.get('status')
                    Description = request.POST.get('Descrription')
                    # print(Category_ID,category_name,User_ID,Order_ID,Status,Description)
                    Category_obj=models.category_entry()
                    Category_obj.Category_ID=Category_ID
                    Category_obj.Category_name=category_name
                    Category_obj.User_ID=User_ID
                    Category_obj.Order_ID=Order_ID
                    Category_obj.Status=Status
                    Category_obj.Description=Description
                    Category_obj.save()
                    if Category_obj.pk is not None:
                         data={
                              'title':'Success',
                              'success':200,
                              'message':"Data inserted Successfully !",
                              'icon': 'success'
                         }
                    else:
                         data={
                              'title':'Success',
                              'success':500,
                              'message':"Something Went Wrong !",
                              'icon': 'error'
                              

                         }
                    return http.JsonResponse(data,safe=False)
               except Exception as error:
               #   print(str(error))
                    data={
                         'success':500,
                         'title':'Error !',
                         'message':str(error),
                         'icon':'error'
                    }
               return http.JsonResponse(data,safe=False)
          
     return render(request,"category-entry.html",{'data':data})
def category_service(request):
     data = {
        'title': 'Cartegory Service'
    }
     category_details = models.category_entry.objects.values('Category_ID')
     # print(category_details)
     if request.POST:
          category_ID=request.POST.get('category_ID')
          category_name=request.POST.get('category_Name')
          status=request.POST.get('status')
          # print(category_ID,category_name,status)
          conditions={}
          if category_ID !="" and category_ID is not None:
               conditions['Category_ID']=category_ID
          if category_name !="" and category_name is not None:
               conditions['Category_name']=category_name
          if status !="" and status is not None:
               conditions['Status']=status
               
          # print(conditions)  
          if conditions:
           filter_data=models.category_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render(request,'category-service.html',{'data':data,'category_details':category_details,'filter_data':filter_data})
          

     return render(request,'category-service.html',{'data':data,'category_details':category_details})
def category_update(request,iid):
     print(iid)
     data={
          'title': 'Category Update'
     }
     try:
          update_data=models.category_entry.objects.get(Category_ID=iid)
          data['updatedata'] = update_data
     except Exception as e:
          print(e)
     if request.method=='POST':
          # if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
             update_data=models.category_entry.objects.get(Category_ID=iid)
             update_data.Category_ID=request.POST.get('category_ID')
             update_data.Category_name=request.POST.get('category_Name')
             update_data.User_ID=request.POST.get('User_ID')
             update_data.Order_ID=request.POST.get('Order_ID')
             update_data.Status=request.POST.get('status')
             update_data.Description=request.POST.get('Descrription')
             update_data.save()
             return redirect('category')


     return render (request,'category-update.html',{'data': data})
def categorydelete(request,iid):
     try:
        models.category_entry.objects.get(Category_ID=iid).delete()
        return redirect('category')
     except Exception as e:
          print(e)

# CUSTOMER ENTRY----------------------------

def customer_entry(request):
    if request.method=='POST':
       if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            try:
                    Entry_date=request.POST.get('Entry_date')
                    customer_id=request.POST.get('customer_id')
                    if models.customer_entry.objects.filter(
                         Customer_ID=customer_id
                    ).exists():
                         return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Customer ID already exists!',
                              'icon': 'warning'
                         })
                    name=request.POST.get('name')
                    contact_number=request.POST.get('contact_number')
                    email=request.POST.get('email')
                    status=request.POST.get('status')
                    state=request.POST.get('state')
                    district=request.POST.get('district')
                    pin=request.POST.get('pin')
                    address=request.POST.get('address')
                    customer_obj=models.customer_entry()
                    customer_obj.Created_at=Entry_date
                    customer_obj.Customer_ID=customer_id
                    customer_obj.Name=name
                    customer_obj.Contact_number=contact_number
                    customer_obj.Email=email
                    customer_obj.Status=status
                    customer_obj.State=state
                    customer_obj.District=district
                    customer_obj.Pin=pin
                    customer_obj.Address=address
                    customer_obj.save()
                    if customer_obj.pk is not None:
                         data={
                              'success':200,
                              'title':'success',
                              'message': 'Inserted Successfully !',
                              'icon': 'success'
                         }
                    else:
                        data={
                              'success':200,
                              'title':'Error',
                              'message': 'Something went wrong !',
                              'icon': 'error'
                         } 
                    return http.JsonResponse(data,safe=False)
            except Exception as error:
                 print(error)
                 data={
                         'success':500,
                         'title':'error',
                         'message':str(error),
                         'icon': 'error' 
                 }
                 return http.JsonResponse(data,safe=False)
    return render(request,'customer-entry.html')
def customer_service(request):
     customer_details=models.customer_entry.objects.values('Customer_ID')
     if request.POST:
          Entry_date=request.POST.get('Entry_date')
          customer_id=request.POST.get('customer_id')
          Name=request.POST.get('Name')
          contact_number=request.POST.get('contact_number')
          status=request.POST.get('status')
          conditions={}
          if Entry_date!="" and Entry_date is not None:
               conditions['Created_at']=Entry_date
          if customer_id!="" and customer_id is not None:
               conditions['Customer_ID']=customer_id
          if Name!="" and Name is not None:
               conditions['Name']=Name
          if contact_number!="" and contact_number is not None:
               conditions['Contact_number']=contact_number
          if status!="" and status is not None:
               conditions['Status']=status
          if conditions:
               filter_data=models.customer_entry.objects.filter(**conditions)
          else:
               filter_data=None

          return render(request,'customer-service.html',{'customer_details':customer_details,'filter_data':filter_data})

     return render(request,'customer-service.html',{'customer_details':customer_details})
def customer_update(request,iid):
     print(iid)
     return render (request,'customer-update.html')

# ORDER ENTRY----------------------------

def order_entry(request):
     if request.method=='POST':
        if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
            try:   
                    order_date=request.POST.get('order_date')
                    order_id=request.POST.get('order_id')
                    if models.order_entry.objects.filter(
                         Order_ID=order_id
                    ).exists():
                         return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Order ID already exists!',
                              'icon': 'warning'
                         })
                    user_id=request.POST.get('user_id')
                    customer_id=request.POST.get('customer_id')
                    amount=request.POST.get('amount')
                    disc_amount=request.POST.get('disc_amount')
                    tax=request.POST.get('tax')
                    Pay_amount=request.POST.get('Pay_amount')
                    status=request.POST.get('status')
                    order_obj=models.order_entry()
                    order_obj.Order_date=order_date
                    order_obj.Order_ID=order_id
                    order_obj.User_ID=user_id
                    order_obj.Customer_ID=customer_id
                    order_obj.Amount=amount
                    order_obj.Disc_amount=disc_amount
                    order_obj.tax=tax
                    order_obj.pay_amount=Pay_amount
                    order_obj.Status=status
                    order_obj.save()
                    if order_obj.pk is not None:
                         data={
                              'success':200,
                              'icon':'success',
                              'message':'Inserted Sucessfully !',
                              'title':'success'
                         }
                    else:
                         data={
                              'success':200,
                              'icon':'Error',
                              'message':'Something went wrong !',
                              'title':'Error'
                         }
                    return http.JsonResponse(data,safe=False)
            except Exception as error:
                 print(error)
                 data={
                         'success':500,
                         'icon':'error',
                         'message':str(error),
                         'title':'error'
                 }
                 return http.JsonResponse(data,safe=False)
     return render (request,'Order-entry.html')
def order_service(request):
     order_details=models.order_entry.objects.values('Order_ID','Customer_ID')
     if request.POST:
          order_date=request.POST.get('order_date')
          order_id=request.POST.get('order_id')
          customer_id=request.POST.get('customer_id')
          conditions={}
          if order_date!="" and order_date is not None:
               conditions['Order_date']=order_date
          if order_id!="" and order_id is not None:
               conditions['Order_ID']=order_id
          if customer_id!="" and customer_id is not None:
               conditions['Customer_ID']=customer_id
          if conditions:
               filter_data=models.order_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render (request,'Order-service.html',{'order_details': order_details,'filter_data': filter_data})
     return render (request,'Order-service.html',{'order_details': order_details})
def order_update(request):
     return render (request,'Order-update.html')

# ORDER ITEM ENTRY----------------------------

def order_item_entry(request):
     if request.method=='POST':
        if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
            try:
                    order_item_id=request.POST.get('order_item_id')
                    if models.order_item_entry.objects.filter(
                         Order_Item_ID=order_item_id
                    ).exists():
                         return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Order Item ID already exists!',
                              'icon': 'warning'
                         })
                    order_id=request.POST.get('order_id')
                    product_id=request.POST.get('product_id')
                    quantity=request.POST.get('quantity')
                    Price=request.POST.get('Price')
                    disc_amount=request.POST.get('disc_amount')
                    Sub_Total=request.POST.get('Sub_Total')
                    order_item_obj=models.order_item_entry()
                    order_item_obj.Order_Item_ID=order_item_id
                    order_item_obj.Order_ID=order_id
                    order_item_obj.Product_ID=product_id
                    order_item_obj.Quantity=quantity
                    order_item_obj.Price=Price
                    order_item_obj.Disc_amount=disc_amount
                    order_item_obj.Sub_total=Sub_Total
                    order_item_obj.save()
                    if order_item_obj.pk is not None:
                         data={
                              'success':200,
                              'icon':'success',
                              'message':'Inserted Successfully !',
                              'title':'success'
                         }
                    else:
                          data={
                              'success':200,
                              'icon':'error',
                              'message':'something went wrong !',
                              'title':'error'
                         }

                    return http.JsonResponse(data,safe=False)
            except Exception as error:
                 print(error)
                 data={
                         'success':500,
                         'icon':'error',
                         'message':str(error),
                         'title':'error'
                 }
                 return http.JsonResponse(data,safe=False)

     return render (request,'order-item-entry.html')
def order_item_service(request):
     order_item_details=models.order_item_entry.objects.values('Order_Item_ID','Product_ID')
     if request.POST:
          order_item_id=request.POST.get('order_item_id')
          product_id=request.POST.get('product_id')
          order_id=request.POST.get('order_id')
          conditions={}
          if order_item_id!="" and order_item_id is not None:
               conditions['Order_Item_ID']=order_item_id
          if product_id!="" and product_id is not None:
               conditions['Product_ID']=product_id
          if order_id!="" and order_id is not None:
               conditions['Order_ID']=order_id
          if conditions:
               filter_data=models.order_item_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render (request,'order-item-service.html',{'order_item_details': order_item_details,'filter_data': filter_data})

     return render (request,'order-item-service.html',{'order_item_details': order_item_details})
def order_item_update(request):
     return render (request,'order-item-update.html')

# ORDER PAYMENT ENTRY----------------------------

def order_payment_entry(request):
     data={
          'title':'Order Payment Onboarding | G-Mart'
     }
     if request.method=='POST':
     #    print(request.POST)
      try:
        payment_date=request.POST.get('payment_date')
        payment_ID=request.POST.get('payment_ID')
        if models.Order_payment_entry.objects.filter(
             Payment_ID=payment_ID
        ).exists():
             return JsonResponse({
                    'success': 409,
                    'title': 'Already Exists',
                    'message': 'Order Payment ID already exists!',
                    'icon': 'warning'
             })
        order_ID=request.POST.get('order_ID')
        Customer_ID=request.POST.get('Customer_ID')
        paid_amount=request.POST.get('paid_amount')
        payment_mode=request.POST.get('payment_mode')
        balance=request.POST.get('balance')
        status=request.POST.get('status')
        remark=request.POST.get('remark')

        order_payment_obj=models.Order_payment_entry()
        order_payment_obj.Payment_date=payment_date
        order_payment_obj.Payment_ID=payment_ID
        order_payment_obj.Order_ID=order_ID
        order_payment_obj.Customer_ID=Customer_ID
        order_payment_obj.Paid_amount=paid_amount
        order_payment_obj.Payment_mode=payment_mode
        order_payment_obj.Balance=balance
        order_payment_obj.Status=status
        order_payment_obj.Remark=remark
        order_payment_obj.save()
        if order_payment_obj.pk is not None:
          data={
                    'success':200,
                    'title':'success',
                    'message':'Inserted Successfully !',
                    'icon':'success'
               }
        else:
             data={
                    'success':500,
                    'title':'Error',
                    'message':'Something Went Wrong !',
                    'icon':'error'
               }
        return http.JsonResponse(data,safe=False)
      except Exception as error:
           print(error)
           data={
                'success':500,
                'title':'Error',
                'message':str(error),
                'icon':'error'
           }
           return http.JsonResponse(data,safe=False)
     return render(request,"Order-payment-entry.html",{'data':data})
def order_payment_service(request):
     order_payment_details=models.Order_payment_entry.objects.values('Payment_ID','Order_ID')
     if request.POST:
          payment_date=request.POST.get('payment_date')
          payment_id=request.POST.get('payment_id')
          order_id=request.POST.get('order_id')
          conditions={}
          if payment_date!="" and payment_date is not None:
               conditions['Payment_date']=payment_date
          if payment_id!="" and payment_id is not None:
               conditions['Payment_ID']=payment_id
          if order_id!="" and order_id is not None:
               conditions['Order_ID']=order_id
          if conditions:
            filter_data=models.Order_payment_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render(request,'Order-payment-service.html',{'filter_data':filter_data,'order_payment_details':order_payment_details})

     return render(request,"Order-payment-service.html",{'order_payment_details':order_payment_details})
def order_payment_update(request):
     return render(request,"Order-payment-update.html")



# PRODUCT  ENTRY---------------------------

def Product_entry(request):
     # print(request.POST)
    if request.method=='POST':
      if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
          try:
               Entry_date=request.POST.get('Entry_date')
               product_ID=request.POST.get('product_ID')
               if models.product_entry.objects.filter(
                   Product_ID=product_ID
               ).exists():
                   return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Product ID already exists!',
                              'icon': 'warning'
                         })
               product_name=request.POST.get('product_name')
               Category_ID=request.POST.get('Category_ID')
               Status=request.POST.get('Status')
               product_obj=models.product_entry()
               product_obj.Entry_date=Entry_date
               product_obj.Product_ID=product_ID
               product_obj.Product_Name=product_name
               product_obj.Category_ID=Category_ID
               product_obj.Status=Status
               product_obj.save()
               if product_obj.pk is not None:  
                    data={
                         'success':200,
                         'message':'Inserted Succesfully !',
                         'title':'success',
                         'icon':'success'
                    }
               else:
                   data={
                         'success':200,
                         'message':'something went wrong !',
                         'title':'error',
                         'icon':'error'
                    }
               return http.JsonResponse(data,safe=False)
          except Exception as error:
            print(error)
            data={
                'success':500,
                'message':str(error),
                'title':'error',
                'icon':'error'
            }
            return http.JsonResponse(data,safe=False)

    return render (request,'Product-entry.html')
def Product_service(request):
     product_details=models.product_entry.objects.values('Product_ID')
     if request.POST:
          product_ID=request.POST.get('product_ID')
          product_name=request.POST.get('product_name')
          status=request.POST.get('status')
          conditions={}
          if product_ID !="" and product_ID is not None:
               conditions['Product_ID']=product_ID
          if product_name !="" and product_name is not None:
               conditions['Product_Name']=product_name
          if status !="" and status is not None:
               conditions['Status']=status
          if conditions:
            filter_data=models.product_entry.objects.filter(**conditions)
          else:
               filter_data=None

          return render (request,'Product-service.html',{'product_details':product_details,'filter_data':filter_data})
     return render (request,'Product-service.html',{'product_details':product_details})
def Product_update(request):
     return render (request,'Product-update.html')

# PURCHASE ITEM ENTRY----------------------------

def Purchase_Item_entry(request):
     if request.method=='POST':
        if request.META.get('HTTP_X_REQUESTED_WITH') =='XMLHttpRequest':
               try:
                    purchase_date=request.POST.get('purchase_date')
                    purchase_item_ID=request.POST.get('purchase_item_ID')
                    if models.purchase_item_entry.objects.filter(
                      Purchase_Item_ID=purchase_item_ID
                    ).exists():
                        return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Purchase Item ID already exists!',
                              'icon': 'warning'
                        })
                    supplier_ID=request.POST.get('supplier_ID')
                    category_id=request.POST.get('category_id')
                    product_id=request.POST.get('product_id')
                    quantity=request.POST.get('quantity')
                    purchase_unit_price=request.POST.get('purchase_unit_price')
                    unit_price=request.POST.get('unit_price')
                    sell_price=request.POST.get('sell_price')
                    gross_amount=request.POST.get('gross_amount')
                    purchase_obj=models.purchase_item_entry()
                    purchase_obj.Purchase_date=purchase_date
                    purchase_obj.Purchase_Item_ID=purchase_item_ID
                    purchase_obj.Supplier_ID=supplier_ID
                    purchase_obj.Category_ID=category_id
                    purchase_obj.Product_ID=product_id
                    purchase_obj.Quantity=quantity
                    purchase_obj.Purchase_unit_price=purchase_unit_price
                    purchase_obj.Unit_price=unit_price
                    purchase_obj.Sell_price=sell_price
                    purchase_obj.Gross_amount=gross_amount
                    purchase_obj.save()
                    if purchase_obj.pk is not None:
                         data={
                              'success':200,
                              'icon':'success',
                              'message':'Inserted successfully !',
                              'title':'success'

                              }
                    else:
                        data={
                              'success':200,
                              'icon':'error',
                              'message':'Something went wrong !',
                              'title':'error'

                              }
                    return http.JsonResponse(data,safe=False)
               except Exception as error:
                print(error)
                data={
                         'success':500,
                         'icon':'error',
                         'message':str(error),
                         'title':'error'
                }
               return http.JsonResponse(data,safe=False)


     return render(request,'purchase-item-entry.html')
     
def Purchase_Item_service(request):
     Purchase_Item_entry_details=models.purchase_item_entry.objects.values('Purchase_Item_ID','Supplier_ID')
     # print(Purchase_Item_entry_details)
     if request.POST:
          purchase_date=request.POST.get('purchase_date')
          purchase_item_ID=request.POST.get('purchase_item_ID')
          supplier_ID=request.POST.get('supplier_ID')
          conditions={}
          if purchase_date!="" and purchase_date is not None:
               conditions['Purchase_date']=purchase_date
          if purchase_item_ID!="" and purchase_item_ID is not None:
               conditions['Purchase_Item_ID']=purchase_item_ID
          if supplier_ID!="" and supplier_ID is not None:
               conditions['Supplier_ID']=supplier_ID
          if conditions:
               filter_data=models.purchase_item_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render (request,'Purchase-item-service.html',{'Purchase_Item_entry_details':Purchase_Item_entry_details,'filter_data':filter_data})

     return render (request,'Purchase-item-service.html',{'Purchase_Item_entry_details':Purchase_Item_entry_details})
def Purchase_Item_update(request):
     return render(request,'Purchase-item-update.html')


# PURCHASE ENTRY----------------------------

def Purchase_entry(request):
     if request.method=='POST':
          try:
                    purchase_date=request.POST.get('purchase_date')
                    Purchase_ID=request.POST.get('Purchase_ID')
                    supplier_ID=request.POST.get('supplier_ID')
                    total_amount=request.POST.get('total_amount')
                    Purchase_entry_obj=models.purchase_entry()
                    Purchase_entry_obj.Purchase_date=purchase_date
                    Purchase_entry_obj.Purchase_ID=Purchase_ID
                    Purchase_entry_obj.Supplier_ID=supplier_ID
                    Purchase_entry_obj.Total_amount=total_amount
                    Purchase_entry_obj.save()
                    if Purchase_entry_obj.pk is not None:  
                         data={
                              'success':200,
                              'message':'Inserted Successfully !',
                              'icon':'success',
                              'title':'success'
                         }
                    else:
                         data={
                              'success':200,
                              'message':'Something went wrong !',
                              'icon':'error',
                              'title':'error'
                         }
                    return http.JsonResponse(data,safe=False)
          except Exception as error:
              print(error)
              data={
                  'success':500,
                  'icon':'error',
                  'message':str(error),
                  'title':'error'
              }
              return http.JsonResponse(data,safe=False)
     return render(request,'Purchase-entry.html')
def Purchase_service(request):
     purchase_details=models.purchase_entry.objects.values('Supplier_ID')
     if request.POST:
          purchase_date=request.POST.get('purchase_date')
          Purchase_ID=request.POST.get('Purchase_ID')
          supplier_ID=request.POST.get('supplier_ID')
          conditions={}
          if purchase_date !="" and purchase_date is not None:
               conditions['Purchase_date']=purchase_date
          if Purchase_ID !="" and Purchase_ID is not None:
               conditions['Purchase_ID']=Purchase_ID
          if supplier_ID !="" and supplier_ID is not None:
               conditions['Supplier_ID']=supplier_ID
          if conditions:
               filter_data=models.purchase_entry.objects.filter(**conditions)
          else:
               filter_data=None
          return render (request,'Purchase-service.html',{'purchase_details':purchase_details,'filter_data':filter_data})
     return render (request,'Purchase-service.html',{'purchase_details':purchase_details})
def Purchase_update(request):
     return render(request,'Purchase-update.html')

# SUPPLIIER ENTRY----------------------------
def Supplier_entry(request):
     # print(request.POST)
     if request.method=='POST':
       if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
          try:
                    Entry_Date=request.POST.get('Entry_Date')
                    supplier_ID=request.POST.get('Supplier_ID')
                    if models.supplier_entry.objects.filter(
                         Supplier_ID=supplier_ID
                         ).exists():
                              return JsonResponse({
                              'success': 409,
                              'title': 'Already Exists',
                              'message': 'Supplier ID already exists!',
                              'icon': 'warning'
                         })
                    Name=request.POST.get('Supplier_Name')
                    Contact_number=request.POST.get('Contact_Number')
                    Email=request.POST.get('Email')
                    GST=request.POST.get('GST_Number')
                    Status=request.POST.get('Status')
                    State=request.POST.get('State')
                    District=request.POST.get('District')
                    Pin=request.POST.get('Pin')
                    Address=request.POST.get('Address')
                    # print(Entry_Date,supplier_ID,Name,Contact_number,Email,GST,Status,State,District,Pin,Address)
                    supplier_obj=models.supplier_entry()
                    supplier_obj.Entry_date=Entry_Date
                    supplier_obj.Supplier_ID=supplier_ID
                    supplier_obj.Name=Name
                    supplier_obj.Contact_Number=Contact_number
                    supplier_obj.Email=Email
                    supplier_obj.GST_Number=GST
                    supplier_obj.Status=Status
                    supplier_obj.State=State
                    supplier_obj.District=District
                    supplier_obj.Pin=Pin
                    supplier_obj.Address=Address
                    supplier_obj.save()
                    if supplier_obj.pk  is not None:
                    
                         data={
                         'success':200,
                         'title':'success',
                         'message':'Inserted Successsfully !',
                         'icon':'success'
                         }
                    else:
                        data={
                         'success':500,
                         'title':'error',
                         'message':'something went wrong !',
                         'icon':'error'
                         }
                        
                    return http.JsonResponse(data,safe=False)
          except Exception as error:
              print(error)
              data={
                  'success':500,
                  'title':'error',
                  'message':str(error),
                  'icon':'error'
              }
              return http.JsonResponse(data,safe=False)

     return render(request,'supplier-entry.html')
def Supplier_service(request):
     supplier_details=models.supplier_entry.objects.values('Supplier_ID')
     # print(supplier_details)
     if request.POST:
          Supplier_ID=request.POST.get('Supplier_ID')
          Supplier_Name=request.POST.get('Supplier_Name')
          Contact_Number=request.POST.get('Contact_Number')
          status=request.POST.get('status')
          conditions={}
          if Supplier_ID!=""and Supplier_ID is not None:
               conditions['Supplier_ID']=Supplier_ID
          if Supplier_Name!=""and Supplier_Name is not None:
               conditions['Name']=Supplier_Name
          if Contact_Number!=""and Contact_Number is not None:
               conditions['Contact_Number']=Contact_Number
          if status!=""and status is not None:
               conditions['Status']=status
          # print(conditions)
          if conditions:
            filter_data=models.supplier_entry.objects.filter(**conditions)
          else:
             filter_data = None 
          
          return render (request,'supplier-service.html',{'supplier_details':supplier_details,'filter_data':filter_data})

     return render (request,'supplier-service.html',{'supplier_details':supplier_details})
def Supplier_update(request,iid):
     data={
          'title':'Supplier Update'
     }
     try:
       update_data=models.supplier_entry.objects.get(Supplier_ID=iid)
       data['updatedata']=update_data
     except Exception as e:
          print(e)
     if request.method=='POST':
          updatedata=models.supplier_entry.objects.get(Supplier_ID=iid)
          updatedata.Entry_date=request.POST.get('Entry_Date')
          updatedata.Supplier_ID=request.POST.get('Supplier_ID')
          updatedata.Name=request.POST.get('Supplier_Name')
          updatedata.Contact_Number=request.POST.get('Contact_Number')
          updatedata.Email=request.POST.get('Email')
          updatedata.GST_Number=request.POST.get('GST_Number')
          updatedata.Status=request.POST.get('Status')
          updatedata.State=request.POST.get('State')
          updatedata.District=request.POST.get('District')
          updatedata.Pin=request.POST.get('Pin')
          updatedata.Address=request.POST.get('Address')
          updatedata.save()
          return redirect('supplier')


     return render(request,'supplier-update.html',{'data': data})

# USER PAYMENT ENTRY----------------------------
def User_payment_entry(request):
     if request.method == 'GET':
         if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
          if request.GET.get('for-what')=='User_payment_data':
               user_list=  models.user_entry.objects.values('User_ID')
               html=""
               for x in user_list:
                    # print(x['User_ID'])
                    html += f'<option value="{x["User_ID"]}">{x["User_ID"]}</option>'
          #  print(html)
               return http.JsonResponse(html,safe=False)
          return render(request,'user-payment-entry.html')

     if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
          # print(request.POST)
          Payment_Date=request.POST.get('Payment_Date')
          User_ID=request.POST.get('User_ID')
          Amount=request.POST.get('Amount')
          Payment_Mode=request.POST.get('Payment_Mode')
          Balance=request.POST.get('Balance')
          Status=request.POST.get('Status')
          # try:
          #     models.user_entry.objects.get(User_ID=User_ID)
          # except models.user_entry.DoesNotExist:
          #     http_response ={
          #          'status' : 500,
          #          'message':'User ID Not Found !',
          #          'error': 'User ID Not Found !'
                    
          #      }
          #     return http.JsonResponse(http_response,safe=False)
          # except Exception as error:
          #     print(error)
          #     http_response ={
          #          'status' : 500,
          #          'message':'Something Went Wrong !',
          #          'error': str(error)
                    
          #      }

          #     return http.JsonResponse(http_response,safe=False)
              
          try:
               user_payment_obj=models.user_payment()
               user_payment_obj.Payment_Date=Payment_Date
               # user_payment_obj.Payment_ID=Payment_ID
               user_payment_obj.User_ID=models.user_entry.objects.get(User_ID=User_ID)
               user_payment_obj.Amount=Amount
               user_payment_obj.Payment_mode=Payment_Mode
               user_payment_obj.Balance=Balance
               user_payment_obj.Status=Status
               user_payment_obj.save()
               http_response ={
                   'status' : 200,
                   'message':'Record Saved Succesfully !'
                    
               }

               return http.JsonResponse(http_response,safe=False)
          except Exception as error:
             print(str(error))
             http_response ={
                   'status' : 500,
                   'message':'Something went Wrong !',
                   'error': str(error)
                    
               }
             return http.JsonResponse(http_response,safe=False)

          
     return render(request,'user-payment-entry.html')
def User_payment_service(request):

     user_payment = models.user_payment.objects.all()
     filter_data = None

     if request.method == "POST":
        Payment_Date = request.POST.get('Payment_Date')
        Payment_ID = request.POST.get('Payment_ID')
        User_ID = request.POST.get('User_ID')

        conditions = {}

        if Payment_Date:
            conditions['Payment_Date'] = Payment_Date

        if Payment_ID:
            conditions['Payment_ID'] = Payment_ID

        if User_ID:
            conditions['User_ID__User_ID'] = User_ID

        print("FILTER CONDITIONS:", conditions)

        if conditions:
            filter_data = models.user_payment.objects.filter(**conditions)
        else:
            filter_data = None 
     return render (request,'user-payment-service.html',{'user_payment':user_payment,'filter_data':filter_data})
def userpaymentupdate(request,id):
     data={
          'title':'User Update'
     }
     try:
        updatedata = models.user_payment.objects.get(User_ID__User_ID=id)
     
        data['updatedata'] = updatedata
        
     except Exception as e:
          print(e)
     users=models.user_payment.objects.all()
     if request.method == 'POST':
             updatedata.Payment_Date= request.POST.get('Payment_Date')
             user_id = request.POST.get('User_ID')
             if user_id:
              updatedata.User_ID = models.user_entry.objects.get(User_ID=user_id)
             updatedata.Amount= request.POST.get('Amount')
             updatedata.Payment_mode= request.POST.get('Payment_Mode')
             updatedata.Balance= request.POST.get('Balance')
             updatedata.Status= request.POST.get('Status')
             updatedata.save()
             return redirect('userpayment')
     return render(request,'user-payment-update.html',{'data': data,'users':users})

def userpaymentdelete(request,id):
    try:
      models.user_payment.objects.get(User_ID=id).delete()
      return redirect('userpayment')
    except Exception as e:
        print(e)
        return render(request,'user-payment-service.html')
# add ons for admin panel
def page_account(request):
     return render(request,"pages-account-settings-account.html")
def page_connection(request):
     return render (request,"pages-account-settings-connections.html")
def page_notification(request):
     return render(request,"pages-account-settings-notifications.html")
# author
def auth_login(request):
     return render (request,"auth-login-basic.html")
def auth_registration(request):
     return render(request,"auth-register-basic.html")
def auth_forgot(request):
     return render(request,"auth-forgot-password-basic.html")
