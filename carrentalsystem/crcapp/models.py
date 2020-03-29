from django.db import models
from django.core.validators import validate_email

# Store Model
class Store(models.Model):
    storeID = models.CharField(max_length=10, primary_key=True)
    storeName = models.CharField(max_length=50)
    storePhone = models.BigIntegerField()
    street = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length = 30)

    def __str__(self):
        return self.storeName

# Customer Model
# Developer: Tom, Sam
class Customer(models.Model):
    customerID = models.CharField(max_length=10, primary_key=True)#required
    firstName = models.CharField(max_length=80)#required
    lastName = models.CharField(max_length=80)#required
    streetAddress = models.CharField(max_length=50)#required
    cityAddress = models.CharField(max_length=16, blank=True, default="")
    postCodeAddress = models.PositiveIntegerField(blank=True, null=True)
    stateAddress = models.CharField(max_length = 30, blank=True, default="")
    DOB = models.DateField(auto_now=False, auto_now_add=False)#required
    driverLicenceNumber = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=2)#required
    occupation = models.CharField(max_length=50)#required
    phoneNumber = models.BigIntegerField()#required
    email = models.EmailField(validators=[validate_email], blank=True, default="")
    userName = models.CharField(max_length=50, blank=True, default="")
    password = models.TextField(max_length=50, blank=True, default="")
    dateJoined = models.DateField(auto_now=False, auto_now_add=True)
    lastLogin = models.DateField(auto_now=False, auto_now_add=True)    
    disable = models.BooleanField(default=0)


# Employee Model
class Employee(models.Model):
    employeeID = models.CharField(max_length=10, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    streetAddress = models.CharField(max_length=50)
    cityAddress = models.CharField(max_length=50)
    postCodeAddress = models.IntegerField()
    stateAddress = models.CharField(max_length = 50)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    TFN = models.BigIntegerField()
    phoneNumber = models.BigIntegerField()
    email = models.EmailField(validators=[validate_email])
    userName = models.CharField(max_length=50,null=True)
    password = models.TextField(null=True)
    userType = models.CharField(max_length=16)
    dateJoined = models.DateField()
    lastLogin = models.DateField()
    disable = models.BooleanField(default=0)
    storeID = models.ForeignKey(Store, on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName

# Vehicle Model
class Vehicle(models.Model):
    vehicleID = models.CharField(max_length=10, primary_key=True)
    makeName = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    series = models.CharField(max_length = 50)
    year = models.IntegerField()
    newPrice = models.DecimalField(max_digits=10,decimal_places=2)
    enginesize = models.DecimalField(max_digits=4,decimal_places=1)
    fuelSystem = models.CharField(max_length=50)
    tankcapacity = models.DecimalField(max_digits=7,decimal_places=1)
    power = models.IntegerField()
    seatingCapacity = models.IntegerField()
    standardTransmission = models.CharField(max_length=50)
    bodyType = models.CharField(max_length=50)
    driveType = models.CharField(max_length=30)
    wheelbase = models.IntegerField()
    storeID = models.ForeignKey(Store, on_delete=models.DO_NOTHING,blank=True,null=True)

# Inspect Model
class Inspects(models.Model):
    employeeID = models.ForeignKey(Employee, on_delete=models.DO_NOTHING,blank=True,null=True)
    vehicleID = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING,blank=True,null=True)
    class Meta:
        unique_together = ('employeeID', 'vehicleID')

# Order Model
class Order(models.Model):
    orderID = models.CharField(max_length=12, primary_key=True)
    orderDate = models.DateField(auto_now=False, auto_now_add=False)
    pickupDate = models.DateField(auto_now=False, auto_now_add=False)
    returnDate = models.DateField(auto_now=False, auto_now_add=False)
    orderType = models.CharField(max_length=16)
    customerID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING,blank=True,null=True)
    pickupStoreID = models.ForeignKey(Store, related_name="pickupstore", on_delete=models.DO_NOTHING,blank=True,null=True)
    returnStoreID = models.ForeignKey(Store, related_name="returnstore", on_delete=models.DO_NOTHING,blank=True,null=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.DO_NOTHING,blank=True,null=True)

# Many to many for order and vehicle
class OrderFor(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.DO_NOTHING,blank=True,null=True)
    vehicleID = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING,blank=True,null=True)
    class Meta:
        unique_together = ('orderID', 'vehicleID')

# Invoice Model
class Invoice(models.Model):
    invoiceID = models.CharField(max_length=10, primary_key=True)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    paymentType = models.CharField(max_length=20)
    orderID = models.ForeignKey(Order, on_delete=models.DO_NOTHING,blank=True,null=True)
