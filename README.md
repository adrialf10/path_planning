# path_planning
Para ejecutar el algoritmo basta con compilar y ejecutar el fichero main.py.

En este fichero hay 4 variables al principio que se pueden modificar para cambiar las pruebas que se realicen con el algoritmo:
  start_point = Punto inicial del camino en coordenadas x,y.
  end_point = Punto final del camino en coordenadas x,y.
  image = Nombre de la imagen que contiene el laberinto, debe estar en la misma carpeta.
  use_pyrobotics = Variable booleana que indica si se quiere utilizar la implementación con la librería Python Robotics o con la librería propia.

Las coordenadas funcionan de la siguiente forma, siendo el eje superior izquierdo el (0,0):
      0                           100 
    0 |----------------------------|
      |                            |
      |                            |
      |                            |
      |                            |
      |                            |
  100 |----------------------------| 
