# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  message = "The estimated insurance cost for " + name + " is $"
  
  return message, estimated_cost


# Estimate Maria's insurance cost
out, maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")

print(out + str(maria_insurance_cost))
# Estimate Omar's insurance cost 
out, omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")

print(out + str(omar_insurance_cost))

def difference_of_cost(cost1, cost2):
  difference = cost1 - cost2
  print("The difference in insurance cost is " + str(difference) + " dollars.")

difference_of_cost(maria_insurance_cost, omar_insurance_cost)
