import uuid
from django.db import models

# Create your models here.(1)
class user_entry(models.Model):
     Joining_date= models.DateField(auto_now_add=True)
     User_ID=models.IntegerField(unique=True, default=None, null=True)
     Name=models.CharField(max_length=100)
     Father_name=models.CharField(max_length=100)
     Mother_name=models.CharField(max_length=100)
     Gender=models.CharField(max_length=50)
     DOB=models.DateField()
     contact_number=models.CharField(max_length=20)
     Alternate_number=models.CharField(max_length=20)
     Email_ID=models.EmailField(max_length=100)
     aadhaar_number=models.CharField(max_length=100)
     highest_qualifiication=models.CharField(max_length=100)
     position=models.CharField(max_length=50)
     salary=models.IntegerField()
     status=models.CharField(max_length=50)
     state=models.CharField(max_length=50)
     district=models.CharField(max_length=50)
     pin=models.CharField(max_length=20)
     address=models.CharField(max_length=500)
     Corr_State=models.CharField(max_length=50,default="not available")
     Corr_District=models.CharField(max_length=50,default="not available")
     Corr_Pin=models.CharField(max_length=20,default="not available")
     corr_address=models.CharField(max_length=500,default="not available")
     photo=models.ImageField(upload_to='photos/',null=True,blank=True)
     aadhaar_pic=models.ImageField(upload_to='aadhaar/',null=True,blank=True)
     signature=models.ImageField(upload_to='signatures/',null=True,blank=True)
     certificate=models.ImageField(upload_to='certificates/',null=True,blank=True)

     def __str__(self):
          return self.Name

# database for user Payment-----------(2)
class user_payment(models.Model):
      Payment_Date=models.DateField(auto_now_add=True)
      Payment_ID=models.AutoField(primary_key=True)
      User_ID=models.ForeignKey(user_entry,on_delete=models.PROTECT,null=True)
      Amount=models.CharField(max_length=50)
      Payment_mode=models.CharField(max_length=50)
      Balance=models.CharField(max_length=50)
      Status=models.CharField(max_length=50)

      def __str__(self):
            return str(self.Payment_ID)
# database for category-----------(3)
class category_entry(models.Model):
          Entry_date=models.DateField(auto_now=True)
          Category_ID=models.IntegerField(unique=True)
          Category_name=models.CharField(max_length=50)
          User_ID=models.CharField(max_length=50)
          Order_ID=models.CharField(max_length=100)
          Status=models.CharField(max_length=20)
          Description=models.CharField(max_length=500)
          def __str__(self):
               return str(self.Category_ID)

# database for supplier-----------(4)
class supplier_entry(models.Model):
      Entry_date=models.DateField(auto_now=True)
      Supplier_ID=models.CharField(max_length=50,unique=True)
      Name=models.CharField(max_length=50)
      Contact_Number=models.CharField(max_length=50)
      Email=models.EmailField(max_length=50)
      GST_Number=models.CharField(max_length=50)
      Status=models.CharField(max_length=50)
      State=models.CharField(max_length=50)
      District=models.CharField(max_length=50)
      Pin=models.CharField(max_length=50)
      Address=models.CharField(max_length=500)

      def __str__(self):
            return str(self.Supplier_ID)

# database for product-----------(5)    
class product_entry(models.Model):
      Entry_date=models.DateField(auto_now=True)
      Product_ID=models.CharField(max_length=50,unique=True)
      Product_Name=models.CharField(max_length=50)
      Category_ID=models.CharField(max_length=50)
      Status=models.CharField(max_length=50)

      def __str__(self):
            return str(self.Product_ID)
      
# database for purchse_Item-----------(6)    
class purchase_item_entry(models.Model):
      Purchase_date=models.DateField(auto_now=True)
      Purchase_Item_ID=models.CharField(max_length=50,unique=True)
      Supplier_ID=models.CharField(max_length=50)
      Category_ID=models.CharField(max_length=50)
      Product_ID=models.CharField(max_length=50)
      Quantity=models.CharField(max_length=50)
      Purchase_unit_price=models.CharField(max_length=50)
      Unit_price=models.CharField(max_length=50)
      Sell_price=models.CharField(max_length=50)
      Gross_amount=models.CharField(max_length=50)

      def __str__(self):
           return str(self.Purchase_Item_ID)
      
# database for purchse-----------(7)    
class purchase_entry(models.Model):
      Purchase_date=models.DateField(auto_now=True)
      Purchase_ID=models.CharField(max_length=50,unique=True)
      Supplier_ID=models.CharField(max_length=50)
      Total_amount=models.CharField(max_length=50)

      def __str__(self):
           return str(self.Purchase_ID)
      

# database for Customer-----------(8)    
class customer_entry(models.Model):
      Created_at=models.DateField(auto_now=True)
      Customer_ID=models.CharField(max_length=50,unique=True)
      Name=models.CharField(max_length=100)
      Contact_number=models.CharField(max_length=50)
      Email=models.EmailField(max_length=50)
      Status=models.CharField(max_length=50)
      State=models.CharField(max_length=50)
      District=models.CharField(max_length=50)
      Pin=models.CharField(max_length=20)
      Address=models.CharField(max_length=500)

      def __str__(self):
            return str(self.Customer_ID)

# database for Order-----------(9)    
class order_entry(models.Model):
      Order_date=models.DateField(auto_now_add=True)
      Order_ID=models.CharField(max_length=50,unique=True)
      User_ID=models.CharField(max_length=50)
      Customer_ID=models.CharField(max_length=50)
      Amount=models.CharField(max_length=50)
      Disc_amount=models.CharField(max_length=50)
      tax=models.CharField(max_length=50)
      pay_amount=models.CharField(max_length=50)
      Status=models.CharField(max_length=20)

      def __str__(self):
            return str(self.Order_ID)
      
# database for Order_Item-----------(10)    
class order_item_entry(models.Model):
      Order_Item_ID=models.CharField(max_length=50,unique=True)
      Order_ID=models.CharField(max_length=50)
      Product_ID=models.CharField(max_length=50)
      Quantity=models.CharField(max_length=50)
      Price=models.CharField(max_length=50)
      Disc_amount=models.CharField(max_length=50)
      Sub_total=models.CharField(max_length=50)

      def __str__(self):
            return str(self.Order_Item_ID)
      
# database for Order_Payment----------- (11)   
class Order_payment_entry(models.Model):
      Payment_date=models.DateField(auto_now_add=True)
      Payment_ID=models.CharField(max_length=50,unique=True)
      Order_ID=models.CharField(max_length=50)
      Customer_ID=models.CharField(max_length=50)
      Paid_amount=models.CharField(max_length=50)
      Payment_mode=models.CharField(max_length=50)
      Balance=models.CharField(max_length=50)
      Status=models.CharField(max_length=50)
      Remark=models.CharField(max_length=500)

      def __str__(self):
            return str(self.Payment_ID)   

class state(models.Model):
      state=models.CharField(max_length=100)
      district=models.CharField(max_length=100,null=True) 



       
