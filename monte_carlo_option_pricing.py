import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Option parameters
S0 = 100       # Current stock price
K = 100        # Strike price
T = 1          # Time to expiry (years)
r = 0.05       # Risk-free interest rate
sigma = 0.20   # Volatility
n_simulations = 10000

# Generate random values from a standard normal distribution
Z = np.random.standard_normal(n_simulations)

# Calculate simulated stock prices after one year
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z
)

print(ST[:10])

# Calculate the payoff of the call option
payoffs = np.maximum(ST - K, 0)

print(payoffs[:10])

# Calculate the Monte Carlo estimate of the call option price
option_price = np.exp(-r * T) * np.mean(payoffs)

print("Monte Carlo Call Option Price:", option_price)

# Calculate Black-Scholes values
d1 = (
    np.log(S0 / K)
    + (r + 0.5 * sigma**2) * T
) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

# Calculate Black-Scholes call option price
black_scholes_price = (
    S0 * norm.cdf(d1)
    - K * np.exp(-r * T) * norm.cdf(d2)
)

print("Black-Scholes Call Option Price:", black_scholes_price)

# Plot distribution of simulated future stock prices
plt.figure(figsize=(10, 5))

plt.hist(ST, bins=50)

plt.title("Distribution of Simulated Future Stock Prices")
plt.xlabel("Stock Price at Expiry")
plt.ylabel("Frequency")

plt.show()

# Compare the two option pricing methods
difference = abs(option_price - black_scholes_price)

print("Monte Carlo Price:", option_price)
print("Black-Scholes Price:", black_scholes_price)
print("Absolute Difference:", difference)
