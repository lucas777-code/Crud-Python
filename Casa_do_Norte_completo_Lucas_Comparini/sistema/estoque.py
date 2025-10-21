from tkinter import ttk, messagebox
from db import getconnection

def showgestaoestoque(app):
    for w in app.winfo_children():
        w.destroy()
    frame = ttk.Frame(app, padding=10)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Gestão de Estoque", font=("TkDefaultFont", 16)).pack()
    cols = ("nome", "quantidade", "estoque_minimo")
    tree = ttk.Treeview(frame, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c.title())
    tree.pack(fill="both", expand=True, pady=10)
    def carregar():
        for i in tree.get_children():
            tree.delete(i)
        with getconnection() as conn:
            for r in conn.execute("SELECT nome, quantidade, estoque_minimo FROM comidas ORDER BY nome ASC"):
                tree.insert("", "end", values=(r["nome"], r["quantidade"], r["estoque_minimo"]))
    carregar()
