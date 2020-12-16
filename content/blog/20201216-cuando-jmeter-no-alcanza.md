---
title: "Cuándo JMeter no alcanza: Pruebas de carga simulando navegadores"
date: 2020-12-16T18:18:23+01:00
draft: false
tags: ['performance', 'español', 'jmeter', 'browsers', 'flood element', 'selenium', 'gatling', 'cypress', 'jest', 'puppeteer', 'playwright', 'video', 'presentation', 'text']
---

Aquí está el video de mi presentación en JMeter Scripting Day, un evento organizado por [JMeter en Español](https://jmeterenespanol.org/) el 31 de Oktubre, 2020.

{{< youtube 1KB8e2Ld08M >}}

## Introducción

Hola a todos! Yo soy Nicole van der Hoeven, y soy performance tester. JMeter es una de mis herramientas favoritas porque es gratis, simple, y por muchos casos hace exactamente lo que quiero y no más. Sin embargo, como performers es parte de nuestro trabajo elegir la herramienta adecuada para cada proyecto, y hay que admitir que hay situaciones en que JMeter simplemente no es suficiente.

## Amazon - UI + Dev Tools 

Esto es el sitio web de Amazon.com. Tengo abierta la pantalla de Chrome Developer Tools, que me muestra las solicitudes (o requests) que componen la página. Cuándo vamos a la página, el navegador (Chrome en este caso) envia estas solicitudes para nosotros, pero eso occure en el fondo. Un usuario normal no las ve. 

## JMeter - Creando un script
   
Lo que JMeter hace es grabar estas solicitudes y replicarlas. Aqui vemos una ejecución de un usuario virtual de un script en JMeter. Cada solicitud tiene la respuesta y el tiempo de respuesta. Pero eso no nos da una idea completa del rendimiento de la aplicación. ¿Por qué?

Por que JMeter, como otras herramientas de nivel protocolo, tiene unas limitaciónes. La primera es que si hay javascript o otros script que deben estar ejecutado por el navegador, JMeter no los ejecuta. JMeter solo los descarga. El tiempo de respuesta mide la descarga, no la duración de la ejecución. Entonces, siempre habrá una diferencia entre los tiempos de respuesta en una prueba de JMeter y los tiempos de respuesta en práctica.

A veces esta diferencia no es tan importante. Pero hay más y más aplicaciones hoy en día que se componen principalmente de estos javascript. Por esas aplicaciones, simplemente no es posible hacer un script en JMeter porque la mayoría de la lógica de la aplicación occure en el navegador, no en el servidor.

## Flood Challenge

La segunda razón es que el aumento de la seguridad de aplicaciones conduce a solicitudes más complejas que incluyen parámetros dinámicos. Estos parámetros hacen que sea más difícil para un intermediario lanzar un ataque, pero también hacen que sea más difícil para nosotros scripters, porque tenemos que extraer información desde la última respuesta y ponerla en la próxima solicitud. Es posible, pero es la pesadilla de cada performance tester.
    
Podemos verlo en la aplicación de muestra [Flood Challenge](https://challenge.flood.io). Ya no trabajo para Flood, pero todavía es un buen ejemplo.

## Correlación en JMeter - Flood challenge script

Esto es mi script en JMeter, y vemos que hay muchos parámetros que he tenido que correlacionar. La solicitud para simular hacer clic en el botón "Start" necesita los parámetros authenticity token, step ID, y step number, que son dinámicos. El contenido de los parámetros cambian cada vez que usamos esta aplicación.

## La experiencia del usuario

La tercera razón es que JMeter tampoco mide la verdadera experiencia del usuario. Solo mide la duración de la comunicación entre el navegador y el servidor, pero no mide cosas como la representación de elementos en la página web, ni el efecto de un script que dura mucho tiempo para terminar.

Eso es importante porque estas cosas afectan significativamente la experiencia del usuario. De hecho, Steve Souders, un conocido el la industría de performance, dice que [hasta 90% del tiempo de respuesta](https://rigor.com/blog/80-90-of-load-times-are-spent-on-the-front-end-start-there/#:~:text=Start%20there.,-Written%20by%20Craig&text=Last%20month%2C%20Steve%20Souders%2C%20Google's,is%20spent%20on%20the%20frontend) que experimenta el usuario está en la interfaz. Con este numero podemos estar ciertos que una prueba con una herramienta de nivel protocolo no va a poder encapsular el rendimiento final de una aplicación.

## Developer Tools - Lighthouse

Entonces, ¿qué podemos hacer?

Lo más fácil es intentar de medir la interfaz durante una prueba de cargas. Mientras ejecutamos una prueba con JMeter, podemos ir manualmente a la aplicación web en Chrome para usar Developer Tools. Podemos usar la pestaña Lighthouse, que nos da más métricos del perspectivo del usuario y sugerencias para mejorar el rendimiento.

## WebPageTest

También uso [WebPageTest](https://webpagetest.org) a veces. Eso tiene más opciones para ejecutar la prueba automáticamente varias veces desde un lugar que puedo elegir. Aún podemos elegir un dispositivo para simular la experiencia de un usuario en un iPad, por ejemplo.

## Herramientas alternativas para pruebas de carga

Tambien podemos elegir herramientas alternativas para ejecutar nuestras pruebas de carga. Lo que tienen en común es que fueron diseñadas para pruebas de automatización, y utilizan un navegador real.

[Selenium](https://www.selenium.dev/) es probablemente la más popular de esas. Selenium WebDriver en particular. Es compatible con Ruby, Java, Python, C# y Javascript. El problema con Selenium es que puede ser muy pesada. En una machina probablamente podemos ejecutar cinco usuarios de Selenium, más o menos. Eso es importante si estamos tratando de simular miles de usuarios.

Hay muchas herramientas basadas en Javascript que también podemos usar. Hay varias framework que se utilizan para adaptar Javascript y nodeJS. 

* Puppeteer fue desarollado por Google. Tricentis Flood también ha diseñado Element que utiliza Puppeteer, pero con un enfoque en el rendimiento.

* [Playwright](https://github.com/microsoft/playwright) es una creación de Microsoft.

* [Jest](https://jest.io) fue desarrollado por Facebook

* Mocha es otro framework que es la base para [Cypress](https://cypress.io).

Todos esas herramientas son open source y gratis. También hay alternativas propietarias, pero prefiero las soluciones open source porque en la mayoría de casos hacen la misma cosa y se actualizan con más frecuencia.

## Element script

Esto es un ejemplo de la misma acción, hacer clic en el botón Start en la aplicación Flood Challenge.

Otra ventaja de simulando navegadores en vez de simulando las solicitudes es que es más simple crear un script. No tenemos que saber cada parámetro. Solo tenemos que describir lo que queremos que cada usuario virtual haga. 

Podemos ejecutar scripts usando estas herramientas al mismo tiempo que un script de [JMeter](https://jmeter.apache.org) o [Gatling](https://gatling.io) o lo que sea, y también tenemos la opción de reemplazar los script de protocolo con estas. 

## Conclusión
Para resumir, JMeter y otras herramientas de nivel protocolo tiene algunas limitaciones.

* No ejecutan scripts del lado del navegador

* Pueden ser más complicado correlacionar parámetros dinámicos

* No miden la experiencia final de un usuario

Para solucionar estos problemas, podemos complementar pruebas de carga tradicionales, de nivel protocolo, como JMeter, con herramientas simulando navegadores. De este modo podremos tener una comprensión más completa del rendimiento total de la aplicación. 

Bueno, se acabó el tiempo, entonces los dejo aquí. Gracias por escuchar, y me disculpo por mi español. Gracias a todos!