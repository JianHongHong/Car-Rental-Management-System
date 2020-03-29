from .modules import *

# Developer: Aidan
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)
        
# Developer: Aidan
# Loading the index page
def index(request, messages="", mtype="i"):
    # Will get the session variables for the message
    # and delete it after wards
    msg = request.session.get('msg', '')
    mtp = request.session.get('mtype', '')
    if msg != "":
        messages =  msg
        del request.session['msg']
    if mtp != "":
        mtype = mtp
        del request.session['mtype']
    
    stores = Store.objects.all()
    vehicles = Vehicle.objects.order_by('-vehicleID')[:6]
    todaysDate = timezone.now()
    return render(request, 'public/index.html', {'msg': messages, 'mtype': mtype, 'stores': stores, 'vehicles': vehicles, 'todaysDate': todaysDate})

# Developer: Aidan
# Login page 
def loginIndex(request, messages="", mtype="i"):
     # Will get the session variables for the message
    # and delete it after wards
    msg = request.session.get('msg', '')
    mtp = request.session.get('mtype', '')
    if msg != "":
        messages =  msg
        del request.session['msg']
    if mtp != "":
        mtype = mtp
        del request.session['mtype']
    return render(request, 'public/login.html', {'msg': messages, 'mtype': mtype})

# Developer: Aidan
# Login page 
def registerIndex(request, messages="", mtype="i"):
    if request.method == 'POST':
        form = request.POST
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        # If the reason is true it means verification failed
        if reason:
            return render(request, 'public/register.html', {'msg': 'Token verification failed!', 'mtype': "d"})
        else:
            if request.POST.get("password") == request.POST.get("confirmpassword"):
               
                result = customer.CustomerController.create(request)
                if result == True:
                    return render(request, 'public/register.html', {'msg': 'Account created, please login.', 'mtype': "i"})
                elif result == False:
                    return render(request, 'public/register.html', {'msg': 'Opps, something went wrong. Please try again.', 'mtype': "d"})
                else:
                    return render(request, 'public/register.html', {'msg': result, 'mtype': "a"})
            else:
                return render(request, 'public/register.html', {'msg': 'Sorry, the passwords did not match.', 'mtype': "i"})
        return render(request, 'public/register.html', {'msg': messages, 'mtype': mtype})
    else:

        return render(request, 'public/register.html', {'msg': messages, 'mtype': mtype})

# Developer: Jax
# Display all the Stores that are in the Database 
def storesIndex(request, messages="", mtype="i"):
    NSW = Store.objects.filter(state = "New South Wales")
    QLD = Store.objects.filter(state = "Queensland")
    SA = Store.objects.filter(state = "South Australia")
    TAS = Store.objects.filter(state = "Tasmania")
    VIC = Store.objects.filter(state = "Victoria")

    return render(request, 'public/stores.html', {'msg': messages, 'mtype': mtype, 'NSW': NSW, 'QLD': QLD, 'SA': SA, 'TAS' : TAS, 'VIC' : VIC })

# Developer: Aidan
# Display all Vehicles that are in the Database 
def vehicleIndex(request, messages="", mtype="i"):
    vehicles_list = Vehicle.objects.order_by('-vehicleID')
    page = request.GET.get('page', 1)

    paginator = Paginator(vehicles_list, 18)
    try:
        vehicles = paginator.page(page)
    except PageNotAnInteger:
        vehicles = paginator.page(1)
    except EmptyPage:
        vehicles = paginator.page(paginator.num_pages)

    return render(request, 'public/vehicles.html', {'msg': messages, 'mtype': mtype, 'vehicles': vehicles })

# Developer: Aidan
# Customer Profile Page
def profileIndex(request, messages="", mtype="i"):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        
        msg = request.session.get('msg', '')
        mtype = request.session.get('mtp', '')
        if msg != "":
            messages =  msg
            del request.session['msg']
        if mtype != "":
            del request.session['mtp']
        customer = Customer.objects.get(customerID=request.session['uid'])
        orders = Order.objects.filter(customerID=request.session['uid']).all()
        
        return render(request, 'public/profile.html', {'msg': messages, 'mtype': mtype,'name': name, 'utype': utype, 'customer': customer, 'orders':orders})
    else:
       return notLoggedIn(request)

# Developer: Aidan
# Setting stores to the order
def setStore(request):
    if request.method == 'POST':
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        # If the reason is true it means verification failed
        if reason:
            return redirect('/')
        else:
            bookings = { 'pickUpStore':request.POST.get("pickUpStore") , 'returnStore': request.POST.get("returnStore"),
             'pickupdate':request.POST.get("pickupdate") , 'returndate': request.POST.get("returndate")}
            request.session['bookings'] =bookings 
            return redirect('/booking')
    return redirect('/')

# Developer: Aidan
# # Confirming order
def confirmOrder(request):
    if request.session.has_key('bookings'):
        booking = request.session.get('bookings', '')
        
        pickupStore = Store.objects.get(storeID= booking['pickupStore'])
        returnStore = Store.objects.get(storeID= booking['returnStore'])
        vehicles = Vehicle.objects.filter(storeID = booking['pickUpStore'] )
        returnDate = booking['returndate']
        pickupDate = booking['pickupdate']
        return render(request, 'public/booking.html', {'bookings': booking, 'vehicles': vehicles, 'returnStore': returnStore, 'pickupStore': pickupStore,
        'pickupDate':pickupDate, 'returnDate':returnDate, "reco": recommendations})
    else:
        return redirect("/")

