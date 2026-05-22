En el **Bloque IV** nos adentramos en el análisis de sistemas en el plano complejo. Mientras que Fourier nos permitía ver "qué frecuencias" componen una señal, las transformadas de **Laplace** y **Z** nos permiten analizar la **estabilidad**, la **transitoriedad** y los sistemas que no necesariamente convergen en Fourier.

---

## Bloque IV: Transformadas Complejas ($s$ y $z$) (Semanas 9-10)

Este bloque se basa en los capítulos 9 y 10 del texto de **Oppenheim**. Es la herramienta definitiva para el diseño de sistemas de control y filtrado.

### Semana 9: La Transformada de Laplace (Tiempo Continuo)

**Clase 17: Definición y Región de Convergencia (ROC)**

* **De Fourier a Laplace:** Generalización de la transformada mediante la variable compleja $s = \sigma + j\omega$.
* **Definición de la Transformada bilateral:**

$$X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt$$


* **La Región de Convergencia (ROC):** Por qué el álgebra no es suficiente; importancia de la ROC para identificar la señal original.
* **Propiedades de la ROC:** Relación con la causalidad y la duración de la señal (señales de lado derecho, izquierdo y biltaterales).
* **Diagrama de Polos y Ceros:** Visualización de la función de transferencia $H(s)$ en el plano $s$.

**Clase 18: Propiedades y Estabilidad de Sistemas LTI**

* **Propiedades de Laplace:** Linealidad, desplazamiento, escalamiento y el teorema del valor inicial/final.
* **Transformada de Laplace Inversa:** Uso de fracciones parciales para volver al dominio del tiempo.
* **Análisis de Sistemas LTI:**
* Función de transferencia $H(s)$.
* **Causalidad:** La ROC es un semiplano a la derecha del polo más a la derecha.
* **Estabilidad:** Un sistema LTI es estable si y solo si la ROC incluye el eje $j\omega$ (equivalente a decir que todos los polos están en el semiplano izquierdo para sistemas causales).



---

### Semana 10: La Transformada Z (Tiempo Discreto)

**Clase 19: Definición y el Plano Z**

* **Generalización en tiempo discreto:** La variable compleja $z = re^{j\omega}$.
* **Definición de la Transformada Z:**

$$X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}$$


* **Relación entre el plano $s$ y el plano $z$:** El mapeo del eje imaginario de $s$ al círculo unitario de $z$.
* **ROC en el plano Z:** Representación como anillos concéntricos. Propiedades de la ROC para secuencias finitas, derechas e izquierdas.

**Clase 20: Propiedades, Inversa y Estabilidad**

* **Propiedades de la Transformada Z:** Desplazamiento temporal (el operador $z^{-1}$ como delay), convolución y diferenciación en el dominio $z$.
* **Transformada Z Inversa:** Método de expansión en fracciones parciales y división larga (series de potencias).
* **Caracterización de Sistemas LTI en el dominio $z$:**
* **Estabilidad:** Un sistema LTI discreto es estable si la ROC incluye el círculo unitario ($|z|=1$).
* Para sistemas causales, esto implica que todos los polos deben estar **dentro** del círculo unitario.



---

### Bibliografía específica para este bloque:

* **Oppenheim:** Capítulo 9 (Laplace) y Capítulo 10 (Z-Transform).
* **Ejercicios recomendados:** 9.21 y 9.22 (identificar señales a partir de polos y ROC), 10.21 y 10.22 (transformada Z y diagramas de polos y ceros).

---

