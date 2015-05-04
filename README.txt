Si usted quiere generar el pdf se le avisa que con compilar el .tex dentro de latex no obtendrá el resultado deseado.

El método correcto para compilar el latex es usando el Makefile de la carpeta raiz:

$ make

Esto se debe a que en el repositorio no se guardan las imagenes que se usan en el documento, estas se crean a través de un código python el cual guarda las imagenes que después usa el latex. 

Si desea hacer los procedimientos sin el makefile usted debe crear la carpeta img dentro de la carpeta latex, posteriormente en la carpeta CodigoPython ejecutar cada programa python, y finalmente generar el pdf desde el .tex en la carpeta latex.