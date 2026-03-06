class MultipleFunction():

    def Subfields():
        print("Sub-fields in AI are:")

        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]

        for field in subfields:
            print(field)

    def OddEven():
        number = int(input("Enter the number to check Odd/Even : "))

        if(number % 2 == 0):
            print("Given Number is Even")
            msg = "Even Number"
        else:
            print("Given Number is Odd")
            msg = "Odd Number"

        return msg

    def Eligible():
        gender = input("Your Gender : ")
        age = int(input("Your Age : "))

        if (gender == "Male" and age >= 21) or (gender == "Female" and age >= 18):
            print("Eligible")
            msg =  "Eligible for Marriage"
        else:
            print("Not Eligible")   
            msg =  "Not Eligible for Marriage"
        return  msg 

    def percentage():

        s1 = int(input("Subject 1 = "))
        s2 = int(input("Subject 2 = "))
        s3 = int(input("Subject 3 = "))
        s4 = int(input("Subject 4 = "))
        s5 = int(input("Subject 5 = "))

        total = s1 + s2 + s3 + s4 + s5
        percentage = total / 5

        print("Total =", total)
        print("Percentage =", percentage)  

    def triangle():
        # AREA
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        formula1="(Height*Breadth)/2"
        Area=(Height*Breadth)/2
        print(f"Area formula: {formula1}") 
        print(f"Area of Triangle: {Area}")
        
        # Perimeter
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        formula2="Height1+Height2+Breadth"
        Perimeter=Height1+Height2+Breadth
        print(f"Perimeter formula: {formula2}")
        print(f"Perimeter of Triangle: {Perimeter}")    
   
