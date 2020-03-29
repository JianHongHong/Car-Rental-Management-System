from .modules import *

# Developer: Aidan
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)

# Developer Aidan
# Customer Profile Page
def profile(request, messages="", mtype="i"):
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
        staff = Employee.objects.get(employeeID=request.session['uid'])
        
        return render(request, 'staff/profile.html', {'msg': messages, 'mtype': mtype,'name': name, 'utype': utype, 'staff': staff})
    else:
       return notLoggedIn(request)

# Developer: Jax
# Staff stores page 
def storesStaff(request, messages="", mtype="i"):
    NSW = Store.objects.filter(state = "New South Wales")
    QLD = Store.objects.filter(state = "Queensland")
    SA = Store.objects.filter(state = "South Australia")
    TAS = Store.objects.filter(state = "Tasmania")
    VIC = Store.objects.filter(state = "Victoria")

    return render(request, 'store/storeLocation.html', {'msg': messages, 'mtype': mtype, 'NSW': NSW, 'QLD': QLD, 'SA': SA, 'TAS' : TAS, 'VIC' : VIC })

# Developer: Aidan
# Loading the home page
def home(request, messages=""):
    # Checking session exists
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
        counts = { 'vehicles': Vehicle.objects.all().count(), 
        'stores': Store.objects.all().count(), 
        'customers': Customer.objects.all().count(), 
        'orders': Order.objects.all().count() }
        return render(request, 'home.html', {'msg': messages, 'mtype': mtype,'name': name, 'utype': utype, 'counts': counts})
    else:
       return notLoggedIn(request)
    
# Developer: Aidan
# Form action class for login, this will be used for employee login only
def login(request):
    if request.method == 'POST':
        form = request.POST
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        if reason:
            messages = "Token verification failed."
            request.session['msg'] = messages
            request.session['mtype'] = 'd'
            return redirect('/login')
        else:
            result = authentication.Authentication.login(request)
            if result != "NULL":
                if request.session['utype'] == "Customer":
                    return  redirect("/profile")
                else:
                    return redirect("/management/home")
            elif result == "NULL":
                messages = "Login failed."
                request.session['msg'] = messages
                request.session['mtype'] = 'd'
                return redirect('/login')
            else:
                messages = result
                request.session['msg'] = messages
                request.session['mtype'] = 'd'
                return redirect('/login')
    else:
        messages = "Opps, something went wrong."
        request.session['msg'] = messages
        request.session['mtype'] = 'd'
        return redirect('/login')

# Developer: Aidan
@csrf_exempt # to disable csrf token check
def disableStaff(request, option, empID):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            staff = Employee.objects.get(employeeID = empID)
            if option == "disable":
                staff.disable = 1
            else:
                staff.disable = 0
            staff.save()
            return redirect('/management/staff/login/'+empID)
        else:
            return accessDeniedHome(request)
    else:
        return notLoggedIn(request)

# Developer: Jax
# Create staff member page
def staffCreate(request, messages="", mtype=""):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            stores = Store.objects.all()
            if request.method == 'POST':
                form = request.POST
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    return render(request, 'staff/create.html', {'msg': 'Token verification failed!', 'mtype': "d"})
                else:
                    result = staff.StaffController.createStaff(request)
                    if result == True:
                        return render(request, 'staff/create.html', {'msg': 'Staff created.', 'mtype': "i"})
                    elif result == False:
                        return render(request, 'staff/create.html', {'msg': 'Staff creation failed.', 'mtype': "d"})
                    else:
                        return render(request, 'staff/create.html', {'msg': result, 'mtype': "a"})
            elif request.method == "GET":
                return render(request, 'staff/create.html', {'msg': messages, 'name': name, 'mtype': mtype, 'utype': utype, "stores": stores})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)

# Developer: Aidan
# get all staff
def getAllStaff(request, messages="", mtype=""):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            stores = Store.objects.all()
            employees = Employee.objects.all()
            return render(request, 'staff/staffmanagementview.html', {'msg': messages, 'name': name, 'mtype': mtype, 'utype': utype, "employees":employees, "stores": stores})
        else:
            accessDeniedHome(request)
    else:
       notLoggedIn(request)

