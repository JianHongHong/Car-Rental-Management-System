from crcapp.models import Employee,Customer,Store, Order, OrderFor, Vehicle
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.utils import timezone

# Create functions related to staff
class OrderController:

    # Developer: Aidan
    def create(request):
        orderObj = Order.objects.raw("SELECT orderID FROM `crcapp_order` ORDER BY orderID DESC LIMIT 1")[0]
        orderID = orderObj.orderID #grab the orderID
        orderID = orderID[1:]
        orderID = int(orderID)+1#increment by one
        orderID = str(orderID).zfill(6)
        booking = request.session.get('bookings', '')
        try:
            # Get all the form data and put into relted variables. Also prepare the other variables
            orderID_ = "O" + orderID
            customerID_ = request.session.get("uid") 
            orderDate_ = timezone.now()
            orderType_ = "Online"
            pickUpDate_ = booking["pickupdate"]
            pickUpStore_ = booking["pickUpStore"] 
            returnDate_ = booking["returndate"]
            returnStore_ = booking["returnStore"]

            customer = Customer.objects.get(customerID=customerID_)
            pickupStore = Store.objects.get(storeID=pickUpStore_)
            returnStore = Store.objects.get(storeID=returnStore_)


            vehicleID_ = booking["vehicleID"]
            vehicle = Vehicle.objects.get(vehicleID=vehicleID_)

            # Create a new customer
            newOrder = Order(
            customerID = customer,
            orderID = orderID_,
            orderDate = orderDate_,
            orderType = orderType_,
            pickupDate = pickUpDate_,
            pickupStoreID = pickupStore,
            returnDate = returnDate_,
            returnStoreID = returnStore)

            orderFor = OrderFor( orderID = newOrder, vehicleID = vehicle)
            # Check that the new customer data is correct and valid
            vali = newOrder.full_clean()

            if vali:#if errors occurred return those
                return vali
            else:#else the data must be valid and can therefore be saved to the database
                newOrder.save()
                orderFor.save()
                return True
        # If there is an error validating the data then return the error
        except ValidationError as e:
            return e