# Developer: Aidan
# get vehicle details to modify page
def getVehicleIndex(request, option, msg='',mtype=''):
    vehicle = Vehicle.objects.filter(vehicleID=option).values()[0]
    if vehicle['storeID_id'] != "":
        store = Store.objects.get(storeID = vehicle['storeID_id'] )
    else:
        store = { 'storeName' : "Not Found" }            
    return render(request, 'public/vehicle.html', {'msg': '', 'mtype': mtype, 'vehicle':vehicle, 'store':store})

# Developer: Aidan
# will return a json arrray of the login usernames
@csrf_exempt # to disable csrf token check
def getUsernamesCustomers(request):
    # Checking session exists
     
    if request.method == 'POST':
        customer = Customer.objects.all()
        return HttpResponse(serialize('json', customer, cls=LazyEncoder))
       
    else:
        return HttpResponse("NULL")


    
# Developer: Aidan
# Change user profile
def changeProfile(request):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Customer":
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    messages = "Token verification failed."
                    request.session['msg'] = messages
                    request.session['mtp'] = 'd'
                    return redirect('/profile')
                else:
                    result = customer.CustomerController.modify(request)
                    if result == True:
                        messages = "Profile saved."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'i'
                        return redirect('/profile')
                    elif result == False:
                        messages = "Opps, something happened, please try again later."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'd'
                        return redirect('/profile')
                    else:
                        messages = result
                        request.session['msg'] = messages
                        request.session['mtp'] = 'a'
                        return redirect('/profile')
            
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)

# Developer: Aidan
# Change user passwords
def changeProfilePassword(request):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Customer":
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    messages = "Token verification failed."
                    request.session['msg'] = messages
                    request.session['mtp'] = 'd'
                    return redirect('/profile')
                else:
                    result = customer.CustomerController.changePW(request)
                    if result == True:
                        messages = "Profile saved."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'i'
                        return redirect('/profile')
                    elif result == False:
                        messages = "Opps, something happened, please try again later."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'd'
                        return redirect('/profile')
                    else:
                        messages = result
                        request.session['msg'] = messages
                        request.session['mtp'] = 'a'
                        return redirect('/profile')
            
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)

# Developer: Aidan
# # Confirming order
def proceedOrder(request):    

    if request.session.has_key('bookings'):
        booking = request.session.get('bookings', '')

        pickupStoreID = booking['pickUpStore']
        recommendations = getRecommendations(pickupStoreID)
        
        pickupStore = Store.objects.get(storeID= pickupStoreID)
        returnStore = Store.objects.get(storeID= booking['returnStore'])
        vehicles = Vehicle.objects.filter(storeID = pickupStore )
        returnDate = booking['pickupdate']
        pickupDate = booking['returndate']
        return render(request, 'public/booking.html', {'bookings': booking, 'vehicles': vehicles, 'returnStore': returnStore, 'pickupStore': pickupStore,
     'pickupDate':pickupDate, 'returnDate':returnDate, 'reco': recommendations}) 
    else:
        return redirect("/")

# Developer: Tom
# Get recommendations
def getRecommendations(pickupStoreID):
    query = '''SELECT crcapp_vehicle.vehicleID, crcapp_vehicle.makeName, crcapp_vehicle.model,
            crcapp_vehicle.series, crcapp_vehicle.`year`, crcapp_vehicle.newPrice, crcapp_vehicle.enginesize,
            crcapp_vehicle.fuelSystem, crcapp_vehicle.tankcapacity, crcapp_vehicle.power, crcapp_vehicle.seatingCapacity,
            crcapp_vehicle.standardTransmission, crcapp_vehicle.bodyType, crcapp_vehicle.driveType, crcapp_vehicle.wheelbase,
            crcapp_vehicle.storeID_id
            FROM crcapp_orderfor
            JOIN crcapp_order ON crcapp_orderfor.orderID_id = crcapp_order.orderID
            JOIN crcapp_vehicle ON crcapp_orderfor.vehicleID_id = crcapp_vehicle.vehicleID
            WHERE MONTH(orderDate) = MONTH(current_date())
            AND pickupSTOREID_id = %s
            AND crcapp_vehicle.storeID_id = crcapp_order.pickupStoreID_id'''
    return Vehicle.objects.raw(query, [pickupStoreID])

# Developer: Aidan
# Setting stores to the order
def setStore(request):
    if request.method == 'POST':
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        # If the reason is true it means verification failed
        if reason:
            return redirect('/')
        else:
            bookings = { 'pickUpStore':request.POST.get("pickUpStore") , 'returnStore': request.POST.get("returnStore"),
             'pickupdate':request.POST.get("pickupdate") , 'returndate': request.POST.get("returndate")}
            request.session['bookings'] =bookings 
            return redirect('/booking')
    return redirect('/')

@csrf_exempt
def addVehicleToOrder(request, option):
    if  request.session.has_key('bookings'):
        booking = request.session.get('bookings', '')
        if option != "":
            booking['vehicleID'] = option
            request.session['bookings'] =booking 
            return HttpResponse("True")
        
    return HttpResponse("NULL")


@csrf_exempt
def confirmOrder(request):
    if  request.session.has_key('bookings'):
        
        result = orders.OrderController.create(request)
        if result == True:
            del request.session['bookings']
            return HttpResponse("True")
        else:
            return HttpResponse("False")
    return HttpResponse("NULL")


@csrf_exempt
def cancelOrder(request):
    if request.session.has_key('bookings'):
            del request.session['bookings']
            return HttpResponse("True")
    else:    
        return HttpResponse("NULL")