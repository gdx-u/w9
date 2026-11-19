def grade(mark):
  if not 0 <= mark <= 100:
    return "Invalid mark"
  if mark >= 70: return "First"
  if mark >= 60: return "2:1"
  if mark >= 50: return "2:2"
  if mark >= 40: return "Third"
  return "Fail"
students = {"Asha": [68, 72], "Ben": [55, 61]}
for name, marks in students.items():
  average = sum(marks) / len(marks)
  print(name, average, grade(average))
