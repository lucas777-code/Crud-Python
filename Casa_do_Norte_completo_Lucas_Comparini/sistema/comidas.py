from tkinter import ttk, messagebox
from db import getconnection
from utils import gerarcodigo

def showcomidas(app):
    for w in app.winfo_children():
        w.destroy()
    frame = ttk.Frame(app, padding=10)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Cadastro de Comidas", font=("TkDefaultFont", 16)).pack()
    cols = ("id", "codigo", "nome", "categoria", "quantidade", "estoque_minimo")
    tree = ttk.Treeview(frame, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c.title())
    tree.pack(fill="both", expand=True, pady=10)

    def carregar():
        for i in tree.get_children():
            tree.delete(i)
        with getconnection() as conn:
            for r in conn.execute("SELECT * FROM comidas"):
                tree.insert("", "end", values=(r["id"], r["codigo"], r["nome"], r["categoria"], r["quantidade"], r["estoque_minimo"]))
    carregar()
