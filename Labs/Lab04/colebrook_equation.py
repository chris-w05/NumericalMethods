import numpy as np

def colebrook_equation(f, e, D, Re):
    #in form f(x) = 0
    return (1 / np.sqrt(f)) + 2 * np.log10((e / D) / 3.7 + 2.51 / (Re * np.sqrt(f)))
