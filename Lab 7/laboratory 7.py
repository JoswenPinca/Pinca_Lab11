name = input("What is your name? ")
section = input("What is your section? ")
prelim = input("What is your prelim grade? ")
if prelim.isdigit():
    prelimf = float(prelim)

    if prelimf > 100 or prelimf < 40:
        print("Invalid input. Please input a grade from 40 to 100.")
    else:
        midterm = float(input("What is your midterm grade? "))
        if midterm > 100 or midterm < 40:
                print("Invalid input. Please input a grade from 40 to 100.")
        else:
            finalterm = float(input("What is your final grade? "))
            if finalterm > 100 or finalterm < 40:
                print("Invalid input. Please input a grade from 40 to 100.")
            else:
                finalgrade = prelim * 0.3333 + midterm * 0.3333 + finalterm * 0.3333
                finalgraderound = round(finalgrade)
        
                if finalgraderound <= 100 and finalgraderound >= 99:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 1.00, Excellent!")
                elif finalgraderound <= 98 and finalgraderound >= 96:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 1.25, Outstanding!")
                elif finalgraderound <= 95 and finalgraderound >= 93:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 1.50, Superior!")
                elif finalgraderound <= 92 and finalgraderound >= 90:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 1.75, Very Good!")
                elif finalgraderound <= 89 and finalgraderound >= 87:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 2.00, Good!")
                elif finalgraderound <= 86 and finalgraderound >= 84:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 2.25, Satisfactory!")
                elif finalgraderound <= 83 and finalgraderound >= 81:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 2.50, Fairly Satisfactory!")
                elif finalgraderound <= 80 and finalgraderound >= 78:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 2.75, Fair!")
                elif finalgraderound <= 77 and finalgraderound >= 75:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 3.00, Passed!")
                elif finalgraderound < 74:
                    print(f"Hello {name} from {section}!")
                    print(f"Your Final Grade is {finalgraderound}, and your GPA is 5.00, Failed!")