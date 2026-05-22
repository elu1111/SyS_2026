Este es el desglose detallado del **Bloque II**, centrado en el análisis de Fourier. En este tramo, pasamos del dominio del tiempo al **dominio de la frecuencia**, una de las transiciones conceptuales más desafiantes y potentes para los estudiantes.

---

## Bloque II: Análisis de Fourier (Semanas 3-6)

### Semana 3: Series de Fourier (Señales Periódicas)

**Clase 5: Serie de Fourier en Tiempo Continuo (CTFS)**

* **Respuesta de sistemas LTI a exponenciales complejas:** El concepto de "autofunciones" y "autovalores" ($H(j\omega)$).
* **Representación de señales periódicas:** La ecuación de síntesis y la ecuación de análisis.
* **Determinación de coeficientes ($a_k$):** Ortogonalidad de las exponenciales complejas.
* **Fenómeno de Gibbs:** Comportamiento de la serie en discontinuidades (bordes de señales cuadradas).
* **Propiedades de la CTFS:** Linealidad, desplazamiento temporal, conjugación y simetría.
* **Relación de Parseval:** Distribución de la potencia en los armónicos.

**Clase 6: Serie de Fourier en Tiempo Discreto (DTFS)**

* **Diferencia fundamental con CTFS:** La periodicidad de las exponenciales discretas (solo existen $N$ coeficientes distintos).
* **Ecuaciones de síntesis y análisis para DTFS:** Sumatorias finitas.
* **Propiedades de la DTFS:** Periodicidad de los coeficientes $a_k$.
* **Sistemas LTI y Series de Fourier:** Filtrado de señales periódicas; cómo el sistema escala y desfasa cada armónico.

---

### Semana 4: Transformada de Fourier en Tiempo Continuo (CTFT)

**Clase 7: Representación de Señales Aperiódicas**

* **Extensión de la Serie de Fourier:** El límite cuando el periodo $T \to \infty$.
* **El par de la Transformada de Fourier:**
* Análisis: $X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt$
* Síntesis: $x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} d\omega$


* **Convergencia de la CTFT:** Condiciones de Dirichlet.
* **Ejemplos clásicos:** El pulso rectangular y la función **Sinc**.

**Clase 8: Propiedades y Sistemas LTI en Frecuencia**

* **Propiedades clave:** Desplazamiento en tiempo/frecuencia, escalamiento, diferenciación e integración.
* **Propiedad de Convolución:** El paso fundamental; $y(t) = x(t) * h(t) \iff Y(j\omega) = X(j\omega)H(j\omega)$.
* **Sistemas descritos por ecuaciones diferenciales:** Determinación de la función de transferencia $H(j\omega)$ mediante inspección.

---

### Semana 5: Transformada de Fourier en Tiempo Discreto (DTFT)

**Clase 9: Transformada de Fourier en Tiempo Discreto (DTFT)**

* **Definición y periodicidad:** Por qué $X(e^{j\omega})$ es siempre periódica con periodo $2\pi$.
* **Pares comunes:** Impulso, escalón, señales exponenciales causales ($a^n u[n]$).
* **Dualidad:** Comparación entre las cuatro transformaciones de Fourier (CTFS, DTFS, CTFT, DTFT).

**Clase 10: Propiedades de la DTFT y Repaso Integral**

* **Convolución en tiempo discreto:** Multiplicación en el dominio de la frecuencia digital.
* **Sistemas descritos por ecuaciones de diferencias:** Obtención de $H(e^{j\omega})$.
* **Repaso General:** Matriz comparativa de propiedades para el examen parcial. Resolución de dudas sobre convolución y Fourier.

---

### Semana 6: Evaluación del Bloque I y II

**Clase 11: Taller de Problemas**

* Resolución de exámenes de años anteriores.
* Énfasis en:
1. Propiedades de sistemas (linealidad/causalidad).
2. Cálculo de convoluciones gráficas.
3. Obtención de espectros de magnitud y fase de señales básicas.



**Clase 12: PRIMER EXAMEN PARCIAL**

* **Temario:** Capítulos 1 al 5 del Oppenheim.
* **Formato sugerido:** 2 problemas de sistemas LTI/convolución y 2 problemas de análisis de Fourier (uno CT y uno DT).

---

### Bibliografía específica para este bloque:

* **Oppenheim:** Capítulos 3, 4 y 5 completos.
* **Ejercicios clave:** 3.22 (coeficientes de serie), 4.21 (pares de transformada CT) y 5.21 (pares de transformada DT).

