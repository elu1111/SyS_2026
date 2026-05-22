A continuación, presento el desglose detallado de los contenidos para las primeras dos semanas de la asignatura, basándome en los capítulos 1 y 2 del texto de **Oppenheim, Willsky y Nawab**. Este bloque es fundamental, ya que establece el lenguaje matemático que usaremos el resto del cuatrimestre.

---

## Bloque I: Fundamentos y Sistemas LTI (Semanas 1-2)

### Semana 1: Definiciones y Propiedades Básicas

**Clase 1: Señales en Tiempo Continuo (CT) y Discreto (DT)**

* **Concepto de Señal:** Definición matemática y ejemplos físicos (voltaje, presión, señales digitales).
* **Transformaciones de la variable independiente:**
* Desplazamiento temporal: $x(t - t_0)$ y $x[n - n_0]$.
* Reflexión (Inversión): $x(-t)$ y $x[-n]$.
* Escalamiento temporal: $x(at)$ (compresión y expansión).


* **Señales Periódicas:** Definición de periodo fundamental $T$ y $N$.
* **Señales Elementales:**
* Exponenciales complejas y senoidales (diferencias de periodicidad entre CT y DT).
* La función impulso unitario ($\delta$) y escalón unitario ($u$). Relación entre ambas (derivada/integral y diferencia/suma).



**Clase 2: Definición y Propiedades de los Sistemas**

* **Interconexiones de sistemas:** Serie (cascada), paralelo y realimentación.
* **Propiedades Fundamentales:** (Definiciones y métodos de verificación)
* **Memoria:** Sistemas instantáneos vs. sistemas con memoria.
* **Invertibilidad:** Concepto de sistema inverso.
* **Causalidad:** Dependencia de valores presentes y pasados.
* **Estabilidad (BIBO):** Entradas acotadas producen salidas acotadas.
* **Invarianza en el tiempo:** El comportamiento no cambia con el tiempo.
* **Linealidad:** Principios de aditividad y homogeneidad (superposición).



---

### Semana 2: Sistemas Lineales Invariantes en el Tiempo (LTI)

**Clase 3: La Suma de Convolución (Tiempo Discreto)**

* **Representación de señales DT en términos de impulsos:** Cómo "desarmar" $x[n]$ usando $\delta[n-k]$.
* **Respuesta al Impulso ($h[n]$):** Definición como la huella dactilar del sistema.
* **La Suma de Convolución:** 
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$


* **Cálculo práctico:** Método gráfico (reflejar, desplazar y multiplicar) y método analítico.

**Clase 4: La Integral de Convolución y Propiedades de LTI**

* **Representación de señales CT en términos de impulsos:** El concepto del límite de pulsos estrechos.
* **La Integral de Convolución:**

$$y(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau) d\tau$$


* **Propiedades de los sistemas LTI:**
* Conmutatividad, Distributividad y Asociatividad.
* Caracterización de propiedades LTI a través de $h(t)$ o $h[n]$ (¿Cómo saber si un sistema LTI es causal o estable mirando solo su respuesta al impulso?).


* **Respuesta al Escalón:** Relación con la respuesta al impulso.

---

### Bibliografía específica para este bloque:

* **Oppenheim:** Capítulo 1 (Secciones 1.1 a 1.6) y Capítulo 2 (Secciones 2.1 a 2.4).
* **Ejercicios recomendados:** Problemas de fin de capítulo 1.21 a 1.27 (propiedades de sistemas) y 2.21 a 2.23 (convoluciones básicas).

