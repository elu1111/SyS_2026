El **Bloque V** es la etapa de cierre, donde la teoría abstracta se convierte en herramientas de ingeniería. Aquí aterrizamos los conceptos de las transformadas en aplicaciones prácticas como el diseño de filtros, el procesamiento digital de señales (DSP) y la representación de sistemas para ser simulados en computadora.

---

## Bloque V: Aplicaciones, Filtros y Simulación (Semanas 11-15)

Este bloque utiliza secciones específicas del **Oppenheim** (Capítulos 6, 7 y 11) y se complementa con técnicas de implementación moderna.

### Semana 11: Muestreo en Frecuencia y la DFT

**Clase 21: Muestreo en el Dominio de la Frecuencia**

* **La Transformada Discreta de Fourier (DFT):** Cómo representar el espectro de una señal mediante un número finito de muestras.
* **Relación entre la DTFT y la DFT:** Muestreo de la DTFT en el círculo unitario.
* **Resolución espectral:** El efecto del enventanado (*windowing*) y la longitud del registro de datos.

**Clase 22: Algoritmos y Procesamiento Rápido**

* **Introducción a la FFT:** Concepto de diezmación en tiempo y frecuencia (sin entrar en el detalle del código, pero sí en su eficiencia computacional).
* **Convolución Circular vs. Lineal:** Por qué la multiplicación en el dominio de la DFT no es exactamente igual a la convolución lineal y cómo corregirlo (*zero-padding*).

---

### Semana 12: Diseño de Filtros Digitales

**Clase 23: Estructuras de Filtros Digitales**

* **Representación mediante diagramas de bloques:** Sumadores, ganancias y retrasos ($z^{-1}$).
* **Formas Directas:** Forma Directa I y Forma Directa II (Canónica).
* **Efectos de la cuantización:** Breve introducción a los errores por precisión finita.

**Clase 24: Filtros FIR e IIR**

* **Filtros de Respuesta al Impulso Finita (FIR):** Propiedad de fase lineal y diseño por el método de ventanas (Hamming, Hann, Blackman).
* **Filtros de Respuesta al Impulso Infinita (IIR):** Diseño a partir de prototipos analógicos (Butterworth, Chebyshev) mediante la **Transformación Bilineal**.

---

### Semana 13: Modelización y Simulación de Sistemas

**Clase 25: Representación en Variables de Estado (State-Space)**

* **Concepto de Estado:** Cómo pasar de ecuaciones diferenciales/diferencias de orden $N$ a un sistema de $N$ ecuaciones de primer orden.
* **Ecuaciones de estado y de salida:** Matrices $A, B, C, D$.
* **Ventajas de la representación de estado:** Modelado multivariable y simulación numérica eficiente.

**Clase 26: Simulación Computacional**

* **Algoritmos de integración numérica:** Euler y Runge-Kutta (conceptos básicos aplicados a señales).
* **Simulación de sistemas realimentados:** Estabilidad numérica y retardo de transporte.
* **Uso de herramientas de software:** Breve repaso de cómo implementar estos modelos en entornos tipo MATLAB, Python (SciPy) o Simulink.

---

### Semana 14: Integración y Repaso Final

**Clase 27: Taller de Integración**

* Resolución de un problema "extremo-a-extremo": Desde la toma de una señal continua, su muestreo, filtrado digital y reconstrucción.
* Análisis de compromiso (*trade-offs*): Velocidad de muestreo vs. carga computacional.

**Clase 28: Sesión de Consultas**

* Repaso de los conceptos más complejos del Bloque IV (Z y Laplace) y Bloque V.
* Simulacro de examen parcial.

---

### Semana 15: Evaluación Final y Cierre

**Clase 29: SEGUNDO EXAMEN PARCIAL**

* **Temario:** Bloques III, IV y V (Muestreo, Laplace, Z, Filtros y Estado).

**Clase 30: Entrega de Notas y Coloquio Final**

* Revisión de exámenes.
* Conclusión de la asignatura y relación con materias correlativas (Control, Comunicaciones, DSP).

---

### Bibliografía específica para este bloque:

* **Oppenheim:** Capítulos 6 (Filtros), 7 (Muestreo/DFT), 10 (Estructuras de filtros) y 11 (Variables de estado/Realimentación).
* **Software:** Documentación de `scipy.signal` (Python) o `Signal Processing Toolbox` (MATLAB).

