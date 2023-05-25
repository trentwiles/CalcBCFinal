import math
from scipy.integrate import quad

def functionOne(x):
    return math.sin(x)

def integral1(upper, lower):
    result, _ = quad(functionOne, upper, lower)
    return result

def midpoint(function, upper, lower, n_times):
    answer = 0
    for x in range(n_times + 1):
        if x == 0:
            # dummy crap
            sdjfjksadf = ""
        else:
            delta_x = ((float(upper) - float(lower)) / n_times)
            each = delta_x / 2
            answer += (delta_x * function(each * x))
    return answer

print(midpoint(functionOne, 2 * math.pi, 0, 8239723))