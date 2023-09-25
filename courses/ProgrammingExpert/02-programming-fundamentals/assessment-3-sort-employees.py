
def sort_employees(employees, sort_by):
    keys = {"name": 0, "age": 1, "salary": 2}  # mapping sort_by keys to their respective indices
    return sorted(employees, key=lambda x: x[keys[sort_by]])

employees = [
  ["John", 33, 65000],
  ["Sarah", 24, 75000],
  ["Josie", 29, 100000],5
  ["Jason", 26, 55000],
  ["Connor", 25, 110000]
]

print(sort_employees(employees, "age"))
print(sort_employees(employees, "salary"))
print(sort_employees(employees, "name"))