# Developer: Aidan
# save changes of staff
def changeStaffDetails(request, option,  name, utype, msg='',mtype=''):
    utype = request.session['utype']
    if utype == "Manager" or utype == "Developer":
        if request.method == 'POST':
            employee = Employee.objects.filter(employeeID=option).values()[0]
            stores = Store.objects.all()
            reason = CsrfViewMiddleware().process_view(request, None, (), {})
            # If the reason is true it means verification failed
            if reason:
                return render(request, 'staff/staffdetailview.html', {'name': name, 'utype': utype,'msg': 'Token verification failed!', 'mtype': "d",'employee':employee, 'stores':stores})
            else:
                result = staff.StaffController.modify(request)
                if result == True:
                    return render(request, 'staff/staffdetailview.html', {'name': name, 'utype': utype,'msg': 'Changes saved.', 'mtype': "i",'employee':employee, 'stores':stores})
                elif result == False:
                    return render(request, 'staff/staffdetailview.html', {'name': name, 'utype': utype,'msg': 'Could not save all changes.', 'mtype': "d",'employee':employee, 'stores':stores})
                else:
                    return render(request, 'staff/staffdetailview.html', {'name': name, 'utype': utype,'msg': result, 'mtype': "a", 'employee':employee, 'stores':stores})
    else:
        return accessDeniedHome(request)

# Developer: Aidan
# get start details to the staff management page
def getStaff(request, option, msg='', mtype=''):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            if request.method == 'POST':
                return changeStaffDetails(request, option, msg, mtype, name, utype)
            elif request.method == 'GET':
                employee = Employee.objects.filter(employeeID=option).values()[0]
                stores = Store.objects.all()
                
                return render(request, 'staff/staffdetailview.html', {'name': name, 'utype': utype,  'msg': '', 'mtype': mtype, 'employee':employee, 'stores':stores})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)


# Developer: Aidan
# viewing the staff login management page
def viewStaffLogin(request):
     # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            stores = Store.objects.all()
            return render(request, 'staff/loginmanagementview.html', {'name': name, 'utype': utype,'stores': stores})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)

# Developer: Aidan
# will return a json arrray to populate in datatable 
# post variable will get the value sent by ajax
@csrf_exempt # to disable csrf token check
def getStaffFromStore(request):
    # Checking session exists
  
    if request.method == 'POST':
        storeID = request.POST.get('storeID', '')
        employees = Employee.objects.raw("SELECT * FROM `crcapp_employee` WHERE storeID_id = '"+storeID+"' ORDER BY dateJoined DESC")
        return HttpResponse(serialize('json', employees, cls=LazyEncoder))
     
    else:
        return HttpResponse("NULL")

# Developer: Aidan
# will return a json arrray of the login usernames
@csrf_exempt # to disable csrf token check
def getUsernames(request):
    # Checking session exists
     
    if request.method == 'POST':
        employees = Employee.objects.all()
        return HttpResponse(serialize('json', employees, cls=LazyEncoder))
       
    else:
        return HttpResponse("NULL")

# Developer: Aidan
# get start details to the login page
def viewStaffLoginDetails(request, option, msg='',mtype=''):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            employee = Employee.objects.filter(employeeID=option).values()[0]
            store = Store.objects.filter(storeID=employee['storeID_id']).values()[0]
            
            return render(request, 'staff/loginstaffview.html', {'name': name, 'utype': utype,  'msg': msg, 'mtype': mtype, 'employee':employee, 'store':store})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)

# Developer: Jax
# Searching for staff
def searchStaff(request, msg='',mtype=''):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        fields = Employee._meta.get_fields()
        employees = Employee.objects.all()
        return render(request, 'staff/search.html', {'fields': fields}, {'employees': employees})
    else:
       return notLoggedIn(request)


# Developer: Jax
# View Booking page
def viewBooking(request, messages="", mtype="i"):
    #orders = Order.objects.all()
    orders = OrderFor.objects.all()    
    return render(request, 'booking/viewBooking.html', {'orders': orders})

# Developer: Aidan
# emails message will contain what to send and to whom 
# message, id is for the employee id or customer id
# by default it is sent to employees
def email(request, message="Default Message", id = "E00001", isEmployee=True):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        date = timezone.now()
        date_un = date.strftime("%Y%m%d")
        if isEmployee:
            items = Employee.objects.filter(employeeID=id).values()[0]
        else:
            items = Customer.objects.filter(customerID=id).values()[0]
        
        return render(request, 'emaillayout.html', {'name': name, 'utype': utype, 'msg': '', 'mtype': '', 'date':date, 'date_un': date_un, 'item':items, 'msgemail':message})
    else:
       return notLoggedIn(request)


