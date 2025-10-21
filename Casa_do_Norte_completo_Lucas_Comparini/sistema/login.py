import tkinter as tk
from tkinter import ttk, messagebox
from db import getconnection
from utils import centralizarjanela

def showlogin(app):
    for w in app.winfo_children():
        w.destroy()
    centralizarjanela(app, 400, 250)
    frm = ttk.Frame(app, padding=20)
    frm.pack(expand=True)
    ttk.Label(frm, text="Login", font=("TkDefaultFont", 16)).grid(column=0, row=0, columnspan=2, pady=10)
    ttk.Label(frm, text="Usuário").grid(column=0, row=1, sticky="e")
    userent = ttk.Entry(frm, width=25)
    userent.grid(column=1, row=1)
    ttk.Label(frm, text="Senha").grid(column=0, row=2, sticky="e")
    pwdent = ttk.Entry(frm, show="*", width=25)
    pwdent.grid(column=1, row=2)
    def attempt_login():
        username, password = userent.get().strip(), pwdent.get().strip()
        if not username or not password:
            messagebox.showwarning("Falha", "Preencha usuário e senha.")
            return
        with getconnection() as conn:
            cur = conn.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (username, password))
            row = cur.fetchone()
        if row:
            app.currentuser = dict(row)
            app.showmain()
        else:
            messagebox.showerror("Falha", "Usuário ou senha inválidos.")
    ttk.Button(frm, text="Entrar", command=attempt_login).grid(column=0, row=3, columnspan=2, pady=10)
