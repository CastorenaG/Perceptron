# Perceptrón para Compuertas Lógicas
Este es un código Python que implementa un perceptrón para simular las compuertas lógicas OR y AND. 
El perceptrón es una unidad básica de una red neuronal artificial y se utiliza para realizar operaciones lógicas simples.

Descripción
El código consta de las siguientes partes:

Importación de bibliotecas:

numpy se utiliza para operaciones matriciales.
Definición de la función de activación del perceptrón:

step_function(x) es la función de activación del perceptrón, que implementa una función escalón. Devuelve 1 si la entrada x es mayor o igual a cero, de lo contrario, devuelve 0.
Función para entrenar el perceptrón:

train_perceptron(X, Y, learning_rate=0.1, epochs=100) entrena el perceptrón con los datos de entrada X y los resultados deseados Y. Utiliza el algoritmo de aprendizaje del perceptrón y devuelve los pesos finales del perceptrón y una lista de errores a lo largo del entrenamiento.
Datos de entrada y resultados deseados:

X_or y Y_or contienen los datos de entrada y resultados deseados para la compuerta lógica OR.
X_and y Y_and contienen los datos de entrada y resultados deseados para la compuerta lógica AND.
Entrenamiento del perceptrón:

Se entrena el perceptrón para la compuerta OR y la compuerta AND utilizando la función train_perceptron. Se obtienen los pesos finales y se registran los errores durante el entrenamiento.
Prueba del perceptrón:

Se prueban las salidas del perceptrón con diferentes entradas en test_inputs. Se calculan las salidas para las compuertas OR y AND, y se muestran en la salida.
Uso
Puede utilizar este código para comprender cómo funciona un perceptrón y cómo se entrena para realizar operaciones lógicas. Puede ajustar los datos de entrada y resultados deseados para probar el perceptrón con otras compuertas lógicas o configuraciones personalizadas.

Recuerde que el perceptrón es un modelo muy básico y solo puede aprender funciones lineales. Para problemas más complejos, se requieren modelos de red neuronal más avanzados.

Nota: Este código es un ejemplo educativo y no debe considerarse como una implementación completa de una red neuronal. Para aplicaciones reales, se utilizan bibliotecas y marcos de trabajo de aprendizaje profundo más avanzados.