# Developer: Aidan
# creating the login details of the employee
def createLoginStaff(request):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype == "Manager" or utype == "Developer":
            employee = Employee.objects.filter(employeeID=request.POST.get("empID", '')).values()[0]
            store = Store.objects.filter(storeID=employee['storeID_id']).values()[0]
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    return render(request, 'staff/loginstaffview.html', {'name': name, 'utype': utype, 'msg': 'Token verification failed!', 'mtype': 'd', 'employee':employee, 'store':store})
                else:
                    result = staff.StaffController.changeLoginDetails(request, make_password(request.POST.get('password', '')))
                    if result == True:
                        msg = { "subject": "", "message":""}
                        msg['subject'] = "Your welcome guide for using the system."
                        msg['message'] = "Good news. Your new account is ready for you to use. Below you will find your account details and additional information you may need as you get started. You can manage your profile by login to the system."
                        msg['message'] += '</p><p class="ml-2 pl-5"><b>Username: </b> '+request.POST.get("username", '')+'<br><b>Password: </b> '+ request.POST.get("password", '')
                        
                        return email(request, msg, request.POST.get("empID",''))
                    elif result == False:
                        return render(request, 'staff/loginstaffview.html', {'name': name, 'utype': utype, 'msg': 'Opps, something happened, please try again later.', 'mtype': 'd', 'employee':employee, 'store':store})
                    else:
                        return render(request, 'staff/loginstaffview.html', {'name': name, 'utype': utype, 'msg': result, 'mtype': 'd', 'employee':employee, 'store':store})
            elif request.method == "GET":
                return render(request, 'staff/loginstaffview.html', {'name': name, 'utype': utype, 'msg': 'HTTP request error', 'mtype': 'd', 'employee':employee, 'store':store})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)


# Developer: Aidan 
# Create vehicle member page
def createVehicle(request, messages="", mtype=""):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype != "Customer":
            stores = Store.objects.all()
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    return render(request, 'vehicle/create.html', {'msg': 'Token verification failed!', 'mtype': "d", 'stores': stores})
                else:
                    result = vehicle.VehicleController.create(request)
                    if result == True:
                        return render(request, 'vehicle/create.html', {'msg': 'Vehicle inserted.', 'mtype': "i", 'stores': stores})
                    elif result == False:
                        return render(request, 'vehicle/create.html', {'msg': 'Vehicle insertion failed.', 'mtype': "d", 'stores': stores})
                    else:
                        return render(request, 'vehicle/create.html', {'msg': result, 'mtype': "a", 'stores': stores})
            elif request.method == "GET":
                return render(request, 'vehicle/create.html', {'msg': messages, 'name': name, 'mtype': mtype, 'utype': utype, 'stores': stores})
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)

# Developer: Aidan 
# edit changes
def editVehicle(request, messages="", mtype=""):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype != "Customer":
            stores = Store.objects.all()
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    return render(request, 'vehicle/vehicleDetail.html', {'msg': 'Token verification failed!', 'mtype': "d", 'stores': stores})
                else:
                    result = vehicle.VehicleController.modify(request, request.POST.get("vID"))
                    if result == True:
                        return render(request, 'vehicle/vehicleDetail.html', {'msg': 'Vehicle updated.', 'mtype': "i", 'stores': stores})
                    elif result == False:
                        return render(request, 'vehicle/vehicleDetail.html', {'msg': 'Vehicle updating failed.', 'mtype': "d", 'stores': stores})
                    else:
                        return render(request, 'vehicle/vehicleDetail.html', {'msg': result, 'mtype': "a", 'stores': stores})
            
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)

@csrf_exempt 
def deleteVehicle(request, option):
    utype = request.session['utype']
    if utype != "Customer":
        result = vehicle.VehicleController.delete(option)
        if result:
            return HttpResponse("True")
        else:
            return HttpResponse("False")
    else:
        return accessDeniedHome(request)


# Developer: Aidan
# save changes of vehicle
def changeVehicleDetails(request, option, name, utype, msg='',mtype=''):
    if utype != "Customer":
       
        vehicleObj = Vehicle.objects.filter(vehicleID=option).values()[0]
        stores = Store.objects.all()
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        # If the reason is true it means verification failed
        if reason:
            return render(request, 'vehicle/detailview.html', {'name': name, 'utype': utype,'msg': 'Token verification failed!', 'mtype': "d",'vehicle':vehicleObj, 'stores':stores})
        else:
            result = vehicle.VehicleController.modify(request, option)
            if result == True:
                return render(request, 'vehicle/detailview.html', {'name': name, 'utype': utype,'msg': 'Changes saved.', 'mtype': "i",'vehicle':vehicleObj, 'stores':stores})
            elif result == False:
                return render(request, 'vehicle/detailview.html', {'name': name, 'utype': utype,'msg': 'Could not save all changes.', 'mtype': "d",'vehicle':vehicleObj, 'stores':stores})
            else:
                return render(request, 'vehicle/detailview.html', {'name': name, 'utype': utype,'msg': result, 'mtype': "a", 'vehicle':vehicleObj, 'stores':stores})
    else:
        return accessDeniedHome(request)

