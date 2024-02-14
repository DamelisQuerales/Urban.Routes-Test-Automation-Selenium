## Tabla de contenidos
1. [Información General]
2. [Technologías]
3. [Instalación]
4. [Metodología]
5. [Conclusión]
### Información general
***
**Automatización de pruebas de la aplicación Urban.Routes con Selenium**

Este documento describe la automatización de pruebas de la aplicación Urban.Routes utilizando el framework Selenium. El objetivo de las pruebas es verificar la funcionalidad de reserva de taxi, incluyendo:

**Validación de campos de entrada:** Se comprueba que los campos de número de teléfono, tarjeta de pago y preferencias del usuario funcionen correctamente.
**Confirmación de reserva:** Se verifica que la reserva de taxi se realiza correctamente y se recibe la información de confirmación.

**Las pruebas se implementaron utilizando los siguientes métodos:**

**Localización de elementos:** Se utilizaron localizadores con la clase By para identificar los elementos en la página web. La clase By permite especificar diferentes criterios de búsqueda, como el nombre del elemento, la clase CSS o el ID.
**Interacción con la aplicación:** Se crearon métodos para interactuar con los elementos de la página web, como completar formularios, hacer clic en botones y verificar el contenido de la página.
**Aserciones:** Se utilizaron aserciones para verificar que el comportamiento de la aplicación coincide con el esperado.


## Tecnologías
***
Lista de tecnologías utilizadas en este proyecto:
* [Paycharm](https://example.com): Version 2023.3.2 
* [Pytest](https://example.com): Version 7.1.0
* [ChromeDriver-Selenium]: Version 121.0.6167.85
* [Google Chrome]: Versión 121.0.6167.140
## Instalación
***

 
```
$ git clone https://github.com/DamelisQuerales/qa-project-07-es.git
$ cd ../projects/qa-project-07-es
$ npm install
$ npm start
```
Información adicional: se trabajo de manera local con PyCharm
## Contenido
***

> En el archivo main.py contiene los método y localizadores
> Los casos de prueba se añadieron en el archivo test_cases.py
> La URL y los datos de entrada se encuentran en el archivo data.py

## Principios
***

Este proyecto utiliza el patrón de diseño POM (Page Object Model) para facilitar el mantenimiento del código de prueba. El POM organiza la lógica de las pruebas en diferentes clases, cada una representando una página de la aplicación web bajo prueba.

Beneficios del POM:

1. **Mantenimiento:** Facilita la organización y el mantenimiento del código de prueba, al separar las pruebas de la lógica de la aplicación.

2. **Reutilización:** Permite reutilizar código en diferentes pruebas, reduciendo la duplicación y mejorando la eficiencia.

3. **Lectura:** Hace que el código de prueba sea más legible y comprensible.

4. **Independencia:** Permite que las pruebas sean más independientes unas de otras, reduciendo el impacto de los cambios en la aplicación.

**En este proyecto:**
- Cada clase contiene los localizadores de los elementos de la página, los métodos para interactuar con esos elementos y las pruebas para esa página.
- Las pruebas se organizan en archivos separados, cada uno correspondiente a una clase de página.


### Conclusión
***
La automatización de las pruebas de la aplicación Urban.Routes con Selenium ha demostrado ser una herramienta eficaz para mejorar la calidad y la confiabilidad de la aplicación. Las pruebas automatizadas ayudan a garantizar que la aplicación funcione correctamente y que los usuarios tengan una experiencia satisfactoria.

Los resultados obtenidos:
9 Casos de prueba --> PASSED [100%]