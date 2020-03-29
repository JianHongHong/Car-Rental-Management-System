# Developer: Sam

from crcapp.models import Vehicle,Store
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.utils import timezone

# Create functions related to staff
class VehicleController:
      # Developer: Sam
    #creates vehicle entry in the database using provided values
    def create(request):

        vehicleObj = Vehicle.objects.raw("SELECT vehicleID FROM `crcapp_vehicle` ORDER BY vehicleID DESC LIMIT 1")[0]
        x = vehicleObj.vehicleID
        x = x[1:]
        x = int(x)+1
        x = str(x).zfill(5)

        vehicleID_ = "V"+x
        makeName_ = request.POST.get("makeName")
        model_ = request.POST.get("model")
        series_ = request.POST.get("series")
        year_ = request.POST.get("year")
        newPrice_ = request.POST.get("newPrice")
        enginesize_ = request.POST.get("enginesize")
        fuelSystem_ = request.POST.get("fuelSystem")
        tankcapacity_ = request.POST.get("tankcapacity")
        power_ = request.POST.get("power")
        seatingCapacity_ = request.POST.get("seatingCapacity")
        standardTransmission_ = request.POST.get("standardTransmission")
        bodyType_ = request.POST.get("bodyType")
        driveType_ = request.POST.get("driveType")
        wheelbase_ = request.POST.get("wheelbase")
        storeID_ = request.POST.get("storeID")
        # Passes the store instance to the model
        store = Store.objects.get(storeID=storeID_)
        try:
            x = Vehicle(
            vehicleID = vehicleID_,
            makeName = makeName_,
            model = model_,
            series = series_,
            year = year_,
            newPrice = newPrice_,
            enginesize = enginesize_,
            fuelSystem = fuelSystem_,
            tankcapacity = tankcapacity_,
            power = power_,
            seatingCapacity = seatingCapacity_,
            standardTransmission = standardTransmission_,
            bodyType = bodyType_,
            driveType = driveType_,
            wheelbase = wheelbase_,
            storeID = store)

            vali = x.full_clean()
            if vali:
                return vali
            else:
                x.save()
                return True

            return False

        except ValidationError as e:
            return e

    #searches for Vehicles that match the given arguments (NW)
#     def search(arg):

#         if(arg == False):
#             for each in Vehicle.objects.all():
#                 print(
#                 each.makeName,
#                 each.model,
#                 each.series,
#                 each.year,
#                 each.newPrice,
#                 each.enginesize,
#                 each.fuelSystem,
#                 each.tankcapacity,
#                 each.power,
#                 each.seatingCapacity,
#                 each.standardTransmission,
#                 each.bodyType,
#                 each.driveType,
#                 each.wheelbase,
#                 each.storeID)

#         if(arg == true):

#             vehicleID_min = request.POST.get("vehicleID_min")
#             vehicleID_max = request.POST.get("vehicleID_max")
#             makeName = request.POST.get("makeName")
#             model = request.POST.get("mode")
#             series = request.POST.get("series")
#             year_min = request.POST.get("year_min")
#             year_max = request.POST.get("year_max")
#             newPrice_min = request.POST.get("newPrice_min")
#             newPrice_max = request.POST.get("newPrice_max")
#             enginesize_min = request.POST.get("enginesize_min")
#             enginesize_max = request.POST.get("enginesize_max")
#             fuelSystem = request.POST.get("fuelSystem")
#             tankcapacity_min = request.POST.get("tankcapacity_min")
#             tankcapacity_max = request.POST.get("tankcapacity_max")
#             power_min = request.POST.get("power_min")
#             power_max = request.POST.get("power_max")
#             seatingCapacity_min = request.POST.get("seatingCapacity_min")
#             seatingCapacity_max = request.POST.get("seatingCapacity_max")
#             standardTransmission = request.POST.get("standardTransmission")
#             bodyType = request.POST.get("bodyType")
#             driveType = request.POST.get("driveType")
#             wheelbase_min = request.POST.get("wheelbase_min")
#             wheelbase_max = request.POST.get("wheelbase_max")
#             storeID = request.POST.get("storeID")

#             condition = " "

#             if (makeName != ''):
#                 condition = condition + "makeName LIKE \'%" + makeName + "%\' AND "

#             if (model != ''):
#                 condition = condition + "model LIKE \'%" + model + "%\' AND "

#             if (series != ''):
#                 condition = condition + "series LIKE \'%" + series + "%\' AND "

#             if (year_min != ''):
#                 condition = condition + "year >= \'" + year_min + "\' AND "

#             if (year_max != ''):
#                 condition = condition + "year <= \'" + year_max + "\' AND "

