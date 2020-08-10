class goblin:
    x=0
    y=0
    z=0
    big=0
    x=int(input("enter the 1st number: "))
    y=int(input("enter the 2nd number: "))
    z=int(input("enter the 3rd number: "))
    def compare(self):
        if self.x>self.y:
            if self.x>self.z:
                self.big=self.x
                
        if self.y>self.x:
            if self.y>self.z:
                self.big=self.y
        
        if self.z>self.x:
            if self.z>self.y:
                self.big=self.z
        print("\nThe largest number is : "+str(self.big))
g1=goblin()
g1.compare()
