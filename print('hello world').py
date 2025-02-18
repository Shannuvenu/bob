print("thank yoou for visiting band name gererator please enter the following details:")
city = input("enter your city name were you grew up in :")
pet = input("enter your pet name:")

band_name = city[0].upper() + city[1:] + "-" + pet[0].upper() + pet[1:]

print("the band name is:", band_name)
