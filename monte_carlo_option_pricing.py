import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set random seed for reproducibility
np.random.seed(42)

# Option parameters
S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.20
n_simulations = 10000


# -----------------------------
# Monte Carlo Simulation
# -----------------------------

# Generate random values from a standard normal distribution
Z = np.random.standard_normal(n_simulations)

# Calculate simulated stock prices at expiry using Geometric Brownian Motion
ST = S0 * np.exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z
)

# Calculate call option payoffs
payoffs = np.maximum(ST - K, 0)

# Calculate Monte Carlo option price
option_price = np.exp(-r * T) * np.mean(payoffs)

print("Monte Carlo Call Option Price:", option_price)


# -----------------------------
# Black-Scholes Model
# -----------------------------

d1 = (
    np.log(S0 / K)
    + (r + 0.5 * sigma**2) * T
) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

black_scholes_price = (
    S0 * norm.cdf(d1)
    - K * np.exp(-r * T) * norm.cdf(d2)
)

print("Black-Scholes Call Option Price:", black_scholes_price)


# -----------------------------
# Comparison
# -----------------------------

difference = abs(option_price - black_scholes_price)

percentage_difference = (
    difference / black_scholes_price
) * 100

print("Absolute Difference:", difference)
print("Percentage Difference:", percentage_difference)


# -----------------------------
# Distribution of Simulated Prices
# -----------------------------

plt.figure(figsize=(10, 5))

plt.hist(ST, bins=50)

plt.title("Distribution of Simulated Future Stock Prices")
plt.xlabel("Stock Price at Expiry")
plt.ylabel("Frequency")

plt.show()


# -----------------------------
# Monte Carlo Convergence
# -----------------------------

simulation_sizes = [100, 500, 1000, 5000, 10000, 50000]

prices = []
errors = []
percentage_errors = []
standard_errors = []

# Generate one reproducible set of random values
# so that smaller samples are nested within the larger sample
np.random.seed(42)
Z_all = np.random.standard_normal(max(simulation_sizes))

for n in simulation_sizes:

    Z = Z_all[:n]

    ST = S0 * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z
    )

    payoffs = np.maximum(ST - K, 0)

    discounted_payoffs = np.exp(-r * T) * payoffs

    price = np.mean(discounted_payoffs)

    standard_error = (
        np.std(discounted_payoffs, ddof=1)
        / np.sqrt(n)
    )

    error = abs(price - black_scholes_price)

    percentage_error = (
        error / black_scholes_price
    ) * 100

    prices.append(price)
    errors.append(error)
    percentage_errors.append(percentage_error)
    standard_errors.append(standard_error)


# Display convergence results

for i in range(len(simulation_sizes)):

    print(
        "Simulations:", simulation_sizes[i],
        "| Price:", prices[i],
        "| Absolute Error:", errors[i],
        "| Percentage Error:", percentage_errors[i],
        "| Standard Error:", standard_errors[i]
    )


# -----------------------------
# Convergence Plot
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    simulation_sizes,
    percentage_errors,
    marker="o"
)

plt.title("Monte Carlo Pricing Error and Number of Simulations")
plt.xlabel("Number of Simulations")
plt.ylabel("Absolute Percentage Error (%)")
plt.xscale("log")

plt.show()


# -----------------------------
# 95% Confidence Intervals
# -----------------------------

confidence_intervals = []

for i in range(len(simulation_sizes)):

    lower = (
        prices[i]
        - 1.96 * standard_errors[i]
    )

    upper = (
        prices[i]
        + 1.96 * standard_errors[i]
    )

    confidence_intervals.append((lower, upper))

    print(
        "Simulations:", simulation_sizes[i],
        "| 95% CI:", lower, "to", upper
    )


# -----------------------------
# Confidence Interval Check
# -----------------------------

for i in range(len(simulation_sizes)):

    lower, upper = confidence_intervals[i]

    within_interval = (
        lower <= black_scholes_price <= upper
    )

    print(
        "Simulations:", simulation_sizes[i],
        "| Black-Scholes within 95% CI:",
        within_interval
    )
