import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = "./prueba.csv"
data = pd.read_csv(data)
print(data)

## Setting variables
x = data['L']
y = data['T^2']
yerr = data['delta_t']
xerr = 0.01

# Calculate weights
weights = 1 / yerr**2

# Calculate sums needed for slope and intercept
sum_w = weights.sum()
sum_wx = (weights * x).sum()
sum_wy = (weights * y).sum()
sum_wxx = (weights * x**2).sum()
sum_wxy = (weights * x * y).sum()

# Calculate weighted slope (a) and intercept (b)
slope = (sum_w * sum_wxy - sum_wx * sum_wy) / (sum_w * sum_wxx - sum_wx**2)
intercept = (sum_wxx * sum_wy - sum_wx * sum_wxy) / (sum_w * sum_wxx - sum_wx**2)

# Calculate standard errors (uncertainties)
slope_std_err = np.sqrt(sum_w / (sum_w * sum_wxx - sum_wx**2))
intercept_std_err = np.sqrt(sum_wxx / (sum_w * sum_wxx - sum_wx**2))

# Predict the Y values
y_pred = slope * x + intercept

# Calculate normalized residuals
residuals = (y - y_pred)/yerr


print(f"Slope (a): {slope} ± {slope_std_err}")
print(f"Intercept (b): {intercept} ± {intercept_std_err}")
print(f"Residuals: {residuals}")

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [2, 1]})  # 2 rows, 1 column, width = 10 inches, height = 10 inches

# Plot the regression line
ax1.errorbar(x, y, yerr, xerr,  fmt='o', label='Data points with errors')
ax1.plot(x, y_pred, color='red', linewidth=2, label=f'Weighted Linear fit: v = ({slope:.2f}± {slope_std_err:.2f})t + ({intercept:.3f}± {intercept_std_err:.3f})')

ax1.set_xlabel('t(s)')
ax1.set_ylabel('v(m/s)')
ax1.legend(loc='upper left')
ax1.set_title('Linear Regression using weighted Least Squares')

# Plot normalized residuals
ax2.scatter(x, residuals, color='green', alpha=0.5, label='Residuals')
ax2.axhline(0, color='black', linewidth=1, linestyle='--')
ax2.set_xlabel('t(s)')
ax2.set_ylabel('Normalized residuals')
ax2.legend(loc='upper right')
ax2.set_title('Normalized residuals from Linear Regression')

plt.tight_layout()

# Save the figure as a PDF file
plt.savefig('Weighted_linear_regression_with_normalized_residuals_least_squares.pdf', format='pdf')
plt.show()
