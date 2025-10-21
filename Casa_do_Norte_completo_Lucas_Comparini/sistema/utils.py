from db import getconnection

def gerarcodigo():
    with getconnection() as conn:
        cur = conn.execute("SELECT id FROM comidas ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        return f"C{(row['id']+1 if row else 1):03d}"

def centralizarjanela(win, w, h):
    ws, hs = win.winfo_screenwidth(), win.winfo_screenheight()
    x, y = (ws//2) - (w//2), (hs//2) - (h//2)
    win.geometry(f"{w}x{h}+{x}+{y}")
