class EntryPass:
    time = 12.00
    rate = 0
    vPass = "A"
    vType = "A"
    def start(self):
        time = self.time
        rate = self.rate
        vPass = self.vPass
        vType = self.vType
        
        while((time>10) or (time<=0)):
            time = float(input("\nHow many hours do you wish to park your vehicle for?\nYour Response: "))
            if((time>10) or (time<0)):
                print("\nTime should be less than 10 hours and more that 0 hours.\n")

        while((vPass!="Y") and (vPass!="N")):
            print("\nDo you already have a pass?\nPress 'Y' or 'y' for Yes\nPress 'N' or 'n' for No")
            vPassTemp = input("Your Response: ")
            vPass = vPassTemp.upper()
            if(vPass=="Y"):
                time = (time-5.0)
            elif((vPass!="Y") and (vPass!="N")):
                print("Please re-enter the correct option\n")

        while((vType!="T") and (vType!="F")):
            print("\nPlease enter the type of your vehicle.\nPress 'T' or 't' for Two wheeler\nPress 'F' or 'f' for Four wheeler")
            vTypeTemp = input("Your Response: ")
            vType = vTypeTemp.upper()
            if (vType=="T"):
                rate = 50
            elif (vType=="F"):
                rate = 80
            elif ((vType!="T") and (vType!="F")):
                print("Please re-enter the correct option\n")
        
        if ((time <= 5.00) and (time > 0.00)):
            bill = rate
        elif (time > 5.00):
            bill = rate*2
        elif (time <=0):
            bill = 0
        print(time)
        return bill

car1 = EntryPass()
print(car1.start())