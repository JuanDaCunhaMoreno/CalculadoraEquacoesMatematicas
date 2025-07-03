import sympy
from sympy import symbols, Eq, solve
import tkinter as tk
from tkinter import messagebox

def ResolverEquacao():
    try:
        #Pegar do input
        equacao_str = entrada_equacao.get()
        x = symbols('x')
        #Convertendo str para expressão sympy
        #Exemplo esperado: "2*x + 3 = 0" ou "x**2 - 5*x + 6 = 0"
        lados = equacao_str.split('=')
        if len(lados) != 2:
            raise ValueError("Equação deve conter um '=' separando os lados.")
        #Verifica se a equação está formulada corretamente
        lado_esq = sympy.sympify(lados[0])
        lado_dir = sympy.sympify(lados[1])
        #Converte as string para expressões simbólicas
        equacao = Eq(lado_esq, lado_dir)
        #Resolve a equação
        solucoes = solve(equacao, x)

        resultado_texto = "Soluções: \n" + "\n".join(str(s)for s in solucoes)
        texto_resultado.config(state='normal')
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, resultado_texto)
        texto_resultado.config(state='disabled')
    except Exception as e:
        messagebox.showerror("ERRO", f"Erro ao resolver equação:\n{e}")


#Configuração janela
janela = tk.Tk()
janela.title("Calculadora de Equações Matemáticas")

label = tk.Label(janela, text="Digite a equação (ex: 2*x + 3 = 0 ou x**2 - 5*x + 6 = 0):")
label.pack(padx=10, pady=5)
#Input
entrada_equacao = tk.Entry(janela, width=40)
entrada_equacao.pack(padx=10, pady=5)
#Botão para resolver
botao_resolver = tk.Button(janela, text="Resolver", command=ResolverEquacao)
botao_resolver.pack(padx=10, pady=5)
#Área para mostrar o resultado
texto_resultado = tk.Text(janela, height=6, width=40, state='disabled')
texto_resultado.pack(padx=10, pady=5)
#Inicar interface
janela.mainloop()
