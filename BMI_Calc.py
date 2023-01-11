# -*- coding: utf-8 -*-
pound = u'\u00A3'

print("Welcome to the BMI calculator! version 1.01\n")

# User inputs
age_years = int(input("Age (Years): "))
height = float(input("Height (M): "))
weight = float(input("Weight (Kg): "))
body_fat = float(input("Body fat (%): "))
gender = input("Gender (M/F): ").lower()
exercise = int(input("Days a week exercise: "))

# BMI stats
bmi = weight / (height * height)
fat_weight = (weight * 2.20462) * (body_fat * 0.01) * 0.453592
lean_weight = weight - body_fat

# BMR stats
bmr = 0
bmr_active = 0

if gender == 'm':
    bmr = (10 * weight) + (6.25 * (height * 100)) - (5 * age_years) + 65
    bmr_active = bmr + (exercise * 130)
elif gender == 'f':
    bmr = (10 * weight) + (6.25 * (height * 100)) - (5 * age_years) - 161
    bmr_active = bmr + (exercise * 130)
else:
    print('invalid Gender!')

# Heart Rate stats
max_heart_rate = 220 - age_years
mhr_80 = (max_heart_rate / 100) * 80
mhr_70 = (max_heart_rate / 100) * 70
mhr_60 = (max_heart_rate / 100) * 60

# Formatting results
bmi = round(bmi, 1)
fat_weight = round(fat_weight, 2)
lean_weight = round(lean_weight, 2)
bmr = round(bmr)
bmr_active = round(bmr_active)

max_heart_rate = round(max_heart_rate)
mhr_80 = round(mhr_80)
mhr_70 = round(mhr_70)
mhr_60 = round(mhr_60)

print(f"\nBMI: {bmi}\nWeight in fat (Kg): {fat_weight}\nLean weight (Kg): {lean_weight}\nBasal Metabolic Rate: {bmr}\nBasal Metabolic Rate (Active): {bmr_active}\n")
print(f"Max Heart Rate: {max_heart_rate}\nMax Heart Rate @ 80%: {mhr_80}\nMax Heart Rate @ 70%: {mhr_70}\nMax Heart Rate @ 60%: {mhr_60}\n")

macro_option = input("Would you like to view your daily macro breakdown? (Y/N): ").lower()

if macro_option == 'yes' or macro_option == 'y':
    print('Here is your daily macro breakdown...')
else:
    exit()

# Macro maths
lose_cals_fast = round(((bmr + bmr_active) / 2) - 250)
protein_lose_fg = round(lean_weight * 2.20462)
protein_lose_fc = round(protein_lose_fg * 4)
fat_lose_fg = round(0.35 * (lean_weight * 2.20462))
fat_lose_fc = round(fat_lose_fg * 9)
carbs_lose_fc = round((((bmr + bmr_active) / 2) - (protein_lose_fc + fat_lose_fc)) - 250)
carbs_lose_fg = round(carbs_lose_fc / 4)

lose_cals = round((bmr + bmr_active) / 2)
protein_loseg = round(lean_weight * 2.20462)
protein_losec = round(protein_loseg * 4)
fat_loseg = round(0.35 * (lean_weight * 2.20462))
fat_losec = round(fat_loseg * 9)
carbs_losec = round(((bmr + bmr_active) / 2) - (protein_losec + fat_losec))
carbs_loseg = round(carbs_losec / 4)

main_cals = round(((bmr + bmr_active) / 2) + 250)
protein_maing = round((lean_weight * 2.20462) * 1.5)
protein_mainc = round(protein_maing * 4)
fat_maing = round(0.5 * (lean_weight * 2.20462))
fat_mainc = round(fat_maing * 9)
carbs_mainc = round((((bmr + bmr_active) / 2) - (protein_mainc + fat_mainc)) + 250)
carbs_maing = round(carbs_mainc / 4)

print(f'\nLose cals fast (day): {lose_cals_fast}\nProtein: {protein_lose_fg} (g), {protein_lose_fc} (cals)\nFat: {fat_lose_fg} (g), {fat_lose_fc} (cals)\nCarbs: {carbs_lose_fg} (g), {carbs_lose_fc} (cals)\n')
print(f'\nLose cals (day): {lose_cals}\nProtein: {protein_loseg} (g), {protein_losec} (cals)\nFat: {fat_loseg} (g), {fat_losec} (cals)\nCarbs: {carbs_loseg} (g), {carbs_losec} (cals)\n')
print(f'\nMaintain cals (day): {main_cals}\nProtein: {protein_maing} (g), {protein_mainc} (cals)\nFat: {fat_maing} (g), {fat_mainc} (cals)\nCarbs: {carbs_maing} (g), {carbs_mainc} (cals)\n')