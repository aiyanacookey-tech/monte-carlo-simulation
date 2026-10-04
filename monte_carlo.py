import numpy as np


starting_pirce = 100
days = 252

print("Starting stock price:", starting_pirce)
print("Trading days:", days)

# "Give me 252 random observations from a normal distribution centred around 0 with a standard deviation of 2%."

daily_returns = np.random.normal(0, 0.02, days)
print(daily_returns)

