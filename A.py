from pulp import *
# ask user to input whether the problem is max or min
mod = input("Enter the model(min or max):")
# checking whether the problem is LP Minimization/Maximization
if mod.lower() == 'max':
    model = LpProblem("Profit_Maximization", LpMaximize)
elif mod.lower() == 'min':
    model = LpProblem("Profit_Minimization", LpMinimize)
# Getting the number of variables as user input
v = int(input("Enter the number of variables:"))
var_list1 = []
# create problem variables
for i in range(0, v):
    var = f'x{i + 1}'
    var = LpVariable(f"{var}", lowBound=0, cat=input(f"Enter the data type of{var}(Continuous/Integer):").title())
    var_list1.append(var)
# Getting coefficients of the objective and constraints
a = list(map(float, input("Enter the coefficients of the objective:").split()))
c = list(map(float, input("Enter the coefficients of the constrains:").split()))
# getting the constants of the constraints
b = list(map(float, input("Enter the constants:").split()))
# Objective function
list_objective = []
for i in range(0, v):
    list_objective.append(a[i] * var_list1[i])
model += lpSum(list_objective)
# Constraints
i = 0
m = 0
while i != len(c):
    list_constrains = []
    for j in range(0, v):
        list_constrains.append(c[i] * var_list1[j])
        i = i + 1
model += lpSum(list_constrains) <= b[m]
m = m + 1
# Display the problem
print(model)
# Solve the problem
model.solve()
# printing the final solutions
# Variable values
for i in var_list1:
    print(f"{i}*:{value(i)}")
# Objective function value
print(value(model.objective))