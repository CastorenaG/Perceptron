import numpy as np

# Definir la función de activación del perceptrón (función escalón)
def step_function(x):
    return 1 if x >= 0 else 0

# Función para entrenar el perceptrón utilizando el algoritmo de aprendizaje Hebbiano
def train_perceptron(X, Y, learning_rate=0.1, epochs=100):
    num_samples, num_features = X.shape
    weights = np.zeros(num_features + 1)  # +1 para el sesgo (bias)
    errors = []

    for _ in range(epochs):
        total_error = 0
        for i in range(num_samples):
            x = np.insert(X[i], 0, 1)  # Agregar sesgo al vector de entrada
            y_pred = step_function(np.dot(weights, x))
            error = Y[i] - y_pred
            total_error += error
            weights += learning_rate * error * x
        errors.append(total_error)
    
    return weights, errors

# Datos de entrada y resultados deseados para la compuerta OR
X_or = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
Y_or = np.array([0, 1, 1, 1])

# Datos de entrada y resultados deseados para la compuerta AND
X_and = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
Y_and = np.array([0, 0, 0, 1])

# Entrenar el perceptrón para la compuerta OR
weights_or, errors_or = train_perceptron(X_or, Y_or)

# Entrenar el perceptrón para la compuerta AND
weights_and, errors_and = train_perceptron(X_and, Y_and)

# Probar el perceptrón
test_inputs = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

for input in test_inputs:
    x = np.insert(input, 0, 1)
    y_or = step_function(np.dot(weights_or, x))
    y_and = step_function(np.dot(weights_and, x))
    print(f"Input: {input}, OR Output: {y_or}, AND Output: {y_and}")
