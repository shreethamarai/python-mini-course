### math lib -> square root, factorial, trigonometry, constants (pi, e), rounding

import math

### Finacial rounding - Currency calculations, invoices, tax computations
amount = 12.56789
print("Rounded to 2 decimels:", round(amount, 2))

### Geometry & design calculations - Engineering CAD, game design
radius = 5
area = math.pi * radius**2
print("Circle area:", area)

### Physics / Simulation - Robotics,graphics rendering, scientific simulations
angle_deg = 45
angle_rad = math.radians(angle_deg)
print("sin(45°):", math.sin(angle_deg))

### Growth & decay models - Population growth, compound interest, radioactive decay
initial_value = 100
rate = 0.05
time = 10
future_value = initial_value * math.exp(rate * time)
print("Future value:", future_value)


