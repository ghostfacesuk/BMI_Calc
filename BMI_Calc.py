# -*- coding: utf-8 -*-
pound = u'\u00A3'

print("Welcome to the BMI calculator!\n")

# User inputs
AgeYears = input("Age (Years): ")
Height = input("Height (M): ")
Weight = input("Weight (Kg): ")
BodyFat = input("Body fat (%): ")
Gender = input("Gender (M/F): ")
Exercise = input("Days a week exercise: ")

# BMI stats
BMI = (float(Weight)/(float(Height)*float(Height)))
FatWeight = ((float(Weight)*2.20462)*(float(BodyFat)*0.01))*0.453592
LeanWeight = (float(Weight) - float(BodyFat))

#BMR stats
BMR = float(1.0)
BMRActive = float(1.0)

if Gender == str('M') or Gender == str('m'):
    BMR = (10*float(Weight))+(6.25*(float(Height)*100))-5*int(AgeYears)+65
    BMRActive = (float(BMR) + (float(Exercise)*130))
elif Gender == str('F') or Gender == str('f'):
    BMR = (10*float(Weight))+(6.25*(float(Height)*100))-5*int(AgeYears)-161
    BMRActive = (float(BMR) + (float(Exercise)*130))
else:
    print('invalid Gender!')

# Heart Rate stats
MaxHeartRate = (220 - int(AgeYears))
MHR80 = ((MaxHeartRate/100)*80)
MHR70 = ((MaxHeartRate/100)*70)
MHR60 = ((MaxHeartRate/100)*60)

# Formatting results
BMI = round(BMI, 1)
FatWeight = round(FatWeight, 2)
LeanWeight = round(LeanWeight, 2)
BMR = round(BMR)
BMRActive = round(BMRActive)

MaxHeartRate = round(MaxHeartRate)
MHR80 = round(MHR80)
MHR70 = round(MHR70)
MHR60 = round(MHR60)

print(f"\nBMI: {BMI}\nWeight in fat (Kg): {FatWeight}\nLean weight (Kg): {LeanWeight}\nBasal Metabolic Rate: {BMR}\nBasal Metabolic Rate (Active): {BMRActive}\n")
print(f"Max Heart Rate: {MaxHeartRate}\nMax Heart Rate @ 80%: {MHR80}\nMax Heart Rate @ 70%: {MHR70}\nMax Heart Rate @ 60%: {MHR60}\n")

