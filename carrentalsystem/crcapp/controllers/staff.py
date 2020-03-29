from crcapp.models import Employee,Store
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.utils import timezone

# Create functions related to staff
class StaffController:

    # Developer: Sam
    # Creating a new staff account. If a username exist in the employee
    # database, do not create the account. else, create the account for
    # the employee
    def createStaff(request):
        staffObj = Employee.objects.raw("SELECT employeeID FROM `crcapp_employee` ORDER BY employeeID DESC LIMIT 1")[0]
        empID = staffObj.employeeID
        empID = empID[1:]
        empID = int(empID)+1
        emploID = str(empID).zfill(5)

        try:
            employeeID_ = "E"+emploID
            firstName_ = request.POST.get("firstName")
            lastName_ = request.POST.get("lastName")
            streetAddress_ = request.POST.get("streetAddress")
            cityAddress_ = request.POST.get("city")
            postCodeAddress_ = request.POST.get("postalCode")
            stateAddress_ = request.POST.get("state")
            DOB_ = request.POST.get("dob")
            TFN_ = request.POST.get("TFN")
            phoneNumber_ = request.POST.get("phoneNumber")
            email_ = request.POST.get("email")
            userName_ = "NULL"
            password_ = "NULL"
            userType_ = request.POST.get("userType")
            dateJoined_ = timezone.now()
            lastLogin_ = timezone.now()
            storeID_ = request.POST.get("storeID")
            store = Store.objects.get(storeID=storeID_)

            # Sam change this according to your create function for now Iam adding this to test
            staff = Employee(employeeID = employeeID_,
                        firstName = firstName_,
                        lastName = lastName_,
                        streetAddress = streetAddress_,
                        cityAddress = cityAddress_,
                        postCodeAddress = postCodeAddress_,
                        stateAddress = stateAddress_,
                        DOB = DOB_,
                        TFN = TFN_,
                        phoneNumber = phoneNumber_,
                        email = email_,
                        userName = userName_,
                        password = password_,
                        userType = userType_,
                        dateJoined = dateJoined_,
                        lastLogin = lastLogin_,
                        storeID = store)

            vali = staff.full_clean()
            if vali:
                return vali
            else:
                staff.save()
                return True

            return False

        except ValidationError as e:
            return e

    # Developer: Sam
    # modifying the staff values
    def modify(request):

        employeeID_ = request.POST.get("employeeID")
        firstName_ = request.POST.get("firstName")
        lastName_ = request.POST.get("lastName")
        streetAddress_ = request.POST.get("streetAddress")
        cityAddress_ = request.POST.get("city")
        postCodeAddress_ = request.POST.get("postalCode")
        stateAddress_ = request.POST.get("state")
        DOB_ = request.POST.get("dob")
        TFN_ = request.POST.get("TFN")
        phoneNumber_ = request.POST.get("phoneNumber")
        email_ = request.POST.get("email")
        userType_ = request.POST.get("userType")
        storeID_ = request.POST.get("storeID")
        store = Store.objects.get(storeID=storeID_)

        staff = Employee.objects.get(employeeID = employeeID_)

        try:
            if(firstName_ != ""):
                staff.firstName = firstName_

            if(lastName_ != ""):
                staff.lastName = lastName_

            if(streetAddress_ != ""):
                staff.streetAddress = streetAddress_

            if(cityAddress_ != ""):
                staff.cityAddress = cityAddress_

            if(postCodeAddress_ != ""):
                staff.postCodeAddress = postCodeAddress_

            if(stateAddress_ != ""):
                staff.stateAddress = stateAddress_

            if(DOB_ != ""):
                staff.DOB = DOB_

            if(TFN_ != ""):
                staff.TFN = TFN_

            if(phoneNumber_ != ""):
                staff.phoneNumber = phoneNumber_

            if(email_ != ""):
                staff.email = email_


            if(userType_ != ""):
                staff.userType = userType_


            if(storeID_ != ""):
                staff.storeID = store

            vali = staff.full_clean()
            if vali:
                return vali
            else:
                staff.save()
                return True

            return False

        except ValidationError as e:
            return e

      # Developer: Aidan
    def changeLoginDetails(request, pw):
        try:
            employeeID_ = request.POST.get("empID")
            userName_ = request.POST.get("username")
            password_ = pw


            # updating certain values
            staff = Employee.objects.get(employeeID=employeeID_)
            staff.userName=userName_
            staff.password = password_
            vali = staff.full_clean()
            if vali:
                return vali
            else:
                staff.save()
                return True

            return False

        except ValidationError as e:
            return e

      # Developer: Sam
    def search(arg):
        if (arg == False):
            for each in Customer.objects.all():
                return(
                    each.employeeID,
                    each.firstName,
                    each.lastName,
                    each.streetAddress,
                    each.cityAddress,
                    each.postCodeAddress,
                    each.stateAddress,
                    each.DOB,
                    each.TFN,
                    each.phoneNumber,
                    each.email,
                    each.userName,
                    each.password,
                    each.userType,
                    each.dateJoined,
                    each.lastLogin,
                    each.storeID)

        if (arg == True):
            employeeID_min = request.POST.get("employeeID_min")
            employeeID_max = request.POST.get("employeeID_max")
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            streetAddress = request.POST.get("streetAddress")
            cityAddress = request.POST.get("cityAddress")
            postCodeAddress_min = request.POST.get("postCodeAddress_min")
            postCodeAddress_max = request.POST.get("postCodeAddress_max")
            stateAddress = request.POST.get("stateAddress")
            DOB_min = request.POST.get("DOB_min")
            DOB_max = request.POST.get("DOB_max")
            TFN = request.POST.get("TFN")
            phoneNumber = request.POST.get("phoneNumber")
            email = request.POST.get("email")
            userName = request.POST.get("userName")
            password = request.POST.get("password")
            userType = request.POST.get("userType")
            dateJoined_min = request.POST.get("dateJoined_min")
            dateJoined_max = request.POST.get("dateJoined_max")
            lastLogin_min = request.POST.get("lastLogin_min")
            lastLogin_max = request.POST.get("lastLogin_max")
            storeID = request.POST.get("storeID")


            condition = " "

            if (employeeID_min != ""):
                condition = condition + "employeeID >= \'" + employeeID_min + "\' AND "

            if (employeeID_max != ""):
                condition = condition + "employeeID <= \'" + employeeID_max + "\' AND "

            if (firstName != ""):
                condition = condition + "firstName LIKE \'%" + firstName + "%\' AND "

            if (lastName != ""):
                condition = condition + "lastName LIKE \'%" + lastName + "%\' AND "

            if (streetAddress != ""):
                condition = condition + "streetAddress LIKE \'%" + streetAddress + "%\' AND "

            if (cityAddress != ""):
                condition = condition + "cityAddress LIKE \'%" + cityAddress + "%\' AND "

            if (postCodeAddress_min != ""):
                condition = condition + "postCodeAddress >= \'" + postCodeAddress_min + "\' AND "

            if (postCodeAddress_max != ""):
                condition = condition + "postCodeAddress <= \'" + postCodeAddress_max + "\' AND "

            if (stateAddress != ""):
                condition = condition + "stateAddress LIKE \'%" + stateAddress + "%\' AND "

            if (DOB_min != ""):
                condition = condition + "DOB >= \'" + DOB_min + "\' AND "

            if (DOB_max != ""):
                condition = condition + "DOB <= \'" + DOB_max + "\' AND "

            if (TFN != ""):
                condition = condition + "TFN = \'" + TFN + "\' AND "

            if (phoneNumber != ""):
                condition = condition + "phoneNumber = \'" + phoneNumber + "\' AND "

            if (email != ""):
                condition = condition + "email LIKE \'%" + email + "%\' AND "

            if (userName != ""):
                condition = condition + "userName LIKE \'%" + userName + "%\' AND "

            if (userType != ""):
                condition = condition + "userType = \'" + userType + "\' AND "

            if (dateJoined_min != ""):
                condition = condition + "dateJoined >= \'" + dateJoined_min + "\' AND "

            if (dateJoined_max != ""):
                condition = condition + "dateJoined <= \'" + dateJoined_max + "\' AND "

            if (lastLogin_min != ""):
                condition = condition + "lastLogin >= \'" + lastLogin_min + "\' AND "

            if (lastLogin_max != ""):
                condition = condition + "lastLogin_max <= \'" + lastLogin_max + "\' AND "

            if (storeID != ""):
                condition = condition + "storeID = \'" + storeID + "\' AND "

            query = 'SELECT * FROM carrentaldb.crcapp_customer WHERE' + condition[:-5] +';'

            for each in Employee.objects.raw(query):
                return(
                each.employeeID,
                each.firstName,
                each.lastName,
                each.streetAddress,
                each.cityAddress,
                each.postCodeAddress,
                each.stateAddress,
                each.DOB,
                each.TFN,
                each.phoneNumber,
                each.email,
                each.userName,
                each.password,
                each.userType,
                each.dateJoined,
                each.lastLogin,
                each.storeID)

    def changePW(request):
        employeeID_ = request.POST.get("employeeID")
        password_ = make_password(request.POST.get('password', ''))

        existingEmployee = Employee.objects.get(employeeID=employeeID_)

        try:
            existingEmployee.password = password_
            
            vali = existingEmployee.full_clean()
            if vali:
                return vali
            else:
                existingEmployee.save()
                return True 
            return False
        except ValidationError as e:
            return e.message_dict