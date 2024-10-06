#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Niklaus Guenther     
Program Title: imperial to metric converter
Description: Program 3
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    tons = float(input("Enter the number of imperial tons: "))
    stones = float(input("Enter the number of stones: "))
    pounds = float(input("Enter the number of pounds: "))
    ounces = float(input("Enter the number of ounces: "))

    #Calculates total ounces
    total_ounces = (35840 * tons) + (224 * stones) + (16 * pounds) + ounces

    #Converts total ounces to kilograms
    total_kilos = total_ounces / 35.274

    #Calculates metric tons and remaining kilograms
    metric_tons = int(total_kilos // 1000)


    print("Metric tons: {metric_tons}")

        #Your code ends on the line above

#Do not change any of the code below!
main()