import math
from scipy.integrate import quad

def functionOne(x):
    return math.sin(x)

def integral1(upper, lower):
    result, _ = quad(functionOne, upper, lower)
    return result

def midpoint(function, upper, lower, n_times):
    answer = 0
    delta_x = ((float(upper) - float(lower)) / n_times)
    for x in range(n_times):
        answer += delta_x * function((delta_x) * (0.5 + x))
    return answer

def right(function, upper, lower, n_times):
    answer = 0
    delta_x = ((float(upper) - float(lower)) / n_times)
    for x in range(n_times + 1):
        if x != 0:
            #print(delta_x * x)
            answer += delta_x * function(delta_x * x)
    return answer

def left(function, upper, lower, n_times):
    answer = 0
    delta_x = ((float(upper) - float(lower)) / n_times)
    for x in range(n_times + 1):
        if x != (n_times + 1):
            #print(delta_x * x)
            answer += delta_x * function(delta_x * x)
    return answer

print(midpoint(functionOne, 123, 0, 2848348))
print(right(functionOne, 123, 0, 2848348))
print(left(functionOne, 123, 0, 2848348))


#print(trap(functionOne, 2 * math.pi, 0, 4))