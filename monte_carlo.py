import numpy as np # numbers/calculations
import matplotlib.pyplot as plt # for plotting, graphs and visualisations


# Our assumptions
starting_price = 100
days = 252
mean_daily_return = 0.0003
daily_volatility = 0.02
number_of_simulations = 1000
final_prices = []



# Generate 252 hypothetical daily returns
daily_returns = np.random.normal(
    mean_daily_return,
    daily_volatility,
    days
)


# Begin our price history at £100
prices = [starting_price]

# Here we are going to loop through the daily returns and calculate the new price for each day, appending it to the prices list.
for simulation in range(number_of_simulations): # loop through the number of simulations
    daily_returns = np.random.normal(
        mean_daily_return,
        daily_volatility,
        days
    )
    prices = [starting_price] # reset prices for each simulation

    for daily_return in daily_returns: # go through each daily return in the daily_returns array
        new_price = prices[-1] * (1 + daily_return) # calculate the new price based on the last price in the prices list and the current daily return
        prices.append(new_price) # append the new price to the prices list

    final_prices.append(prices[-1]) # append the final price after 252 trading days to the final_prices list

print("Number of simulations:", len(final_prices))
print("Average final price", np.mean(final_prices))

## Out of our 100 simulated years, what percentage ended below our starting price of £100?

losses = 0

for final_price in final_prices:
    if final_price < starting_price:
        losses += 1

probablity_of_loss = losses / number_of_simulations
print("Probability of loss:", f"{probablity_of_loss:.2%}") # print the probability of loss as a percentage with 2 decimal places

total_return = (prices[-1] - starting_price) / starting_price # calculate the total return over the 252 trading days
print("Total return:", f"{total_return:.2%}") # print the total return as a percentage with 2 decimal places
# print("Final price:", prices[-1]) # print the final price after 252 trading days

plt.plot(prices) # plot the prices list
plt.xlabel("Trading Day") # label the x-axis
plt.ylabel("Stock Price") # label the y-axis
plt.title("Simulation of Stock Price") # title of the plot
plt.show() # display the plot



