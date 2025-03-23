import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class Espectrofotometro:
    def __init__(self, operador, data):
        self.operador = operador
        self.data = data

    def __str__(self):
        return f"Operador: {self.operador}\nData: {self.data}"

    @staticmethod
    def funcao_linear(x,a,b):
        return a*x + b

    def curva_de_calibracao(self):
        pares_concentracao_abs = []

        while True:
            try:
                concentracao = float(input("Digite a concentração da solução (mg/L): "))
                absorbancia = float(input("Digite a absorbância lida: "))
            except EOFError:
                break
            else:
                pares_concentracao_abs.append({concentracao:absorbancia})
        
        x_data = []
        y_data = []

        for dados in pares_concentracao_abs:
            for conc in dados:
                x_data.append(conc)    
                y_data.append(dados[conc]) 

        concentracoes = np.array(x_data)
        absorbancias = np.array(y_data)      

        parametro_reta, pcov = curve_fit(Espectrofotometro.funcao_linear, concentracoes, absorbancias)
        self.a_, self.b_ = parametro_reta

        plt.plot(concentracoes, Espectrofotometro.funcao_linear(concentracoes, self.a_, self.b_))
        plt.xlabel("Concentração (mg/L)")
        plt.ylabel("Absorbância")
        plt.show()

        return self.a_, self.b_

    def concentracao(self):
        abs = float(input("Digite a absorbância medida: "))

        try:
            self.concentracao_calculada = abs/self.a_ - self.b_
        except AttributeError:
            return "Não há uma curva de calibração registrada"
        else:
            return f"Concentração: {self.concentracao_calculada} mg/L"

def main():
    espectrofotometro = Espectrofotometro("for_code", "17/03/2021")
    print(espectrofotometro)
    espectrofotometro.curva_de_calibracao()
    print(espectrofotometro.concentracao())


if __name__ == "__main__":
    main()
