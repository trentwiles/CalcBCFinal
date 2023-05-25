import math
from scipy import integrate

def functionOne(x):
    return math.sin(x)

def integral(function, lower, upper):
    # I have to put it backwards for some reason
    result, error = integrate.quad(function, upper, lower)
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
print(integral(functionOne, 123, 0))