import qrcode
qr=qrcode.QRCode(
    version=10,
    box_size=10,
    border= 5

    )
name=input("Enter the name : ")
age = int(input("Enter the age :"))
email= input("Enter the email :")
mobile = int(input("Enter the mobile number:"))
Doornumber  = input("Enter the door number:")
Area = input("Enter the area :")
Dist = input("Enter the district:")
State= input("Enter the state :")
Country = input("Enter the country name:")
data = {"Name":name,"Age":age,"Email":email,"Door number":Doornumber,"Area":Area,"Dist":Dist,"State":State,"Country":Country}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("Mydetails.png")
img.show()
