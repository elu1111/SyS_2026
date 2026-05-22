A continuación, se detalla el contenido del **Bloque III**, que es el puente fundamental entre el procesamiento de señales analógicas y el mundo digital. Este bloque se basa principalmente en los capítulos 6 y 7 del texto de **Oppenheim**.

---

## Bloque III: Caracterización y Muestreo (Semanas 7-8)

Este bloque se enfoca en cómo los sistemas afectan la forma de la señal (magnitud y fase) y cómo podemos representar una señal continua mediante una secuencia de números sin perder información.

### Semana 7: Caracterización de Sistemas en Tiempo y Frecuencia

**Clase 13: Respuesta en Magnitud y Fase**

* **Análisis de la respuesta en frecuencia:** Representación de $H(j\omega)$ y $H(e^{j\omega})$ en forma polar.
* **Efectos de la Fase:** Concepto de retraso de grupo (*group delay*) y distorsión de fase. Importancia de la fase lineal.
* **Escalas Logarítmicas:** Introducción a los diagramas de Bode (magnitud en dB y fase en grados).
* **Relación Tiempo-Frecuencia:** Cómo el ancho de banda en frecuencia afecta la rapidez de respuesta (tiempo de subida) en el dominio del tiempo.

**Clase 14: Filtros y Sistemas de Segundo Orden**

* **Filtros Ideales:** Pasabajos, pasaaltos y pasabanda. La imposibilidad física de los filtros ideales (causalidad).
* **Filtros No Ideales:** Concepto de banda de paso, banda de transición y banda de rechazo.
* **Sistemas de primer y segundo orden:** * Tiempo continuo: Circuitos RC, RLC y su respuesta en frecuencia.
* Tiempo discreto: Ecuaciones de diferencias de primer y segundo orden.
* Análisis de resonancia y amortiguamiento.



---

### Semana 8: El Teorema del Muestreo

**Clase 15: Muestreo en el Dominio del Tiempo**

* **Representación del muestreo como una multiplicación:** El tren de impulsos unitarios como señal de muestreo.
* **Efecto en el espectro:** Replicación del espectro de la señal original en múltiplos de la frecuencia de muestreo $\omega_s$.
* **El Teorema de Nyquist-Shannon:** Condición para evitar el solapamiento (*aliasing*): $\omega_s > 2\omega_M$.
* **Aliasing:** Qué ocurre cuando se submuestrea una señal (ejemplos visuales y auditivos).

[Image showing the frequency spectrum of a sampled signal and the effect of aliasing when spectra overlap]

**Clase 16: Reconstrucción y Procesamiento Digital**

* **Reconstrucción de señales:** El filtro pasabajos ideal como interpolador.
* **Interpolación práctica:** Retención de orden cero (*Zero-Order Hold*) y de primer orden.
* **Procesamiento de tiempo continuo en tiempo discreto:** * Diagrama de bloques: C/D (Conversor Continuo a Discreto) $\to$ Sistema LTI Discreto $\to$ D/C (Conversor Discreto a Continuo).
* Cómo diseñar un sistema digital que emule un filtro analógico.


* **Diezmación e Interpolación:** Conceptos básicos de cambio de la frecuencia de muestreo en el dominio discreto.

---

### Bibliografía específica para este bloque:

* **Oppenheim:** Capítulo 6 (Secciones 6.1 a 6.5) y Capítulo 7 (Secciones 7.1 a 7.5).
* **Ejercicios recomendados:** Problemas 6.21 (diagramas de magnitud y fase), 7.21 y 7.22 (cálculo de frecuencias de Nyquist y reconstrucción).

---

