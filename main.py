import random
from dp_lap import lap

grades = [random.randint(50,100) for i in range(100)]
sensitivity=1
epsilon=0.5
grade_addNoise = lap.lapAddNoise(grades,sensitivity,epsilon)
print(grades)
print(grade_addNoise)

