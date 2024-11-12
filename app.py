# Parte de importação da biblioteca tkinter
from tkinter import *
from tkinter import ttk
from services import *

# Funções para rodar a interface
def main():
    def adicionar_despesa():
        categoria = categoriaEntry.get()
        valor = float(valorEntry.get())
        adicionar_despesa(categoria, valor)
        
        categoriaEntry.delete(0, END)
        valorEntry.delete(0, END)

    def listar_despesas():
        despesas = listar_despesas()

        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de Despesas')
        janela_listar.geometry('500x300')

        tree = ttk.Treeview(janela_listar, columns=('ID', 'Categoria', 'Valor', 'Data'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Categoria', text='Categoria')
        tree.heading('Valor', text='Valor')
        tree.heading('Data', text='Data')
        tree.pack(fill=BOTH, expand=True)

        for despesa in despesas:
            tree.insert('', END, values=despesa)

        voltar = Button(janela_listar, text='Voltar', width=10, command=janela_listar.destroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)

    def exibir_total_por_categoria():
        totais = calcular_total_por_categoria()
        janela_total = Toplevel(janela)
        janela_total.title('Total por Categoria')
        janela_total.geometry('300x200')

        for categoria, total in totais:
            Label(janela_total, text=f"{categoria}: R${total:.2f}").pack()

    def exibir_gasto_mensal():
        total_mensal = calcular_gasto_mensal()
        Label(janela, text=f"Gasto Mensal Total: R${total_mensal:.2f}").place(x=50, y=250)

    def exibir_media_diaria():
        media_diaria = calcular_media_diaria()
        Label(janela, text=f"Média Diária: R${media_diaria:.2f}").place(x=50, y=280)

# Criação de janela
    janela = Tk()
    janela.colormapwindows()
    janela.geometry('400x350')
    janela.title('Calculadora de Despesas Pessoais')

# Titulo da interface
    titulo = Label(janela, text='Calculadora de Despesas', font=('Arial BLACK', 16))
    titulo.pack(pady=20)

# Colocando os botoes na interface
    Label(janela, text='Categoria:', font=('Comic')).place(x=50, y=80)
    categoriaEntry = Entry(janela, width=30)
    categoriaEntry.place(x=130, y=80)

    Label(janela, text='Valor:', font=('Comic')).place(x=80, y=110)
    valorEntry = Entry(janela, width=30)
    valorEntry.place(x=130, y=110)

    adicionar = Button(janela, text='Adicionar Despesa', width=15, command=adicionar_despesa)
    adicionar.place(x=150, y=140)

    listar = Button(janela, text='Listar Despesas', width=15, command=listar_despesas)
    listar.place(x=150, y=170)

    total_categoria = Button(janela, text='Total por Categoria', width=15, command=exibir_total_por_categoria)
    total_categoria.place(x=150, y=200)

    total_mensal = Button(janela, text='Gasto Mensal', width=15, command=exibir_gasto_mensal)
    total_mensal.place(x=150, y=230)

    media_diaria = Button(janela, text='Média Diária', width=15, command=exibir_media_diaria)
    media_diaria.place(x=150, y=260)

    janela.mainloop()

if __name__ == '__main__':
    main()
