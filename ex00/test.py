from give_bmi import give_bmi, apply_limit

print("Standard example")
height = [2.71, 1.15, 1.65]
weight = [165.3, 38.4, 50]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("Not same dimension")
# not same dimension
height = [2.71, 1.15, 1.65, 1.30]
weight = [165.3, 38.4, 50]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("Empty list")
# list vide
height = []
weight = []
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("Divide by zero")
# division par zero
height = [1.60, 0]
weight = [50, 40]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("not int or float type")
# division par zero
height = ["oui", 1.78]
weight = [50, "zozo"]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))