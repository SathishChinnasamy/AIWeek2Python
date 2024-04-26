class Assignment4():
    
    def subfeilds():
        subf=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-feilds in AI are :")
        for i in subf:
            print(i)

    def OddEven():
        num=int(input("Enter the number"))
        if(num%2==0):
            print(num," is Even Number")
        else:
            print(num," is Odd Number")
               
    def eligible(gender,age):
        if(gender=='Male'):
            if(age<=20):
                print("NOT ELIGIBLE")
            else:
                print("Eligible")
        else:
            if(age<=18):
                print("NOT ELIGIBLE")
            else:
                print("Eligible")

    def eligible(gender,age):
        if(gender=='Male'):
            if(age<=20):
                print("NOT ELIGIBLE")
            else:
                print("Eligible")
        else:
            if(age<=18):
                print("NOT ELIGIBLE")
            else:
                print("Eligible")
                  
    def percentage(subject1,subject2,subject3,subject4,subject5):
        total=subject1+subject2+subject3+subject4+subject5
        print("Total: ",total)
        percent=(total/500)*100
        return percent
    
    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area Formula: (Height * Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle: ",area)
        height1=int(input("Height1 :"))
        height2=int(input("Height2 :"))
        breadth=int(input("Breadth: "))
        print("Perimeter Formula: Height1 + Height2 +Breadth")
        peri=height1+height2+breadth
        print("Perimeter of triangle: ",peri)