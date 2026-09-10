# Monte Carlo Option Pricing

## Overview

This project implements a Monte Carlo simulation to price a European call option and compares the result with the analytical Black-Scholes model.

The simulation models the terminal stock price using Geometric Brownian Motion and evaluates how the accuracy of the Monte Carlo estimate changes as the number of simulations increases.

## Methodology

The project:

- Simulates terminal stock prices using Geometric Brownian Motion
- Calculates European call option payoffs
- Discounts expected payoffs to obtain the Monte Carlo option price
- Calculates the analytical Black-Scholes price
- Compares Monte Carlo and Black-Scholes estimates
- Measures absolute and percentage pricing error
- Analyses convergence across different simulation sizes
- Calculates Monte Carlo standard error
- Constructs 95% confidence intervals
- Visualises the distribution of simulated stock prices and pricing error

## Parameters

| Parameter | Value |
|---|---:|
| Initial Stock Price | $100 |
| Strike Price | $100 |
| Time to Expiry | 1 year |
| Risk-Free Rate | 5% |
| Volatility | 20% |
| Initial Simulations | 10,000 |

## Results

The 10,000-simulation Monte Carlo estimate was:

| Method | Option Price |
|---|---:|
| Monte Carlo | $10.4502 |
| Black-Scholes | $10.4506 |

The absolute difference was **$0.0004**, corresponding to a percentage difference of **0.004%**.

### Convergence Analysis

| Simulations | Monte Carlo Price | Percentage Error | Standard Error |
|---:|---:|---:|---:|
| 100 | $8.1600 | 21.92% | 1.1783 |
| 500 | $10.3776 | 0.70% | 0.6775 |
| 1,000 | $10.5166 | 0.63% | 0.4730 |
| 5,000 | $10.4850 | 0.33% | 0.2076 |
| 10,000 | $10.4502 | 0.004% | 0.1478 |
| 50,000 | $10.4462 | 0.042% | 0.0657 |

The standard error decreases substantially as the number of simulations increases, reflecting greater estimation precision with larger sample sizes.

For each simulation size, the Black-Scholes price fell within the calculated 95% confidence interval.

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib

## Disclaimer

This project is for educational purposes and does not constitute investment advice.
