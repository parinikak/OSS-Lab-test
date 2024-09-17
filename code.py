import numpy as np
import matplotlib.pyplot as plt
#import SciPy as sp

patient_list = np.array([
    [1, "John", 101, "age: 41 years", "diagnosed with diabetes", "eat less sugar", "Room 101", 1000],
    [2, "Jill", 102, "age:31 years", "diagnosed with bone problem", "advised to consume vitamin d", "Room 102", 2000],
    [3, "Jack", 101, "age: 28 years", "fracture", "advised to eat calcium,vitamin d and rest", "Room 103", 3000],
    [4, "Arjun", 103, "age: 24 years", "risk of heart attack", "regular laughter exercise; no stress", "Room 104", 4000],
    [5, "Neha", 102, "age: 20 years", "light sprain", "a week bed rest", "Room 105", 5000]
], dtype=object)

doctor_list = np.array([
    [101, "Dr. Rohan", "Cardiologist"],
    [102, "Dr. Rohit", "Neurologist"],
    [103, "Dr. Khanna", "Orthopedic"]
], dtype=object)

def find_patients_by_doctor(doctor_id):
    return patient_list[patient_list[:, 2] == doctor_id]

def update_treatment(patient_id, new_treatment):
    patient_list[patient_list[:, 0] == patient_id, 4] = new_treatment

#def find_doctors_with_max_min_patients():
    #patient_counts = np.unique(patient_list[:, 2], return_counts=True)[1]
    #max_count = np.max(patient_counts)
    #min_count = np.min(patient_counts)
    #max_doctors = doctor_list[np.isin(doctor_list[:, 0],(patient_list[:, 2][patient_list[:, 2]])== np.unique(patient_list[:, 2])[np.argmax(patient_counts)]
    #min_doctors = doctor_list[np.isin(doctor_list[:, 0],(patient_list[:, 2][patient_list[:, 2]]) == np.unique(patient_list[:, 2])[np.argmin(patient_counts)]
    #return max_doctors[:, 0], min_doctors[:, 0]

def find_patients_with_max_min_bill():
    max_bill = np.max(patient_list[:, 7].astype(int))
    min_bill = np.min(patient_list[:, 7].astype(int))
    max_bill_patients = patient_list[patient_list[:, 7].astype(int) == max_bill]
    min_bill_patients = patient_list[patient_list[:, 7].astype(int) == min_bill]
    return max_bill_patients, min_bill_patients

print(find_patients_by_doctor(101))

update_treatment(1, "New Treatment")
print(patient_list)

#max_doctors, min_doctors = find_doctors_with_max_min_patients()
#print(max_doctors, min_doctors)

max_bill_patients, min_bill_patients = find_patients_with_max_min_bill()
print(max_bill_patients, min_bill_patients)

