names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are ", num_medical_records, " medical records.")

first_medical_record = medical_records[0]
print("Here is the first medical record: ", first_medical_record)
print()
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

print()
cheapest_three = medical_records[:3]
print("Here are the cheapest three insurance costs in the medical records: ", cheapest_three)

print()
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in the medical record: ", priciest_three)

print()
print("There are ", names.count("Paul"), " individuals with the name Paul in the medical records.")
