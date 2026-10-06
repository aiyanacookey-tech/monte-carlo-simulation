import numpy as np # numbers/calculations
import matplotlib.pyplot as plt # used for creating plots, graphs / visualisations


starting_price = 100
days = 252

# print("Starting stock price:", starting_pirce)
# print("Trading days:", days)

# "Give me 252 random observations from a normal distribution centred around 0 with a standard deviation of 2%."

daily_returns = np.random.normal(0, 0.02, days)
# print(daily_returns)

mean_daily_returns = 0.0003 # stock's average daily return is around 0.03%
daily_volatility = 0.005 

random_returns = np.random.normal(mean_daily_returns, daily_volatility)
new_price = starting_price * (1 + random_returns)
# print(random_returns)
# print(new_price)
# print(starting_price)

daily_returns = np.random.normal(mean_daily_returns, daily_volatility, days)
# print(daily_returns[:10])  # Print the first 10 daily returns

prices = [starting_price] # these square brakcets create a Python list

# Here we are going to loop through the daily returns and calculate the new price for each day, appending it to the prices list.

for daily_return in daily_returns: # go through each daily return in the daily_returns array
    new_price = prices[-1] * (1 + daily_return) # calculate the new price based on the last price in the prices list and the current daily return
    prices.append(new_price) # append the new price to the prices list

# print("Final price:", prices[-1]) # print the final price after 252 trading days

plt.plot(prices) # plot the prices list
plt.xlabel("Trading Day") # label the x-axis
plt.ylabel("Stock Price") # label the y-axis
plt.title("Simulation of Stock Price") # title of the plot
plt.show() # display the plot



