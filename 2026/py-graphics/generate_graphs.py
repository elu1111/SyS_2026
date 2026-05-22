import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import os

# --- Funciones auxiliares ---
def mrange(start, step, stop):
    """
    Emula el comportamiento de start:step:stop de MATLAB,
    asegurándose de incluir el límite superior.
    """
    return np.arange(start, stop + (step / 10), step)

def save_fig(filename):
    """
    Ajusta el layout para que no se superpongan los textos
    y guarda la figura en formato PNG.
    """
    plt.tight_layout()
    plt.savefig('./target/' + filename + '.png', dpi=150)
    plt.close()

# =========================================================
# SCRIPT DE GENERACIÓN DE GRÁFICOS
# =========================================================

# 1. cos2tcoarse
t = mrange(-np.pi, 0.5, np.pi)
xt = np.cos(2*t)
plt.figure()
plt.plot(t, xt)
plt.xlabel('t')
plt.ylabel('cos(2*t)')
plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('cos2tcoarse')

# 2. cos2t
t = mrange(-np.pi, 0.01, np.pi)
xt = np.cos(2*t)
plt.figure()
plt.plot(t, xt)
plt.xlabel('t')
plt.ylabel('cos(2*t)')
plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('cos2t')

# 3. cosdisc
n = mrange(-10, 1, 10)
xn = np.cos(2 * np.pi * n / 10)
plt.figure()
plt.stem(n, xn)
plt.axis([-10, 10, -1.2, 1.2])
plt.xlabel('n')
plt.ylabel('cos(2 * pi * n / 10)')
save_fig('cosdisc')

# 4. contvart
plt.figure()
plt.subplot(3,1,1)
plt.plot(t, np.exp(t/10))
plt.title('exp(t/10)')
plt.axis([-np.pi, np.pi, -0.2, 3])

plt.subplot(3,1,2)
plt.plot(t, np.exp(1/20 * t + 1/3))
plt.title('exp(1/20 * t + 1/3)')
plt.axis([-np.pi, np.pi, -0.2, 3])

plt.subplot(3,1,3)
plt.plot(t, np.exp(-1/20 * t + 1/3))
plt.title('exp(-1/20 * t + 1/3)')
plt.axis([-np.pi, np.pi, -0.2, 3])
save_fig('contvart')

