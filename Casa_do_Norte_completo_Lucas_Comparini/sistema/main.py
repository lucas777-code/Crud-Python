import tkinter as tk
from tkinter import ttk
from login import showlogin
from utils import centralizarjanela
from db import ensuredb
from comidas import showcomidas
from estoque import showgestaoestoque

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque: Comidas Nordestinas")
        ensuredb()
        self.currentuser = None
        centralizarjanela(self, 400, 250)
        showlogin(self)

    def showmain(self):
        for w in self.winfo_children():
            w.destroy()
        centralizarjanela(self, 1000, 550)
        top = ttk.Frame(self, padding=2)
        top.pack(fill="x")
        ttk.Label(top, text=f" Usuário logado: {self.currentuser.get('nome_completo','')}").pack(side="left")
        ttk.Button(top, text="Sair", command=lambda: showlogin(self)).pack(side="right")
        ttk.Button(top, text="Cadastro de Comidas", command=lambda: showcomidas(self)).pack(side="right", padx=6)
        ttk.Button(top, text="Gestão de Estoque", command=lambda: showgestaoestoque(self)).pack(side="right", padx=6)
        center = ttk.Frame(self, padding=40)
        center.pack(expand=True)
        msg = f"Olá, {self.currentuser.get('nome_completo','')}!\nBem-vindo ao sistema de controle de estoque.\nEscolha uma opção acima."
        tk.Label(center, text=msg, font=("TkDefaultFont", 18), justify="left").pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
