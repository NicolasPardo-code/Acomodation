# Estimar Acomodacion

En este proyecto se propone crear un modelo de ML capaz de hacer una recomendacion de la mejor acomodacion (Hotel o Airbnb) para un usuario basado en algunos de sus datos (Genero, Edad, Destino, Niños, duracion de la estadia),

Los datos en crudo se encuentran en el archivo train_data.txt
En data_procesing.ipynb se encuentra el script necesario para parcear la data a un CSV
Los modelos que se intentaron implentar fueron:
   - Estimator.DNNClassifier (NN.ipynb)
   - Naive_bayes.MultinomialNB (bayes.ipynb)
   - Logistic regression (logistic regression.ipynb)
   - Decision tree (tree.ipynb)

Los primeros tres modelos no fueron implementado exitosamente ya que al momento de hacer la predición retornaban siempre el mismo valor, mostrando un comportamiento claramente erroneo.

El unico modelo con resultados coherentes fue el decision tree, el dataset fue modificado para un funcionamiento optimo y mejorar la precision en la las predicciones del modelo, las modificaciones fueron:

- Eliminar la columna ID, ya que esta no contiene ninguna información util para el modelo y es solo un identificador.
- Se eliminaron las columnas "Pais" y "Dias", ya que al usar la funcion featured_importances_ estas dos columnas mostraban la menor relevancia y hacian al arbol de decision excesivamente grande.
- Se sustituyeron los valores nulos de la columna "Edad" con la mediana de la misma, ya que esta medida de centralidad se ve menos afectada por los outliers.
- Se sustituyeron los valores nulos de la columna "Niños" con el ultimo registro valido de esa columna con esto se consigue mantener la proporcion de valores.
- La columna "Genero" fue modificada para remplazar "F" y "M" por 0 y 1 respectivamente.

Este modelo fue aplicado al archivo "DataAcomodacion.csv" para predecir el valor de la columna 'Acomodacion', este proceso fue realizado a traves del script "Acomodacion.py" y el resultado del mismo se encuentra en "resultado.csv".