# covidapp

usage: run covidapp.py

Enter options: 
1. User    
2. Admin   
3. ZoneInfo
4. Exit    
1
user options:       
1. New User Register
2. Self Assessment  
1
Enter user Details in json format: 
{"name":"A","phoneNumber":"9999999999","pinCode":"111111"}
Response: {"userId": "1"}     
do you want to continue (y/n):
y
Enter options: 
1. User
2. Admin
3. ZoneInfo
4. Exit
1
user options:
1. New User Register
2. Self Assessment
2
Enter user assessment Details in json format: 
{"userId":"1","symptoms":["fever","cold","cough"],"travelHistory":true,"contactWithCovidPatient":true}
Response: {"riskPercentage": 95}
do you want to continue (y/n):
y
Enter options: 
1. User
2. Admin
3. ZoneInfo
4. Exit
2
Admin options:
1. New Admin Register
2. Update Covid Result
1
Enter Admin Details in json format: 
{"name":"X","phoneNumber":"9999999999","pinCode":"111111"}
Response: {"adminId": "1"}
do you want to continue (y/n):
y
Enter options: 
1. User
2. Admin
3. ZoneInfo
4. Exit
2
Admin options:
1. New Admin Register
2. Update Covid Result
2
Enter user covid result Details in json format:
{"userId":"1","adminId":"1","result":"positive"}
Response: {"updated": true}
do you want to continue (y/n):
y
Enter options:
1. User
2. Admin
3. ZoneInfo
4. Exit
3
Enter Zone pincode in json format:
{"pinCode":"111111"}
Response: {"numCases": "1", "zoneType": "ORANGE"}
do you want to continue (y/n):
y
Enter options:
1. User
2. Admin
3. ZoneInfo
4. Exit
4
