# heston_model
Heston model in option pricing 

Here is a comprehensive English README file for your GitHub repository:

Heston Model Option Pricing

This repository contains Python code for implementing the Heston Model for option pricing. The Heston Model is a stochastic volatility model that extends the Black-Scholes framework by incorporating random variance. It is widely used in financial engineering to price options and capture volatility smiles.

Features
	•	Computes the price of European call options using the Heston model.
	•	Accepts user inputs for all key Heston model parameters.
	•	Calculates prices based on numerical integration and characteristic functions.
	•	Provides a well-documented and extensible Python implementation.

Prerequisites

To run this code, ensure you have the following installed:
	•	Python 3.6 or above
	•	Required libraries (install via pip):

pip install numpy scipy

	2.	Enter the required Heston model parameters when prompted:
	•	S0: Current stock price
	•	K: Strike price
	•	T: Time to maturity (in years)
	•	r: Risk-free rate (e.g., 0.05 for 5%)
	•	q: Dividend yield (e.g., 0.02 for 2%)
	•	kappa: Speed of variance mean reversion
	•	theta: Long-term mean variance
	•	sigma_v: Volatility of variance
	•	rho: Correlation between stock price and variance
	•	v0: Initial variance
	3.	View the calculated European call option price in the terminal.

Example

Input

S0 (Current stock price): 100
K (Strike price): 100
T (Time to maturity, in years): 1
r (Risk-free rate): 0.05
q (Dividend yield): 0.02
kappa (Speed of variance mean reversion): 2
theta (Long-term mean variance): 0.04
sigma_v (Volatility of variance): 0.3
rho (Correlation between stock price and variance, -1 to 1): -0.7
v0 (Initial variance): 0.04

Output

The computed price of the European call option is: 10.56

Code Structure
	•	heston_model.py: The main script implementing the Heston model option pricing logic.

How It Works
	1.	Characteristic Function:
	•	The Heston model’s characteristic function is used for pricing options via Fourier transforms.
	2.	Numerical Integration:
	•	The option price is calculated by numerically integrating the characteristic function.
	3.	Key Parameters:
	•	kappa, theta, sigma_v, rho, and v0 capture the stochastic volatility dynamics.

References
	•	Heston, Steven L. (1993). “A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options.” The Review of Financial Studies.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributions

Contributions are welcome! If you find issues or have suggestions, feel free to open an issue or submit a pull request.

Author

Williams Wang
Feel free to connect for questions or collaboration opportunities!

Enjoy exploring the Heston Model!