#             if (newPrice_min != ''):
#                 condition = condition + "newPrice >=  \'" + newPrice_min + "\' AND "

#             if (newPrice_max != ''):
#                 condition = condition + "newPrice <= \'" + newPrice_max + "\' AND "

#             if (enginesize_min != ''):
#                 condition = condition + "enginesize >= \'" + enginesize_min + "\' AND "

#             if (enginesize_max != ''):
#                 condition = condition + "enginesize <= \'" + enginesize_max + "\' AND "

#             if (fuelSystem != ''):
#                 condition = condition + "fuelSystem = \'" + fuelSystem + "\' AND "

#             if (tankcapacity_min != ''):
#                 condition = condition + "tankcapacity >= \'" + tankcapacity_min + "\' AND "

#             if (tankcapacity_max != ''):
#                 condition = condition + "tankcapacity <= \'" + tankcapacity_max + "\' AND "

#             if (power_min != ''):
#                 condition = condition + "power >= \'" + power_min + "\' AND "

#             if (power_max != ''):
#                 condition = condition + "power <= \'" + power_max + "\' AND "

#             if (seatingCapacity_min != ''):
#                 condition = condition + "seatingCapacity >= \'" + seatingCapacity_min + "\' AND "

#             if (seatingCapacity_max != ''):
#                 condition = condition + "seatingCapacity <= \'" + seatingCapacity_max + "\' AND "

#             if (standardTransmission != ''):
#                 condition = condition + "standardTransmission LIKE \'%" + standardTransmission + "%\' AND "

#             if (bodyType != ''):
#                 condition = condition + "bodyType CONTAINS \'" + bodyType + "\' AND "

#             if (driveType != ''):
#                 condition = condition + "driveType CONTAINS \'" + driveType + "\' AND "

#             if (wheelbase_min != ''):
#                 condition = condition + "wheelbase >= \'" + wheelbase_min + "\' AND "

#             if (wheelbase_max != ''):
#                 condition = condition + "wheelbase <= \'" + wheelbase_max + "\' AND "

#             if (storeID != ''):
#                 condition = condition + "storeID = \'" + storeID + "\' AND "

#             query = 'SELECT * FROM carrentaldb.crcapp_customer WHERE' + condition[:-5] +';'

#             for each in Vehicle.objects.raw(query):
#                 return(
#                 each.makeName,
#                 each.model,
#                 each.series,
#                 each.year,
#                 each.newPrice,
#                 each.enginesize,
#                 each.fuelSystem,
#                 each.tankcapacity,
#                 each.power,
#                 each.seatingCapacity,
#                 each.standardTransmission,
#                 each.bodyType,
#                 each.driveType,
#                 each.wheelbase,
#                 each.storeID)

    
    # edit vehicle entry in the database using provided values
    def modify(request, vID):
        vehicle = Vehicle.objects.get(vehicleID=vID)
        makeName_ = request.POST.get("makeName")
        model_ = request.POST.get("model")
        series_ = request.POST.get("series")
        year_ = request.POST.get("year")
        newPrice_ = request.POST.get("newPrice")
        enginesize_ = request.POST.get("enginesize")
        fuelSystem_ = request.POST.get("fuelSystem")
        tankcapacity_ = request.POST.get("tankcapacity")
        power_ = request.POST.get("power")
        seatingCapacity_ = request.POST.get("seatingCapacity")
        standardTransmission_ = request.POST.get("standardTransmission")
        bodyType_ = request.POST.get("bodyType")
        driveType_ = request.POST.get("driveType")
        wheelbase_ = request.POST.get("wheelbase")
        storeID_ = request.POST.get("storeID")
        # Passes the store instance to the model
        store = Store.objects.get(storeID=storeID_)
        try:
            vehicle.makeName = makeName_
            vehicle.model = model_
            vehicle.series = series_
            vehicle.year = year_
            vehicle.newPrice = newPrice_
            vehicle.enginesize = enginesize_
            vehicle.fuelSystem = fuelSystem_
            vehicle.tankcapacity = tankcapacity_
            vehicle.power = power_
            vehicle.seatingCapacity = seatingCapacity_
            vehicle.standardTransmission = standardTransmission_
            vehicle.bodyType = bodyType_
            vehicle.driveType = driveType_
            vehicle.wheelbase = wheelbase_
            vehicle.store = store

            vali = vehicle.full_clean()
            if vali:
                return vali
            else:
                vehicle.save()
                return True

            return False

        except ValidationError as e:
            return e
       


    def delete(ID):
        x = Vehicle.objects.get(vehicleID = ID)
        res = x.delete()
        if res:
            return True
        else:
            return False