# Developer: Aidan
# get all vehicles to the view page
def getAllVehicles(request, messages="", mtype=""):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        utype = request.session['utype']
        if utype != "Customer":
            stores = Store.objects.all()
            vehicles = Vehicle.objects.all()
            return render(request, 'vehicle/vehiclemanagementview.html', {'msg': messages, 'name': name, 'mtype': mtype, 'utype': utype, "vehicles":vehicles, "stores": stores})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)

# Developer: Aidan
# get vehicle details to modify page
def getVehicle(request, option, msg='',mtype=''):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        utype = request.session['utype']
        if utype != "Customer":
            if request.method == 'POST':
                return changeVehicleDetails(request, option, name, utype,  msg, mtype)
            elif request.method == 'GET':
                vehicle = Vehicle.objects.filter(vehicleID=option).values()[0]
                stores = Store.objects.all()
                
                return render(request, 'vehicle/detailview.html', {'name': name, 'utype': utype,  'msg': '', 'mtype': mtype, 'vehicle':vehicle, 'stores':stores})
        else:
            return accessDeniedHome(request)
    else:
       return notLoggedIn(request)



# Developer: Aidan
# Change staff profile
def changeStaffProfile(request):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype != "Customer":
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    messages = "Token verification failed."
                    request.session['msg'] = messages
                    request.session['mtp'] = 'd'
                    return redirect('/management/profile')
                else:
                    result = staff.StaffController.modify(request)
                    if result == True:
                        messages = "Profile saved."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'i'
                        return redirect('/management/profile')
                    elif result == False:
                        messages = "Opps, something happened, please try again later."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'd'
                        return redirect('/management/profile')
                    else:
                        messages = result
                        request.session['msg'] = messages
                        request.session['mtp'] = 'a'
                        return redirect('/management/profile')
            
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)

# Developer: Aidan
# Change staff passwords
def changeStaffProfilePassword(request):
    # Checking session exists
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype != "Customer":
            if request.method == 'POST':
                reason = CsrfViewMiddleware().process_view(request, None, (), {})
                # If the reason is true it means verification failed
                if reason:
                    messages = "Token verification failed."
                    request.session['msg'] = messages
                    request.session['mtp'] = 'd'
                    return redirect('/profile')
                else:
                    result = staff.StaffController.changePW(request)
                    if result == True:
                        messages = "Profile saved."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'i'
                        return redirect('/management/profile')
                    elif result == False:
                        messages = "Opps, something happened, please try again later."
                        request.session['msg'] = messages
                        request.session['mtp'] = 'd'
                        return redirect('/management/profile')
                    else:
                        messages = result
                        request.session['msg'] = messages
                        request.session['mtp'] = 'a'
                        return redirect('/management/profile')
            
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)
       
# Developer: Aidan
# Viewing reports
def viewReports(request, msg='', mtype=''):
    if request.session.has_key('uid'):
        name = request.session['name']
        utype = request.session['utype']
        if utype != "Customer":
            stores = Store.objects.all()
            vehicles = Vehicle.objects.all()
            orders = Order.objects.all()           
            query = "SELECT V.count as 'vehicleCount', o.count as 'orderCount', v.state FROM (SELECT COUNT(vehicleID) as 'count', crcapp_store.state FROM crcapp_vehicle, crcapp_store WHERE crcapp_vehicle.storeID_id = crcapp_store.storeID GROUP BY crcapp_store.state) V, (SELECT COUNT(orderID) as 'count', crcapp_store.state FROM crcapp_order, crcapp_store WHERE crcapp_order.pickupStoreID_id = crcapp_store.storeID GROUP BY crcapp_store.state) O WHERE v.state = o.state"
            cursor = connection.cursor()
            cursor.execute(query)
            counts = cursor.fetchall()
            return render(request, 'reports/reports.html', {'name': name, 'utype': utype,  'msg': '', 'mtype': mtype,'orders':orders, 'vehicles':vehicles, 'stores':stores, 'counts': counts})
       
        else:
            return accessDeniedHome(request) 
    else:
       return notLoggedIn(request)