import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the ODE
def exponential_growth(t, y, k):
    return k * y

# Constant k (can be positive for growth or negative for decay)
k = 0.1

# Initial condition
y0 = [1]

# Time span (from t=0 to t=10)
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 100)

# Solve the ODE
sol = solve_ivp(exponential_growth, t_span, y0, args=(k,), t_eval=t_eval)

# Plotting
plt.plot(sol.t, sol.y[0], label='y(t)')
plt.xlabel('Time t')
plt.ylabel('y(t)')
plt.title('Exponential Growth/Decay')
plt.legend()
plt.grid(True)
plt.show()
