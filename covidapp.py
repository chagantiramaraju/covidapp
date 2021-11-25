import json

userDB = dict()
userId = 0
adminDB = dict()
adminId = 0

def GetUserId():
    global userId
    userId += 1
    return str(userId)

def GetAdminId():
    global adminId
    adminId += 1
    return str(adminId)

def CalculateRiskPercentage(symptoms,travelhistory, contactwithcovidPatient):
    if len(symptoms) == 0 and travelhistory == False and contactwithcovidPatient == False:
        return 0
    if len(symptoms) == 1 and (travelhistory or contactwithcovidPatient):
        return 50
    if len(symptoms) == 2 and (travelhistory or contactwithcovidPatient):
        return 75
    if len(symptoms) > 2 and (travelhistory or contactwithcovidPatient):
        return 95

def RegisterUser(userdata):
    userid = GetUserId()
    userdata['symptoms'] = []
    userdata['travelHistory'] = False
    userdata['contactWithCovidPatient'] = False
    userdata['result'] = ''
    userdata['adminId'] = ''
    userDB[userid] = userdata

    response = {}
    response['userId'] = userid
    responsestr = json.dumps(response)
    
    return responsestr

def UserSelfAssessment(userdata):
    response = {}
    userid = userdata['userId']
    if userid in userDB:
        del userdata['userId']
        userdata['name'] = userDB[userid]['name']
        userdata['phoneNumber'] = userDB[userid]['phoneNumber']
        userdata['pinCode'] = userDB[userid]['pinCode']
        userDB[userid] = userdata

        response['riskPercentage'] = CalculateRiskPercentage(userdata['symptoms'],userdata['travelHistory'],userdata['contactWithCovidPatient'])        
    else:
        response['error'] = 'userId is not present'
    
    responsestr = json.dumps(response)
    return responsestr

def RegisterAdmin(admindata):
    adminid = GetAdminId()
    adminDB[adminid] = admindata
    response = {}
    response['adminId'] = adminid
    responsestr = json.dumps(response)
    return responsestr

def UpdateCovidResult(userdata):
    response = {}
    userid = userdata['userId']
    adminid = userdata['adminId']
    if userid in userDB and adminid in adminDB:
        del userdata['userId']
        userdata['name'] = userDB[userid]['name']
        userdata['phoneNumber'] = userDB[userid]['phoneNumber']
        userdata['pinCode'] = userDB[userid]['pinCode']
        userdata['symptoms'] = userDB[userid]['symptoms']
        userdata['travelHistory'] = userDB[userid]['travelHistory']
        userdata['contactWithCovidPatient'] = userDB[userid]['contactWithCovidPatient']
        userDB[userid] = userdata #userdata will already have adminId and result
        response["updated"] = True
    else:
        response["updated"] = False

    responsestr = json.dumps(response)
    return responsestr

def GetZoneInfo(zonedata):
    noOfcases = 0
    for k,v in userDB.items():
        if v['pinCode'] == zonedata['pinCode'] and v['result'] == 'positive':
            noOfcases += 1
    
    zoneType = 'GREEN'
    if noOfcases == 0:
        zoneType = 'GREEN'
    elif noOfcases < 5:
        zoneType = 'ORANGE'
    else:
        zoneType = 'RED'

    response = {}
    response['numCases'] = str(noOfcases)
    response['zoneType'] = zoneType
    responsestr = json.dumps(response)
    return responsestr

def main():
    str = 'y'
    while(str == 'y'):
        print('Enter options: ')
        print('1. User')
        print('2. Admin')
        print('3. ZoneInfo')
        print('4. Exit')

        user = input()

        if user == 'User' or user == '1':
            print('user options:')
            print('1. New User Register')
            print('2. Self Assessment')
            userinput = input()
            if userinput == '1' or userinput == 'New User Register':
                print('Enter user Details in json format: ')
                userin = input()
                udata = json.loads(userin)
                print("Response: " + RegisterUser(udata))

            if userinput == '2' or userinput == 'Self Assessment':
                print('Enter user assessment Details in json format: ')
                userassin = input()
                udata = json.loads(userassin)
                print("Response: " + UserSelfAssessment(udata))

        if user == 'Admin' or user == '2':
            print('Admin options:')
            print('1. New Admin Register')
            print('2. Update Covid Result')
            admininput = input()
            if admininput == '1' or admininput == 'New Admin Register':
                print('Enter Admin Details in json format: ')
                adminin = input()
                admindata = json.loads(adminin)
                print("Response: " + RegisterAdmin(admindata))

            if admininput == '2' or admininput == 'Update Covid Result':
                print('Enter user covid result Details in json format: ')
                resultin = input()
                resultdata = json.loads(resultin)
                print("Response: " + UpdateCovidResult(resultdata))

        
        if user == 'ZoneInfo' or user == '3':
            print('Enter Zone pincode in json format: ')
            zonepin = input()
            zonedata = json.loads(zonepin)
            print("Response: " + GetZoneInfo(zonedata))

        if user == 'Exit' or user == '4':
            break
        
        print('do you want to continue (y/n):')
        str = input()

if __name__=='__main__':
    main()