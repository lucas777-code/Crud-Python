import sqlite3, os

DBFILENAME = "comidasdb.sqlite"

def getconnection():
    conn = sqlite3.connect(DBFILENAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def ensuredb():
    if not os.path.exists(DBFILENAME):
        scriptpath = os.path.join(os.path.dirname(__file__), "db_init.sql")
        if os.path.exists(scriptpath):
            with getconnection() as conn, open(scriptpath, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
        else:
            raise FileNotFoundError("db_init.sql não encontrado.")
