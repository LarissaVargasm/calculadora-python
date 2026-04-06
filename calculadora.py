import customtkinter as ctk

#parte visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("300x450")
app.title("Calculadora")

#para poder inserir os números
def clicar(num):
    display.insert("end", num)

#função de limpar a tela
def limpar():
    display.delete(0,"end")

#função de calcular os resultados
def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, "end")
        display.insert(0, str(resultado))
    except:
        display.delete(0,"end")
        display.insert(0,"Erro")

#parte de exibição
display = ctk.CTkEntry(app, width=260, height=50, font=("arial", 28), justify="right")
display.pack(padx=20, pady=20)

#organizador dos botões
frame = ctk.CTkFrame(app)
frame.pack()

#botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, k, c) in botoes:
    if texto == '=':
        comando = calcular
    elif texto == 'C':
        comando = limpar
    else:
        comando = lambda t=texto: clicar(t)

    ctk.CTkButton(frame, text=texto, width=60, height=60, command=comando).grid(row=k, column=c, padx=5, pady=5)


app.mainloop()