from django.db import models
from crcapp.models import Employee,Customer,Store
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.utils import timezone

# Functions related to Customer
class CustomerController:
    # Developer: Tom, Sam and with fixes and debugging done by Aidan
    # Create a new customer
    def create(request):
        # Grab the customer with the largest customerID from the database
        custObj = Customer.objects.raw("SELECT customerID FROM `crcapp_customer` ORDER BY customerID DESC LIMIT 1")[0]
        custID = custObj.customerID#grab the customerID
        custID = custID[1:]
        custID = int(custID)+1#increment by one
        custID = str(custID).zfill(7)

        try:
            # Get all the form data and put into relted variables. Also prepare the other variables
            customerID_ = "C" + custID
            firstName_ = request.POST.get("firstName")
            lastName_ = request.POST.get("lastName")
            streetAddress_ = request.POST.get("streetAddress")
            cityAddress_ = request.POST.get("cityAddress")
            postCodeAddress_ = request.POST.get("postCodeAddress")
            stateAddress_ = request.POST.get("stateAddress")
            DOB_ = request.POST.get("DOB")
            driverLicenseNumber_ = request.POST.get("driverLicenseNumber")
            gender_ = request.POST.get("gender")
            occupation_ = request.POST.get("occupation")
            phoneNumber_ = request.POST.get("phoneNumber")
            email_ = request.POST.get("email")
            userName_ = request.POST.get("userName")
            password_ = make_password(request.POST.get('password', ''))
            dateJoined_ = timezone.now()
            lastLogin_ = timezone.now() 

            # Create a new customer
            newCustomer = Customer(
            customerID = customerID_,
            firstName = firstName_,
            lastName = lastName_,
            streetAddress = streetAddress_,
            cityAddress = cityAddress_,
            postCodeAddress = postCodeAddress_,
            stateAddress = stateAddress_,
            DOB = DOB_,
            driverLicenceNumber = driverLicenseNumber_,
            gender = gender_,
            occupation = occupation_,
            phoneNumber = phoneNumber_,
            email = email_,
            userName = userName_,
            password = password_,
            dateJoined = dateJoined_,
            lastLogin = lastLogin_,
            disable = 0)

            # Check that the new customer data is correct and valid
            vali = newCustomer.full_clean()

            if vali:#if errors occurred return those
                return vali
            else:#else the data must be valid and can therefore be saved to the database
                newCustomer.save()
                return True
        # If there is an error validating the data then return the error
        except ValidationError as e:
            return e

    # Developer Tom, Sam and with fixes and debugging done by Aidan
    def modify(request):
        try:
            # Get all the form data and put into relted variables. Also prepare the other variables
            customerID_ = request.POST.get("customerID")#supplied
            firstName_ = request.POST.get("firstName")#required
            lastName_ = request.POST.get("lastName")#required
            streetAddress_ = request.POST.get("streetAddress")#required
            cityAddress_ = request.POST.get("cityAddress")
            postCodeAddress_ = request.POST.get("postCodeAddress")
            stateAddress_ = request.POST.get("stateAddress")
            DOB_ = request.POST.get("DOB")#required
            driverLicenceNumber_ = request.POST.get("driverLicenseNumber")
            gender_ = request.POST.get("gender")#required
            occupation_ = request.POST.get("occupation")#required
            phoneNumber_ = request.POST.get("phoneNumber")#required
            email_ = request.POST.get("email")
            userName = request.POST.get("userName")
            password = request.POST.get("password")

            # Get the exisitng customer from the database
            existingCustomer = Customer.objects.get(customerID__exact=customerID_)

            # Update the details of the customer
            existingCustomer.firstName = firstName_
            existingCustomer.lastName = lastName_
            existingCustomer.streetAddress = streetAddress_

            # For each non-required integer field check if it contains a value and if so update accordingly
            if (postCodeAddress_ != ""):
                existingCustomer.postCodeAddress = postCodeAddress_
            else:
               existingCustomer.postCodeAddress = None

            existingCustomer.DOB = DOB_

            if (driverLicenceNumber_ != ""):
                existingCustomer.driverLicenceNumber = driverLicenceNumber_
            else:
                existingCustomer.driverLicenceNumber = None
            
            existingCustomer.gender = gender_
            existingCustomer.occupation = occupation_
            existingCustomer.phoneNumber = phoneNumber_
            
            # Check that the new customer details are correct and valid
            vali = existingCustomer.full_clean()

            if vali:#if errors occurred return those
                return vali
            else:#else the data must be valid and can therefore be saved to the database
                existingCustomer.save()
                return True
        # If there is an error validating the data then return the error
        except ValidationError as e:
            return e.message_dict

    # Developer : Sam
    # Deletes Customer based on given ID
    def delete(ID):
        x = Customer.objects.get(customerID = ID)
        x.delete()

    # Developer: Sam
    # Has a purpose that is only the Developer who wrote it remembers
    def search(arg):
        if(arg == "all"):
            for each in Customer.objects.all():
                return(
                each.customerID,
                each.firstName,
                each.lastName,
                each.streetAddress,
                each.cityAddress,
                each.postCodeAddress,
                each.stateAddress,
                each.DOB,
                each.driverLicenceNumber,
                each.gender,
                each.occupation,
                each.phoneNumber,
                each.email,
                each.userName,
                each.dateJoined,
                each.lastLogin)

        if(arg!= "all"):
            customerID_min = request.POST.get("customerID_min")
            customerID_max = request.POST.get("customerID_max")
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            streetAdress = request.POST.get("streetAdress")
            cityAddress = request.POST.get("cityAddress")
            postCodeAddress = request.POST.get("postCodeAddress")
            stateAddress = request.POST.get("stateAddress")
            DOB_min = request.POST.get("DOB_min")
            DOB_max = request.POST.get("DOB_max")
            driverLicenceNumber = request.POST.get("driverLicenceNumber")
            gender = request.POST.get("gender")
            occupation = request.POST.get("occupation")
            phoneNumber = request.POST.get("phoneNumber")
            email = request.POST.get("email")
            userName = request.POST.get("userName")
            dateJoined_min = request.POST.get("dateJoined_min")
            dateJoined_max = request.POST.get("dateJoined_max")
            lastLogin_min = request.POST.get("lastLogin_min")
            lastLogin_max = request.POST.get("lastLogin_max")

            condition = " "

            if (customerID_min != ""):
                condition = condition + "customerID >= \'" + customerID_min + "\' AND "
            if (customerID_max != ""):
                condition = condition + "customerID <= \'" + customerID_max + "\' AND "
            if (firstName != ""):
                condition = condition + "firstName LIKE \'%" + firstName + "%\' AND "
            if (lastName != ""):
                condition = condition + "lastName LIKE \'%" + lastName + "%\' AND "
            if (streetAdress != ""):
                condition = condition + "streetAdress LIKE \'%" + streetAdress + "%\' AND "
            if (cityAddress != ""):
                condition = condition + "cityAddress LIKE \'%" + cityAddress + "%\' AND "
            if (postCodeAddress != ""):
                condition = condition + "postCodeAddress = \'" + postCodeAddress + "\' AND "
            if (stateAddress != ""):
                condition = condition + "stateAddress = \'" + stateAddress + "\' AND "
            if (DOB_min != ""):
                condition = condition + "DOB >= \'" + DOB_min + "\' AND "
            if (DOB_max != ""):
                condition = condition + "DOB <= \'" + DOB_max + "\' AND "
            if (driverLicenceNumber != ""):
                condition = condition + "driverLicenceNumber = \'" + driverLicenceNumber + "\' AND "
            if (gender != ""):
                condition = condition + "gender = \'" + gender + "\' AND "
            if (occupation != ""):
                condition = condition + "occupation LIKE \'%" + occupation + "\' AND "
            if (phoneNumber != ""):
                condition = condition + "phoneNumber = \'" + phoneNumber + "\' AND "
            if (email != ""):
                condition = condition + "email = \'" + email + "\' AND "
            if (userName != ""):
                condition = condition + "userName = \'" + userName + "\' AND "
            if (dateJoined_min != ""):
                condition = condition + "dateJoined >= \'" + dateJoined_min + "\' AND "
            if (dateJoined_max != ""):
                condition = condition + "dateJoined <= \'" + dateJoined_max + "\' AND "
            if (lastLogin_min != ""):
                condition = condition + "lastLogin >= \'" + lastLogin_min + "\' AND "
            if (lastLogin_max != ""):
                condition = condition + "lastLogin <= \'" + lastLogin_max + "\' AND "

            query = 'SELECT * FROM carrentaldb.crcapp_customer WHERE' + condition[:-5] +';'

            for each in Customer.objects.raw(query):
                return(
                each.customerID,
                each.firstName,
                each.lastName,
                each.streetAddress,
                each.cityAddress,
                each.postCodeAddress,
                each.stateAddress,
                each.DOB,
                each.driverLicenceNumber,
                each.gender,
                each.occupation,
                each.phoneNumber,
                each.email,
                each.userName,
                each.dateJoined,
                each.lastLogin)

    # Developer : Aidan
    # To change the password of a customer
    def changePW(request):
        customerID_ = request.POST.get("customerID")
        password_ = make_password(request.POST.get('password', ''))

        existingCustomer = Customer.objects.get(customerID=customerID_)

        try:
            existingCustomer.password = password_
            
            vali = existingCustomer.full_clean()
            if vali:
                return vali
            else:
                existingCustomer.save()
                return True 
            return False
        except ValidationError as e:
            return e.message_dict