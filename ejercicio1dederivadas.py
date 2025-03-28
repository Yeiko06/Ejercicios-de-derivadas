import numpy as np
import matplotlib.pyplot as plt

# Función a derivar
def f(x):
    return np.sin(x)

# Derivada analítica
def df_analytical(x):
    return np.cos(x)

# Métodos de diferencias finitas
def forward_diff(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h=0.1):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h=0.1):
    return (f(x + h) - f(x - h)) / (2*h)

# Rango de valores
a, b, h = 0.0, np.pi, 0.1
x_vals = np.arange(a, b, h)
df_exact = df_analytical(x_vals)

# Aproximaciones numéricas
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Errores
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Graficar derivadas
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), label='Función $f(x)$')
plt.plot(x_vals, df_exact, 'k-', label='Derivada Analítica')
plt.plot(x_vals, df_forward, 'r--', label='Diferencias Adelante')
plt.plot(x_vals, df_backward, 'g-.', label='Diferencias Atrás')
plt.plot(x_vals, df_central, 'b:', label='Diferencias Centradas')
plt.xlabel('x')
plt.ylabel("Derivada")
plt.legend()
plt.grid()
plt.title("Diferenciación Numérica de $f(x) = \sin(x)$")
plt.show()

# Graficar errores
plt.figure(figsize=(10, 6))
plt.plot(x_vals, error_forward, 'r--', label='Error Adelante')
plt.plot(x_vals, error_backward, 'g-.', label='Error Atrás')
plt.plot(x_vals, error_central, 'b:', label='Error Centrado')
plt.xlabel('x')
plt.ylabel("Error absoluto")
plt.legend()
plt.grid()
plt.title("Errores en Diferenciación Numérica")
plt.show()