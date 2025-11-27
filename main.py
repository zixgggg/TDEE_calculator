#!/usr/bin/python3
#male_BMR=(10*weight_kg)+(6.25*height_cm)-(5*age)+5
#female_BMR=(10*weight_kg)+(6.25*height_cm)-(5*age)-161
never_exercise=1.2 # as it name
light_exercise=1.375 # 1-3 days a week
middle_exercise=1.55 # 3-5 days a week
high_exercise=1.725 # 6-7 days a week
very_high_exercise=1.9 # every day
gender=""
user_BMR=""
user_TDEE=""
coefficient_list="""
--------------------------
| never exercise:1.2     |
| as it name             |
|                        |
| light exercise:1.375   |
| 1-3 days a week        |
|                        |
| middle exercise:1.55   |
| 3-5 days a week        |
|                        |
| high exercise:1.725    |
| 6-7 days a week        |
|                        |
| very high exercise:1.9 |
| every day              |
--------------------------
"""
def male_BMR(weight_kg,height_cm,age):
	BMR=10*weight_kg+6.25*height_cm-5*age+5
	return BMR
def female_BMR(weight_kg,height_cm,age):
	BMR=10*weight_kg+6.25*height_cm-5*age-161
	return BMR
def TDEE(BMR,exercise_coefficient):
	answer=BMR*exercise_coefficient
	return answer
def gender_ask():
    gender_ask=input("male or female? enter=(m/f)")
    if gender_ask=="m":
        gender="m"
        user_BMR=male_BMR(user_weight,user_height,user_age)
        return False
    elif gender_ask=="f":
        gender="f"
        user_BMR=female_BMR(user_weight,user_height,user_age)
        return False
    else:
        print("please enter \"m\" or \"f\" ")
        return True
def every_ask():
    user_weight=float(input("enter your weight:"))
    user_height=float(input("enter your height:"))
    user_age=float(input("enter your age:"))
    print(coefficient_list)
    user_exercise_coefficient=float(input("enter your coefficient:"))
    while gender_ask():
        gender_ask()
def BT_output():
    user_TDEE=user_BMR*user_exercise_coefficient
    print(f"your BMR:{user_BMR}")
    print(f"your TDEE:{user_TDEE}")
every_ask()
BT_output()