# 5. contfase
plt.figure()
plt.subplot(3,1,1); plt.plot(t, np.cos(15*t)); plt.title('cos(15*t)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
plt.subplot(3,1,2); plt.plot(t, np.cos(15*t+1)); plt.title('cos(15*t+1)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
plt.subplot(3,1,3); plt.plot(t, np.cos(15*t-1)); plt.title('cos(15*t-1)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('contfase')

# 6. contfrec
plt.figure()
plt.subplot(3,1,1); plt.plot(t, np.cos(20*t)); plt.title('cos(20*t)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
plt.subplot(3,1,2); plt.plot(t, np.cos(15*t)); plt.title('cos(15*t)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
plt.subplot(3,1,3); plt.plot(t, np.cos(10*t)); plt.title('cos(10*t)'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('contfrec')

# 7. discvart
n = mrange(-10, 1, 10)
plt.figure()
plt.subplot(3,1,1); plt.stem(n, np.exp(n/10)); plt.title('exp(n/10)'); plt.axis([-10, 10, -0.2, 3])
plt.subplot(3,1,2); plt.stem(n, np.exp(1/20 * n + 1/3)); plt.title('exp(1/20 * n + 1/3)'); plt.axis([-10, 10, -0.2, 3])
plt.subplot(3,1,3); plt.stem(n, np.exp(-1/20 * n + 1/3)); plt.title('exp(-1/20 * n + 1/3)'); plt.axis([-10, 10, -0.2, 3])
save_fig('discvart')

# 8. discfase
plt.figure()
plt.subplot(3,1,1); plt.stem(n, np.cos(15*n)); plt.title('cos(15*n)'); plt.axis([-10, 10, -1.2, 1.2])
plt.subplot(3,1,2); plt.stem(n, np.cos(15*n+2)); plt.title('cos(15*n+2)'); plt.axis([-10, 10, -1.2, 1.2])
plt.subplot(3,1,3); plt.stem(n, np.cos(15*n-2)); plt.title('cos(15*n-2)'); plt.axis([-10, 10, -1.2, 1.2])
save_fig('discfase')

# 9. discfrec
plt.figure()
plt.subplot(3,1,1); plt.stem(n, np.cos(20*n)); plt.title('cos(20*n)'); plt.axis([-10, 10, -1.2, 1.2])
plt.subplot(3,1,2); plt.stem(n, np.cos(15*n)); plt.title('cos(15*n)'); plt.axis([-10, 10, -1.2, 1.2])
plt.subplot(3,1,3); plt.stem(n, np.cos(10*n)); plt.title('cos(10*n)'); plt.axis([-10, 10, -1.2, 1.2])
save_fig('discfrec')

# 10. contpar
plt.figure()
plt.plot(t, np.cos(t)); plt.title('funcion par'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('contpar')

# 11. contimpar
plt.figure()
plt.plot(t, np.sin(t)); plt.title('funcion impar'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('contimpar')

# 12. discimpar
plt.figure()
plt.stem(n, n*n*n/100); plt.title('n^3/100 funcion impar'); plt.axis([-10, 10, -10, 10])
save_fig('discimpar')

# 13. discpar
plt.figure()
plt.stem(n, n*n/10); plt.title('n^2/10 funcion par'); plt.axis([-10, 10, -0.2, 10])
save_fig('discpar')

# 14. contparimpar
xpt = np.cos(5*t) + np.sin(10*t)
xnt = np.cos(-5*t) + np.sin(-10*t)
plt.figure()
plt.subplot(3,1,1); plt.plot(t, xpt); plt.title('cos(5*t)+sin(10*t)'); plt.axis([-np.pi, np.pi, -2.4, 2.4])
plt.subplot(3,1,2); plt.plot(t, (xpt+xnt)/2); plt.title('parte par'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
plt.subplot(3,1,3); plt.plot(t, (xpt-xnt)/2); plt.title('parte impar'); plt.axis([-np.pi, np.pi, -1.2, 1.2])
save_fig('contparimpar')

# 15. discparimpar
xpn = n*n*n/100 + n*n/10
xnn = (-n)*(-n)*(-n)/100 + (-n)*(-n)/10
plt.figure()
plt.subplot(3,1,1); plt.stem(n, xpn); plt.title('n^3/100+n^2/10'); plt.axis([-10, 10, -20, 20])
plt.subplot(3,1,2); plt.stem(n, (xpn+xnn)/2); plt.title('parte par'); plt.axis([-10, 10, -10, 10])
plt.subplot(3,1,3); plt.stem(n, (xpn-xnn)/2); plt.title('parte impar'); plt.axis([-10, 10, -10, 10])
save_fig('discparimpar')

# 16-21. Señales Singulares
xn = np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
yn = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])

plt.figure(); plt.stem(n, xn); plt.title('Impulso unitario'); plt.axis([-10, 10, -0.2, 1.2]); save_fig('impunidisc')
plt.figure(); plt.stem(n, yn); plt.title('Escalon unitario'); plt.axis([-10, 10, -0.2, 1.2]); save_fig('escunidisc')
plt.figure(); plt.stem(n+2, xn); plt.title('Impulso unitario desplazado'); plt.axis([-10, 10, -0.2, 1.2]); save_fig('impunidiscdesp')
plt.figure(); plt.stem(n+2, yn); plt.title('Escalon unitario desplazado'); plt.axis([-10, 10, -0.2, 1.2]); save_fig('escunidiscdesp')
plt.figure(); plt.stem(n+2, -xn); plt.title('Impulso unitario desplazado y multiplicado'); plt.axis([-10, 10, -1.2, 1.2]); save_fig('impunidiscdespmult')
plt.figure(); plt.stem(n+2, yn); plt.title('Escalon unitario desplazado y multiplicado'); plt.axis([-10, 10, -1.2, 1.2]); save_fig('escunidiscdespmult')

# 22. diversa
try:
    mat = sio.loadmat('diversa.mat')
    logica = mat['logica']
    continua = mat['continua']
    t_div = mrange(0, 1, 15)
    z_div = np.zeros_like(t_div)

    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(logica[:,0], logica[:,1], 'b')
    plt.plot(t_div, z_div, 'r')
    plt.title('Representacion logica')
    plt.axis([0, 15, -0.4, 1.4])

    plt.subplot(2,1,2)
    plt.plot(continua[:,0], continua[:,1], 'b')
    plt.plot(t_div, z_div, 'r')
    plt.title('Representacion continua')
    plt.axis([0, 15, -0.4, 1.4])
    save_fig('diversa')
except FileNotFoundError:
    print("Aviso: 'diversa.mat' no encontrado. Se omitió la generación de 'diversa.png'.")

# 23. percont
t_per = mrange(0, 0.01, 50)
xt_per = np.cos(2 * np.pi / 10 * t_per)
plt.figure()
plt.plot(t_per, xt_per)
plt.axis([0, 50, -1.2, 1.2])
plt.xlabel('t'); plt.ylabel('cos(2 * pi * t / 10)')
plt.title('Funcion periodica x(t) = cos(2 * pi * t / 10)')
save_fig('percont')

# 24. perdisc
n_per = mrange(0, 1, 50)
xn_per = np.cos(2 * np.pi / 10 * n_per)
plt.figure()
plt.stem(n_per, xn_per)
plt.axis([0, 50, -1.2, 1.2])
plt.xlabel('n'); plt.ylabel('cos(2 * pi * n / 10)')
plt.title('Funcion periodica x[n] = cos[2 * pi * n / 10]')
save_fig('perdisc')

# 25. noperdisc
xdn = np.cos(7/11 * n_per)
xcn = np.cos(7/11 * t_per)
z_per = np.zeros_like(t_per)
plt.figure()
plt.stem(n_per, xdn)
# t_per[0:5000:20] emula a t(1:20:5000) de MATLAB
plt.plot(t_per[0:5000:20], xcn[0:5000:20], 'r-')
plt.plot(t_per, z_per, 'b-')
plt.axis([0, 50, -1.2, 1.2])
plt.xlabel('n'); plt.ylabel('cos(7 * n / 10)')
plt.title('Funcion discreta no periodica con envolvente continua periodica')
save_fig('noperdisc')

# 26. sucimpcont
t11 = mrange(-3, 0.1, 0); x11 = np.zeros_like(t11)
xe112 = mrange(0, 0.1, 1); te112 = 0 * np.ones_like(xe112)
t12 = mrange(0, 0.1, 1); x12 = np.ones_like(t12)
xe123 = mrange(0, 0.1, 1); te123 = 1 * np.ones_like(xe123)
t13 = mrange(1, 0.1, 3); x13 = np.zeros_like(t13)

t21 = mrange(-3, 0.1, 0); x21 = np.zeros_like(t21)
xe212 = mrange(0, 0.1, 1) * 2; te212 = 0 * np.ones_like(xe212)
t22 = mrange(0, 0.1, 1) / 2; x22 = 2 * np.ones_like(t22)
xe223 = mrange(0, 0.1, 1) * 2; te223 = 0.5 * np.ones_like(xe223)
t23 = mrange(0.5, 0.1, 3); x23 = np.zeros_like(t23)

t31 = mrange(-3, 0.1, 0); x31 = np.zeros_like(t31)
xe312 = mrange(0, 0.1, 1) * 4; te312 = 0 * np.ones_like(xe312)
t32 = mrange(0, 0.1, 1) / 4; x32 = 4 * np.ones_like(t32)
xe323 = mrange(0, 0.1, 1) * 4; te323 = 0.25 * np.ones_like(xe323)
t33 = mrange(0.25, 0.1, 3); x33 = np.zeros_like(t33)

plt.figure()
plt.plot(t11,x11,'k'); plt.plot(te112,xe112,'k'); plt.plot(t12,x12,'k'); plt.plot(te123,xe123,'k'); plt.plot(t13,x13,'k')
plt.plot(t21,x21,'b'); plt.plot(te212,xe212,'b'); plt.plot(t22,x22,'b'); plt.plot(te223,xe223,'b'); plt.plot(t23,x23,'b')
plt.plot(t31,x31,'r'); plt.plot(te312,xe312,'r'); plt.plot(t32,x32,'r'); plt.plot(te323,xe323,'r'); plt.plot(t33,x33,'r')
plt.axis([-3, 3, -0.5, 4.5])
save_fig('sucimpcont')

# 27. sucesccont
t11 = mrange(-3, 0.1, 0); x11 = np.zeros_like(t11)
t12 = mrange(0, 0.1, 1); x12 = t12 * np.ones_like(t12)
t13 = mrange(1, 0.1, 3); x13 = np.ones_like(t13)

t21 = mrange(-3, 0.1, 0); x21 = np.zeros_like(t21)
t22 = mrange(0, 0.1, 1) / 2; x22 = t22 * (2 * np.ones_like(t22))
t23 = mrange(0.5, 0.1, 3); x23 = np.ones_like(t23)

t31 = mrange(-3, 0.1, 0); x31 = np.zeros_like(t31)
t32 = mrange(0, 0.1, 1) / 4; x32 = t32 * (4 * np.ones_like(t32))
t33 = mrange(0.25, 0.1, 3); x33 = np.ones_like(t33)

plt.figure()
plt.subplot(3,1,1); plt.plot(t11,x11,'b'); plt.plot(t12,x12,'b'); plt.plot(t13,x13,'b'); plt.axis([-3, 3, -0.5, 1.5])
plt.subplot(3,1,2); plt.plot(t21,x21,'b'); plt.plot(t22,x22,'b'); plt.plot(t23,x23,'b'); plt.axis([-3, 3, -0.5, 1.5])
plt.subplot(3,1,3); plt.plot(t31,x31,'b'); plt.plot(t32,x32,'b'); plt.plot(t33,x33,'b'); plt.axis([-3, 3, -0.5, 1.5])
save_fig('sucesccont')

# 28. limesccont
t11 = mrange(-3, 0.1, 0); x11 = np.zeros_like(t11)
x12 = mrange(0, 0.1, 1); t12 = np.zeros_like(x12)
t22 = mrange(0, 0.1, 3); x22 = np.ones_like(t22)

plt.figure()
plt.plot(t11,x11,'k'); plt.plot(t12,x12,'k'); plt.plot(t22,x22,'k')
plt.axis([-3, 3, -0.5, 1.5])
plt.title('u(t)')
save_fig('limesccont')

# 29. compesccont
t_lim = mrange(-2, 0.001, 4)
y = ((t_lim >= 0) & (t_lim <= 2)).astype(float)
z = np.zeros_like(t_lim)
plt.figure()
plt.plot(t_lim, z, '-', t_lim, y)
plt.axis([-2, 4, -0.5, 1.5])
plt.title('u(t) - u(t-2)')
save_fig('compesccont')

# 30. compescdisc
n_lim = mrange(-2, 1, 4)
x = ((n_lim >= 0) & (n_lim < 2)) * 1.0
plt.figure()
plt.stem(n_lim, x)
plt.axis([-2, 4, -0.5, 1.5])
plt.title('u[n] - u[n-2]')
save_fig('compescdisc')

# 31. compcontuno
t_c = mrange(-2, 0.1, 8)
x = t_c * ((t_c >= 0) & (t_c <= 2)) + (6 - t_c) * ((t_c >= 4) & (t_c <= 6))
z = np.zeros_like(t_c)
plt.figure()
plt.plot(t_c, x, 'b', t_c, z, 'g')
plt.axis([-2, 8, -0.5, 2.5])
save_fig('compcontuno')

# 32. compcontdos
n_c = mrange(-2, 1, 8)
x = (n_c * n_c) * ((n_c >= 0) & (n_c < 2)) - (n_c / 4) * ((n_c >= 4) & (n_c < 6))
plt.figure()
plt.stem(n_c, x)
plt.axis([-2, 8, -1.5, 1.5])
save_fig('compcontdos')

# 33. comppreguno
t_p = mrange(-2, 0.01, 10)
x1 = ((t_p >= 0) & (t_p < 2)) * 1.0
x2 = (~((t_p >= 2) & (t_p < 4))) * 1.0
x3 = ((t_p >= 4) & (t_p < 6)) * 1.0
x4 = (~((t_p >= 6) & (t_p < 8))) * 1.0
x = x1 + x2 + x3 + x4
y = t_p * x1 + (t_p - 4) * x2 + (t_p - 4) * x3 + (t_p - 8) * x4
plt.figure()
plt.subplot(1,2,1); plt.plot(t_p, x); plt.axis([-2, 10, -1.5, 1.5])
plt.subplot(1,2,2); plt.plot(t_p, y); plt.axis([-2, 10, -0.5, 2.5])
save_fig('comppreguno')

# 34. comppregdos
n_p = mrange(-2, 1, 10)
x1 = ((n_p >= 0) & (n_p < 2)) * 1.0
x2 = (~((n_p >= 2) & (n_p < 4))) * 1.0
x3 = ((n_p >= 4) & (n_p < 6)) * 1.0
x4 = (~((n_p >= 6) & (n_p < 8))) * 1.0
x = x1 + x2 + x3 + x4
y = n_p * x1 + (n_p - 4) * x2 + (n_p - 4) * x3 + (n_p - 8) * x4
plt.figure()
plt.subplot(1,2,1); plt.stem(n_p, x); plt.axis([-2, 10, -1.5, 1.5])
plt.subplot(1,2,2); plt.stem(n_p, y); plt.axis([-2, 10, -0.5, 2.5])
save_fig('comppregdos')

# 35. lecture2
# Nota: MATLAB usa índices base 1.
# El array n_p va de -2 a 10 (13 elementos).
# El 3° elemento en MATLAB (índice 2 en Python) corresponde a n=0
# El 5° elemento en MATLAB (índice 4 en Python) corresponde a n=2
x1 = np.zeros_like(n_p)
x2 = np.copy(x1)
x1[2] = 1
x2[4] = 2

plt.figure()
plt.subplot(2,1,1); plt.stem(n_p, x2); plt.title('Impulso desplazado y multiplicado')
plt.subplot(2,1,2); plt.stem(n_p, x1); plt.title('Impulso unitario')
save_fig('lecture2')

print("¡Todos los gráficos han sido generados y guardados en formato PNG exitosamente!")
