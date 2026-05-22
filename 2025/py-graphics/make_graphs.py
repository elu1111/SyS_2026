from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def ConfigurationException(Exception):
    def __init__(self):
        super(ConfigurationException).__init__('Configuration error')


def get_configuration_identifier(base_directory):
    return Path(base_directory, 'configuration.json')


def read_configuration(configuration_identifier):
    return json.load(open(configuration_identifier, 'r'))


def write_configuration(configuration_identifier, configuration):
    with open(configuration_identifier, 'w') as json_file:
         json.dump(configuration, json_file)

             
def ensure_configuration_exists(base_directory, default_configuration):
    configuration_identifier = get_configuration_identifier(base_directory)
    if configuration_identifier.exists():
        if configuration_identifier.is_file():
            configuration = read_configuration(configuration_identifier)
        else:
            raise ConfigurationException()
    else:
        configuration = default_configuration
        write_configuration(configuration_identifier, configuration)
    return configuration


class BaseApp(object):
    def __init__(self, name, target):
        home_user = Path('~').expanduser()
        base = name if name[0] == '.' else ('.' + name)
        base_directory = Path(home_user, base)
        target_directory = Path(home_user, target)
        base_directory.mkdir(mode=0o700, parents=True, exist_ok=True)
        target_directory.mkdir(mode=0o700, parents=True, exist_ok=True)
        self._base_directory = base_directory
        self._target_directory = target_directory
        self._configuration = ensure_configuration_exists(base_directory, {})
        plt.style.use("ggplot")

    @property
    def base_directory(self):
        return self._base_directory
    
    @property
    def target_directory(self):
        return self._target_directory
    
    @target_directory.setter
    def target_directory(self, value):
        self._target_directory = value
    
    @property
    def configuration(self):
        return self._configuration
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def figure_filename(self, name):
        return Path(self.target_directory, name + '.png')

    def get_ut(self, t, m):
        fm = lambda v: 0 if v < 0.0 else v / m if v < m else 1.0 
        return np.vectorize(fm)(t)        
    
    def execute(self):
        t = np.linspace(-np.pi, np.pi, num=10, dtype=np.float)
        xt = np.cos(2*t)
        plt.clf()
        plt.plot(t, xt)
        plt.xlabel('t')
        plt.ylabel('$x(t) = cos(2*t)$')
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.savefig(self.figure_filename('cos2tcoarse'), format='png')

        t = np.linspace(-np.pi, np.pi, num=1000, dtype=np.float)
        plt.clf()
        plt.plot(t, np.cos(2*t))
        plt.xlabel('t')
        plt.ylabel('cos(2*t)')
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.savefig(self.figure_filename('cos2t'), format='png')

        n = np.arange(-10, 10 + 1, 1)
        plt.clf()
        plt.stem(n, np.cos(2 * np.pi * n / 10), use_line_collection=True)
        plt.xlabel('n')
        plt.ylabel('cos(2 * pi * n / 10)') 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.savefig(self.figure_filename('cosdisc'), format='png')
  
        plt.clf()
        plt.subplot(2,1,1)
        plt.plot(t, np.exp(t/4 + 1/3))
        plt.title('1: exp(t/4 + 1/3) - 2: exp(-t/4 + 1/3)')
        plt.axis([-np.pi, np.pi, -0.2, 3])
        plt.subplot(2,1,2)
        plt.plot(t, np.exp(-t/4 + 1/3))
        plt.axis([-np.pi, np.pi, -0.2, 3])
        plt.savefig(self.figure_filename('contvart'), format='png')

        plt.clf()
        plt.subplot(2,1,1) 
        plt.plot(t, np.cos(15*t))   
        plt.title('$y_{1}(t) = cos(15*t)$ | $y_{2}(t) = cos(15*t+1)$')   
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.subplot(2,1,2) 
        plt.plot(t, np.cos(15*t+1))
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.savefig(self.figure_filename('contfase-1'), format='png')

        plt.clf()
        plt.subplot(2,1,1) 
        plt.plot(t, np.cos(15*t))   
        plt.title('1: cos(15*t) - 2: cos(15*t-1)')   
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.subplot(2,1,2) 
        plt.plot(t, np.cos(15*t-1)) 
        plt.axis([-np.pi, np.pi, -1.2, 1.2])
        plt.savefig(self.figure_filename('contfase-2'), format='png')
        
        plt.clf()
        plt.subplot(3,1,1) 
        plt.plot(t, np.cos(20*t)) 
        plt.title('1: cos(20*t) - 2: cos(15*t) - 3: cos(10*t)') 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.subplot(3,1,2) 
        plt.plot(t, np.cos(15*t)) 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.subplot(3,1,3) 
        plt.plot(t, np.cos(10*t)) 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.savefig(self.figure_filename('contfrec'), format='png')
        
        plt.clf()
        plt.subplot(3,1,1)
        plt.stem(n, np.exp(n/10), use_line_collection=True) 
        plt.title('1: exp(n/10) - 2: exp(1/20 * n + 1/3) - 3: exp(-1/20 * n + 1/3)') 
        plt.axis([-10, 10, -0.2, 3])
        plt.subplot(3,1,2) 
        plt.stem(n, np.exp(1/20 * n + 1/3), use_line_collection=True) 
        plt.axis([-10, 10, -0.2, 3]) 
        plt.subplot(3,1,3) 
        plt.stem(n, np.exp(-1/20 * n + 1/3), use_line_collection=True) 
        plt.axis([-10, 10, -0.2, 3])
        plt.savefig(self.figure_filename('discvart'), format='png')
        
        plt.clf()
        plt.subplot(3,1,1) 
        plt.stem(n, np.cos(15*n), use_line_collection=True)   
        plt.title('1: cos(15*n) - 2: cos(15*n+2) - 3: cos(15*n-2)')   
        plt.axis([-10, 10, -1.2, 1.2]) 
        plt.subplot(3,1,2) 
        plt.stem(n, np.cos(15*n+2), use_line_collection=True) 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.subplot(3,1,3) 
        plt.stem(n, np.cos(15*n-2), use_line_collection=True) 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.savefig(self.figure_filename('discfase'), format='png')
        
        plt.clf()
        plt.subplot(3,1,1) 
        plt.stem(n, np.cos(20*n), use_line_collection=True) 
        plt.title('1: cos(20*n) - 2: cos(15*n) - 3: cos(10*n)') 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.subplot(3,1,2) 
        plt.stem(n, np.cos(15*n), use_line_collection=True) 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.subplot(3,1,3) 
        plt.stem(n, np.cos(10*n), use_line_collection=True) 
        plt.axis([-10, 10, -1.2, 1.2])
        plt.savefig(self.figure_filename('discfrec'), format='png')
        
        plt.clf() 
        plt.plot(t, np.cos(t)) 
        plt.title('función par') 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.savefig(self.figure_filename('contpar'), format='png')
        
        plt.clf() 
        plt.plot(t, np.sin(t)) 
        plt.title('función impar') 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.savefig(self.figure_filename('contimpar'), format='png')
        
        plt.clf()
        plt.stem(n, n*n*n/100, use_line_collection=True) 
        plt.title('n^3/100 funcion impar') 
        plt.axis([-10, 10, -10, 10])
        plt.savefig(self.figure_filename('discimpar'), format='png')
        
        plt.clf() 
        plt.stem(n, n*n/10, use_line_collection=True) 
        plt.title('n^2/10 funcion par') 
        plt.axis([-10, 10, -0.2, 10]) 
        plt.savefig(self.figure_filename('discpar'), format='png')
        
        xpt = np.cos(5*t) + np.sin(10*t)
        xnt = np.cos(-5*t) + np.sin(-10*t)
        plt.clf()
        plt.subplot(3,1,1) 
        plt.plot(t, xpt) 
        plt.title('cos(5*t)+sin(10*t)') 
        plt.axis([-np.pi, np.pi, -2.4, 2.4]) 
        plt.subplot(3,1,2) 
        plt.plot(t, (xpt+xnt)/2) 
        plt.title('parte par') 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.subplot(3,1,3) 
        plt.plot(t, (xpt-xnt)/2) 
        plt.title('parte impar') 
        plt.axis([-np.pi, np.pi, -1.2, 1.2]) 
        plt.savefig(self.figure_filename('contparimpar'), format='png')

        xpn = n*n*n/100 + n*n/10
        xnn = (-n)*(-n)*(-n)/100 + (-n)*(-n)/10
        plt.clf()
        plt.subplot(3,1,1)
        plt.stem(n, xpn, use_line_collection=True) 
        plt.title('n^3/100+n^2/10') 
        plt.axis([-10, 10, -20, 20])
        plt.subplot(3,1,2) 
        plt.stem(n, (xpn+xnn)/2, use_line_collection=True) 
        plt.title('parte par') 
        plt.axis([-10, 10, -10, 10])
        plt.subplot(3,1,3) 
        plt.stem(n, (xpn-xnn)/2, use_line_collection=True) 
        plt.title('parte impar') 
        plt.axis([-10, 10, -10, 10])
        plt.savefig(self.figure_filename('discparimpar'), format='png')
        
        xn = np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
        yn = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        plt.clf() 
        plt.stem(n,xn, use_line_collection=True) 
        plt.title('Impulso unitario') 
        plt.axis([-10, 10, -0.2, 1.2])
        plt.savefig(self.figure_filename('impunidisc'), format='png')
        plt.clf() 
        plt.stem(n,yn, use_line_collection=True) 
        plt.title('Escalon unitario') 
        plt.axis([-10, 10, -0.2, 1.2])
        plt.savefig(self.figure_filename('escunidisc'), format='png')
        plt.clf() 
        plt.stem(n+2,xn, use_line_collection=True) 
        plt.title('Impulso unitario desplazado') 
        plt.axis([-10, 10, -0.2, 1.2]) 
        plt.savefig(self.figure_filename('impunidiscdesp'), format='png')
        plt.clf() 
        plt.stem(n+2,yn, use_line_collection=True) 
        plt.title('Escalon unitario desplazado') 
        plt.axis([-10, 10, -0.2, 1.2]) 
        plt.savefig(self.figure_filename('escunidiscdesp'), format='png')
        plt.clf()
        plt.stem(n+2,-xn, use_line_collection=True) 
        plt.title('Impulso unitario desplazado multiplicado por una constante') 
        plt.axis([-10, 10, -1.2, 1.2]) 
        
        plt.savefig(self.figure_filename('impunidiscdespmult'), format='png')
        plt.clf()
        plt.stem(n+2,yn, use_line_collection=True) 
        plt.title('Escalón unitario desplazado multiplicado por una constante') 
        plt.axis([-10, 10, -1.2, 1.2]) 
        plt.savefig(self.figure_filename('escunidiscdespmult'), format='png')
        
        data = scipy.io.loadmat('diversa.mat')
        continua = data['continua']
        logica = data['logica']
        
        plt.clf() 
        # t = np.arange(15)
        # z = np.zeros_like(t)
        plt.subplot(1,2,1) 
        plt.plot(logica[:,0], logica[:,1])
        plt.title('Representación lógica') 
        plt.axis([0,15,-0.4, 1.4])
        plt.subplot(1,2,2) 
        plt.plot(continua[:,0], continua[:,1])
        plt.title('Representación continua') 
        plt.axis([0,15,-0.4, 1.4])
        plt.savefig(self.figure_filename('diversa'), format='png')
        
        t = np.linspace(0, 50, 5000)
        xt = np.cos(2 * np.pi/10 * t)
        plt.clf() 
        plt.plot(t, xt)
        plt.axis([0, 50, -1.2, 1.2]) 
        plt.xlabel('t')
        plt.ylabel('cos(2 * pi * t / 10)')
        plt.title('Función periódica x(t) = np.cos(2 * pi * t / 10)')
        plt.savefig(self.figure_filename('percont'), format='png')
         
        n = np.arange(50, dtype=np.int)
        xn = np.cos(2 * np.pi/10 * n)
        plt.clf() 
        plt.stem(n, xn) 
        plt.axis([0.0, 50.0, -1.2, 1.2]) 
        plt.xlabel('n') 
        plt.ylabel('cos(2 * pi * n / 10)')
        plt.title('Función periódica x[n] = np.cos[2 * pi * n / 10]')
        plt.savefig(self.figure_filename('perdisc'), format='png')
        
        xdn = np.cos(7/11 * n)
        xcn = np.cos(7/11 * t)
        z = np.zeros_like(t)
        plt.clf() 
        plt.stem(n, xdn) 
        plt.axis([0.0, 50.0, -1.2, 1.2])
        plt.plot(t[1:20:5000], xcn[1:20:5000],'r-', t, z)
        plt.xlabel('n') 
        plt.ylabel('cos(7 * n / 10)')
        plt.title('Función discreta no periódica de envolvente continua periódica')
        plt.savefig(self.figure_filename('noperdisc'), format='png')
        
        t = np.linspace(-3, 3, 5000)
        f1 = lambda v: 0.5 if (0.0 <= v < 2.0) else 0.0
        y1 = np.vectorize(f1)(t)
        f2 = lambda v: 1.0 if (0.0 <= v < 1.0) else 0.0
        y2 = np.vectorize(f2)(t)
        f3 = lambda v: 2.0 if (0.0 <= v < 0.5) else 0.0
        y3 = np.vectorize(f3)(t)        
        plt.clf()
        plt.plot(t, y1, 'r', t, y2, 'b', t, y3, 'g')
        plt.axis([-3.0, 3.0, -0.5, 4.5])
        plt.savefig(self.figure_filename('sucimpcont'), format='png')
    

        ut1 = self.get_ut(t, 0.1)
        ut5 = self.get_ut(t, 0.5)        
        ut10 = self.get_ut(t, 1.0)
        ut15 = self.get_ut(t, 1.5)
        ut20 = self.get_ut(t, 2.0)
        plt.clf()
        plt.subplot(4,1,1) 
        plt.plot(t,ut1)
        plt.axis([-3, 3, -0.5, 1.5])
        plt.subplot(4,1,2)
        plt.plot(t, ut5)
        plt.axis([-3, 3, -0.5, 1.5])
        plt.subplot(4,1,3)
        plt.plot(t, ut10)
        plt.axis([-3, 3, -0.5, 1.5])
        plt.subplot(4,1,4)
        plt.plot(t, ut15)
        plt.axis([-3, 3, -0.5, 1.5])
        plt.savefig(self.figure_filename('sucesccont'), format='png')
        
        # 
        # t11 = [-3:0.1:0]
        # x11 = zeros(size(t11))
        # x12 = [0:0.1:1]
        # t12 = zeros(size(x12))
        # t22 = [0:0.1:3]
        # x22 = ones(size(t22))
        # plt.clf()
        # plt.plot(t11,x11,'k',t12,x12,'k',t22,x22,'k') plt.axis([-3, 3, -0.5, 1.5]) title('u(t)')
        # plt.savefig(self.figure_filename('limesccont'), format='png')
        # 
        # t = -2:0.001:4
        # y = (t >= 0) & (t <= 2)
        # z = zeros(size(t))
        # plt.clf()
        # plt.plot(t, z, '-', t, y) plt.axis([-2, 4, -0.5, 1.5]) title('u(t) - u(t-2)') 
        # plt.savefig(self.figure_filename('compesccont'), format='png')
        # 
        # n = [-2:1:4]
        # x = ((n >= 0) & (n < 2)) * 1.0
        # plt.clf()
        # stem(n,x) 
        # plt.axis([-2, 4, -0.5, 1.5]) 
        # title('u[n] - u[n-2]')
        # plt.savefig(self.figure_filename('compescdisc'), format='png')
        # 
        # t = [-2:0.1:8]
        # x = t .* ((t >= 0) & (t <= 2)) + (6 - t) .* ((t >= 4) & (t <= 6))
        # z = zeros(size(t))
        # plt.clf()
        # plt.plot(t,x,t,z) plt.axis([-2,8,-0.5,2.5])
        # plt.savefig(self.figure_filename('compcontuno'), format='png')
        # 
        # n = [-2:1:8]
        # x = (n .* n) .* ((n >= 0) & (n < 2)) - (n/4) .* ((n >= 4) & (n < 6))
        # plt.clf()
        # stem(n,x) plt.axis([-2,8,-1.5,1.5])
        # plt.savefig(self.figure_filename('compcontdos'), format='png')
        # 
        # t = [-2:0.01:10]
        # x1 = ((t >= 0) & (t < 2)) * 1.0
        # x2 = (-((t >= 2) & (t < 4))) * 1.0
        # x3 = ((t >= 4) & (t < 6)) * 1.0
        # x4 = (-((t >= 6) & (t < 8))) * 1.0
        # x = x1 + x2 + x3 + x4
        # y = t .* x1 + (t - 4) .* x2 + (t - 4) .* x3 + (t - 8) .* x4
        # plt.clf() 
        # plt.subplot(1,2,1) plt.plot(t, x) plt.axis([-2,10,-1.5,1.5]) 
        # plt.subplot(1,2,2) plt.plot(t, y) plt.axis([-2,10,-0.5,2.5]) 
        # plt.savefig(self.figure_filename('comppreguno'), format='png')
        # 
        # n = [-2:1:10]
        # x1 = ((n >= 0) & (n < 2)) * 1.0
        # x2 = (-((n >= 2) & (n < 4))) * 1.0
        # x3 = ((n >= 4) & (n < 6)) * 1.0
        # x4 = (-((n >= 6) & (n < 8))) * 1.0
        # x = x1 + x2 + x3 + x4
        # y = n .* x1 + (n - 4) .* x2 + (n - 4) .* x3 + (n - 8) .* x4
        # plt.clf() 
        # plt.subplot(1,2,1) stem(n, x) plt.axis([-2,10,-1.5,1.5]) 
        # plt.subplot(1,2,2) stem(n, y) plt.axis([-2,10,-0.5,2.5]) 
        # plt.savefig(self.figure_filename('comppregdos'), format='png')
        # 
        # 
        # x1 = zeros(size(n))
        # x2 = x1
        # x1(3) = 1
        # x2(5) = 2
        # plt.subplot(2,1,1) stem(n, x2) title('Impulso desplazado multiplicado') 
        # plt.subplot(2,1,2) stem(n, x1) title('Impulso unitario')
        # plt.savefig(self.figure_filename('lecture2'), format='png')
        # 
        # 

        n  = np.array([-7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0,   1.0,  2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        x  = np.array([ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,   2.0, -2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        h  = np.array([ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[0] = \sum_{k=-\infty}^\infty x[k] \, h[0-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp01-01'), format='png')

        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[1] = \sum_{k=-\infty}^\infty x[k] \, h[1-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(1-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[1-k]')
        plt.tight_layout()
        
        plt.savefig(self.figure_filename('convejemp01-02'), format='png')

        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[2] = \sum_{k=-\infty}^\infty x[k] \, h[2-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(2-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[2-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp01-03'), format='png')

        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[3] = \sum_{k=-\infty}^\infty x[k] \, h[3-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(3-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[3-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp01-04'), format='png')

        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[4] = \sum_{k=-\infty}^\infty x[k] \, h[4-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(4-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[4-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp01-05'), format='png')
        
        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[5] = \sum_{k=-\infty}^\infty x[k] \, h[5-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(5-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[5-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp01-06'), format='png')



        q = 99.0 / 100.0
        n  = np.array([-7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0,  1.0,  2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        x = np.array([0.0 if np.sign(v) < 0.0 else q**v for v in n])
        h  = np.array([ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  1.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
        plt.clf()
        plt.subplot(4,1,1)
        plt.title(r"Convolución  "
                  r"$y[2] = \sum_{k=-\infty}^\infty x[k] \, h[2-k]$",
                  fontsize=16, color='black')
        plt.subplots_adjust(top=1.0)
        plt.stem(n, x, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('x[k]')
        plt.subplot(4,1,2) 
        plt.stem(n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[k]')
        plt.subplot(4,1,3) 
        plt.stem(2-n, h, use_line_collection=True) 
        plt.axis([-3, 3, -3, 3])
        plt.xlabel('k')
        plt.ylabel('h[2-k]')
        plt.tight_layout()
        plt.savefig(self.figure_filename('convejemp02-01'), format='png')
        
        plt.close("all")
