# Ejemplo con la librería de Pandas / Examples with Pandas' Library
### Spanish:
Para más información visitar las siguientes URLs:

1. **Parte I**: Introducción a Pandas. (http://jarroba.com/pandas-python-ejemplos-parte-i-introduccion/)
2. **Parte II**: DataFrame: Lectura y Escritura, Mergeo de DataFrame's y GroupBy. (http://jarroba.com/pandas-python-ejemplos-parte-ii-io-merge-groupby/)
3. **Parte III**: Operaciones de "Pivot_table" con DataFrame's.(http://jarroba.com/pandas-python-ejemplos-parte-iii-pivot_table/)


### Sort description in English:
In this project is going to make an example with pandas' library in Python.

Will see the differences between Series and DataFrame:

  - **Series**: Is a unidimensional array with indexation. Similar to dictionary.
  - **DataFrame**: Data structure similar to excel or SQL table.
  

For this example i used the "MovieLens" data set that contains information of users, films and ratings. We'll see how transform the Movielens data set to a DataFrame, and work with this structure similarly to work as a database.

![alt movielensER](https://github.com/RicardoMoya/Example_Pandas/blob/master/MovieLens_ER.png)

## Prerequisites
Is necessary to install next libraries (with pip):
```ssh
$ pip install pandas
$ pip install numpy
```