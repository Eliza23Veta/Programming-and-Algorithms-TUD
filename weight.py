weight = float(input("input weight: "))            #input weight
units = input("(K)g or (L)bs: ")                   # input units
if units.upper() == "K":
    print("weight in lbs is: ", weight*2.205)      #if in kg -> convert to l
if units.upper() == "L":
    print ("weight in Kg is: ", weight/2.205)       # if in lbs -> convert to kg
else: units = input("Enter K/k or L/l units only. Run the program again.")
