import numpy as np
from scipy.integrate import quad

# Heston model characteristic function
def heston_characteristic_function(u, S0, K, T, r, q, kappa, theta, sigma_v, rho, v0):
    """
    Computes the characteristic function of the Heston model.
    :param u: Complex argument for the Fourier transform.
    :param S0: Current stock price.
    :param K: Strike price.
    :param T: Time to maturity (in years).
    :param r: Risk-free rate (annualized).
    :param q: Dividend yield (annualized).
    :param kappa: Mean reversion speed of variance.
    :param theta: Long-term variance.
    :param sigma_v: Volatility of variance.
    :param rho: Correlation between stock price and variance.
    :param v0: Initial variance.
    :return: Value of the characteristic function.
    """
    i = 1j  # Imaginary unit
    x = np.log(S0 / K)  # Log of the stock-to-strike ratio
    d = np.sqrt((rho * sigma_v * u * i - kappa) ** 2 + (sigma_v ** 2) * (u * i + u ** 2))
    g = (kappa - rho * sigma_v * u * i - d) / (kappa - rho * sigma_v * u * i + d)
    C = (r - q) * u * i * T + (kappa * theta / sigma_v**2) * ((kappa - rho * sigma_v * u * i - d) * T - 2 * np.log((1 - g * np.exp(-d * T)) / (1 - g)))
    D = ((kappa - rho * sigma_v * u * i - d) / sigma_v**2) * (1 - np.exp(-d * T)) / (1 - g * np.exp(-d * T))
    return np.exp(C + D * v0 + u * i * x)

# Heston option price function
def heston_option_price(S0, K, T, r, q, kappa, theta, sigma_v, rho, v0):
    """
    Computes the price of a European call option using the Heston model.
    :param S0: Current stock price.
    :param K: Strike price.
    :param T: Time to maturity (in years).
    :param r: Risk-free rate (annualized).
    :param q: Dividend yield (annualized).
    :param kappa: Mean reversion speed of variance.
    :param theta: Long-term variance.
    :param sigma_v: Volatility of variance.
    :param rho: Correlation between stock price and variance.
    :param v0: Initial variance.
    :return: Option price.
    """
    P1 = 0.5 + (1 / np.pi) * quad(
        lambda u: np.real(heston_characteristic_function(u - 1j, S0, K, T, r, q, kappa, theta, sigma_v, rho, v0) / (u * 1j)),
        0, np.inf
    )[0]
    P2 = 0.5 + (1 / np.pi) * quad(
        lambda u: np.real(heston_characteristic_function(u, S0, K, T, r, q, kappa, theta, sigma_v, rho, v0) / (u * 1j)),
        0, np.inf
    )[0]
    return np.exp(-r * T) * (S0 * P1 - K * P2)

# Input parameters with descriptions
def get_user_inputs():
    """
    Prompts the user to input Heston model parameters with descriptions.
    :return: Dictionary of user-input parameters.
    """
    print("Please provide the following parameters for the Heston model:")
    S0 = float(input("S0 (Current stock price): "))
    K = float(input("K (Strike price): "))
    T = float(input("T (Time to maturity, in years): "))
    r = float(input("r (Risk-free interest rate, annualized, e.g., 0.05 for 5%): "))
    q = float(input("q (Dividend yield, annualized, e.g., 0.02 for 2%): "))
    kappa = float(input("kappa (Speed of variance mean reversion): "))
    theta = float(input("theta (Long-term mean variance): "))
    sigma_v = float(input("sigma_v (Volatility of variance): "))
    rho = float(input("rho (Correlation between stock price and variance, between -1 and 1): "))
    v0 = float(input("v0 (Initial variance): "))
    return {
        "S0": S0, "K": K, "T": T, "r": r, "q": q,
        "kappa": kappa, "theta": theta, "sigma_v": sigma_v, "rho": rho, "v0": v0
    }

# Main function to compute and display the option price
def main():
    print("\nWelcome to the Heston Model Option Pricing Tool!")
    params = get_user_inputs()
    price = heston_option_price(**params)
    print(f"\nThe computed price of the European call option is: {price:.2f}")

if __name__ == "__main__":
    main()
