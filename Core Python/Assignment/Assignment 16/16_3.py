# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.



class Shirt():
    discount = 10
    def __init__(self, sid=1, sname="", stype="", sprice=0, ssize=""):

        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.sprice=sprice
        self.ssize=ssize

        if(self.ssize in 'S,s,small,Small'):
            self.discount = sprice
        elif(self.ssize in 'M,m,medium,MEDIUM'):
            Shirt.discount *= 1
            self.discount = (sprice/100*Shirt.discount)+sprice
        elif(self.ssize in 'L,l,large,LARGE'):
            Shirt.discount *= 2
            self.discount = (sprice/100*Shirt.discount)+sprice
        elif(self.ssize in 'XL,xl,xlarge,XLARGE'):
            Shirt.discount *= 3
            self.discount = (sprice/100*Shirt.discount)+sprice


        


    def showshirt(self):
        print("#######################################")
        print("Shirt Id :",self.sid)
        print("Shirt Brand Name :",self.sname)
        print("Shirt Type :",self.stype)
        print("Shirt Size :",self.ssize)        
        print("Shirt Price :",self.discount)

    def __del__(self):
        print("distroctor is called")



shirt1=Shirt(1025,"U.S.Polo","Formal",1000,"M")
shirt1.showshirt()

del shirt1

shirt2=Shirt()
shirt2.showshirt()