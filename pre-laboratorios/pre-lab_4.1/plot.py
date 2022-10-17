import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_error(series,y_tag,colour='tab:blue',save=False,folder=None,display=True,title=None,y_lim=None):
    """
    Plotea una (o varias) secuencia(s) de errores

    Parametros
    ----------
        errores: numpy.array o list(numpy.array)
            secuencia de valores o lista con varias secuencias de errores
        y_tag: str o list(str)
            etiqueta o etiquetas de los errores a graficar
        colour: str 
            opcional, default 'tab:blue'. color (matplotlib) de las lineas de la series, solo valido cuando se plotea una sola serie
        save: str o bool
            opcional, default False. si es un string entonces guarda la figura con el nombre correspondiente
        
        folder: str
            opcional, default None. directorio en el cual se guarda la figura
        display: bool
            opcional, default True. si se muestran o no las figuras.
    
    """
    sns.set_theme(style="whitegrid")
    _, ax = plt.subplots(figsize=(12,5))
    if isinstance(y_tag,list):
        assert(len(series)==len(y_tag))
        for i in range(len(y_tag)):
            sns.lineplot(data=series[i], ax=ax, markers=['o','o','o'])
        ax.legend(y_tag)
        if title is None:
            title = 'Error versus iteraciones'
        ax.set(xlabel='iteración',ylabel='error',title=title)
    else:
        sns.lineplot(data=series, ax=ax, markers=['o','o','o'], color=colour)
        if title is None:
            title = 'Error {} versus iteraciones'.format(y_tag)
        ax.set(xlabel='iteración',ylabel='error',title=title)
    if y_lim is not None:
        ax.set_ylim((0,y_lim))
    if display:
        plt.show()
    if save:
        path = folder+ '/' + save
        plt.savefig(path)


def plot_samples2d(puntos,tags,linea=None,title=None):
    """
    Plotea puntos de dos distribuciones dos dimensionales
    
    Parametros
    ----------
        puntos: numpy.array
            secuencia de puntos
        tags: numpy.array
            secuencia de clases 0 o 1
        linea: numpy.array
            opcional, default None. pesos y bias que definen linea a plotear
        title: str
            opcional, default None. título del gráfico
    
    """
    if linea is not None:
        xx = np.linspace(-3, 7)
        yy_teorico = (-linea[2]-linea[0]*xx)/linea[1]
        plt.plot(xx, yy_teorico, linestyle='solid',color='red')

    colors = ['tab:blue' if t==0 else 'tab:orange' for t in tags]
    if title is not None:
        plt.title(title)
    plt.scatter(np.array(puntos)[:,0],np.array(puntos)[:,1],color=colors)
    plt.xlim([-4, 7])
    plt.ylim([-6, 9])
    plt.grid()
    plt.xticks(range(-4, 7))
    plt.yticks(range(-6, 9))
    plt.plot();


