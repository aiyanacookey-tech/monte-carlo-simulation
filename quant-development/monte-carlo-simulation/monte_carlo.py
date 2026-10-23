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

percentile_5 = np.percentile(final_prices, 5) # calculate the 5th percentile of the final prices
percentile_50 = np.percentile(final_prices, 50) # calculate the 50th percentile of the final prices
percentile_95 = np.percentile(final_prices, 95) # calculate the 95th percentile of the final prices

print(f"5th percentile: £{percentile_5:.2f}")
print(f"50th percentile: £{percentile_50:.2f}")
print(f"95th percentile: £{percentile_95:.2f}")


print("Average final price", np.mean(final_prices))

# Calculate 95% Value at Risk 
var_95 = starting_price - percentile_5
print(f"95% Value at Risk: £{var_95:.2f}")
plt.hist(final_prices, bins=30)

# Mark the 5th percentile on the histogram 
plt.axvline(percentile_5, color='orange', linestyle='--', label='5th Percentile (95% VaR threshold') # add a vertical line at the 5th percentile
plt.legend()

final_prices_array = np.array(final_prices)
worst_prices = final_prices_array[final_prices_array <= percentile_5] # get all final prices that are below the 5th percentile
print("Number of worst ouctomes:", len(worst_prices)) # print the number of worst outcomes
worst_losses = starting_price - worst_prices # calculate the losses for the worst outcomes
cvar_95 = np.mean(worst_losses) # calculate the average loss for the worst outcomes
print(f"95% Conditional Value at Risk: £{cvar_95:.2f}")
assert cvar_95 >= var_95

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

# Create a histogram of simulated ending prices
plt.hist(final_prices, bins=30, alpha=0.7)

plt.xlabel("Final Stock Price (£)") 
plt.ylabel("Number of Simulations") 
plt.title("Monte Carlo Risk Distribution")
plt.axvline(starting_price, color='red', linestyle='--', label='Starting Price (£100)') # add a vertical line at the starting price
plt.axvline(percentile_5, color='orange', linestyle='--', label='5th Percentile (95% VaR threshold)') # add a vertical line at the 5th percentile
plt.axvline(np.mean(final_prices), color='purple', linestyle=':', label='CVAR Tail Average') # add a vertical line at the mean final price
plt.legend() # add a legend to the plot

# Show the graph 
plt.show()



