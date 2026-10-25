import numpy as np

def simulate_stock_price(starting_price, days, mean_daily_return, daily_volatility):
    daily_returns = np.random.normal(mean_daily_return, daily_volatility, days)
    prices = [starting_price]

    for daily_return in daily_returns:
        new_price = prices[-1] * (1 + daily_return)
        prices.append(new_price)

    return prices

if __name__ == "__main__":

    starting_price = 100
    days = 252
    mean_daily_return = 0.0003
    daily_volatility = 0.02

    number_of_simulations = 1000
    final_prices = []

    for simulation in range(number_of_simulations):
        prices = simulate_stock_price(starting_price, days, mean_daily_return, daily_volatility)
        final_prices.append(prices[-1])

    assert len(final_prices) == number_of_simulations, "The length of final_prices should be equal to number_of_simulations"    

    print("Simulations completed:", len(final_prices))
    print("Average final price:", np.mean(final_prices))

