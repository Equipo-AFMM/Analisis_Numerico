import math
import matplotlib.pyplot as plt

class Gaussian():
 """ 
     COMENTARIO:
     
     Clase de distribución gaussiana para calcular y
     visualizar una distribución gaussiana.
    
     Atributos:
         media (flotante) que representa el valor medio de la distribución
         stdev (float) que representa la desviación estándar de la distribución
         data_list (lista de flotadores) una lista de flotadores extraídos del archivo de datos
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []

    
    def calculate_mean(self):
        """
        COMENTARIO:
        
        Función para calcular la media del conjunto de datos.
        
         Args:
             Ninguna
        
         Devoluciones:
             flotante: media del conjunto de datos
    
         """
                    
        avg = 1.0 * sum(self.data) / len(self.data)
        
        self.mean = avg
        
        return self.mean



    def calculate_stdev(self, sample=True):

        """
        COMENTARIO:
        
         Función para calcular la desviación estándar del conjunto de datos.
        
         Args:
             muestra (bool): si los datos representan una muestra o población
        
         Devoluciones:
             flotante: desviación estándar del conjunto de datos
    
         """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.mean
    
        sigma = 0
    
        for d in self.data:
            sigma += (d - mean) ** 2
        
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
        
        return self.stdev
        

    def read_data_file(self, file_name, sample=True):
    
       """
         COMENTARIO:
         
         Función para leer datos de un archivo txt. El archivo txt debería tener
         Un número (flotante) por línea. Los números se almacenan en el atributo de datos.
         Después de leer en el archivo, se calculan la media y la desviación estándar
                
         Args:
             nombre_archivo (cadena): nombre de un archivo para leer
        
         Devoluciones:
             Ninguna
        
         """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
        
    def plot_histogram(self):
        """

         COMENTARIO:
         
         Función para generar un histograma de los datos variables de la instancia utilizando
         Matplotlib Pyplot Library.
        
         Args:
             Ninguna
            
         Devoluciones:
             Ninguna
         """
        plt.hist(self.data)
        plt.title('Histrogama De Datos')
        plt.xlabel('Datos')
        plt.ylabel('Orden')
        
        
        
    def pdf(self, x):
        """
        
        CALCULADORA:
        
        Calculadora de función de densidad de probabilidad para la distribución gaussiana.
        
         Args:
             x (flotante): punto para calcular la función de densidad de probabilidad
            
        
         Devoluciones:
             flotante: salida de función de densidad de probabilidad
         """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
        

    def plot_histogram_pdf(self, n_spaces = 50):

        """
        
        COMENTARIO:
        
        Función para trazar el histograma normalizado de los datos y un gráfico de la
        función de densidad de probabilidad a lo largo del mismo rango
        
         Args:
             n_spaces (int): número de puntos de datos
        
         Devoluciones:
             lista: valores x para el diagrama pdf
             lista: valores y para el diagrama pdf
            
         """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Histrograma Del Espacio Normado')
        axes[0].set_ylabel('Densidad')

        axes[1].plot(x, y)
        axes[1].set_title('Distribución Normal Para \ n Media De Muestra Y Desviación Estándar De Muestra')
        axes[0].set_ylabel('Densidad')
        plt.show()

        return x, y