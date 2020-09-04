import sqlite3


def listarcontatos():
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contatos')
    return c.fetchall()


def listarcontatospelonome(nome):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM contatos WHERE nome=?', nome)
    return c.fetchone()


def listarcontatospeloid(id):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM contatos WHERE id=?', id)
    return c.fetchone()


def novocontato(contato):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contatos (id integer primary key autoincrement, nome text not null, endereco '
              'text, numero text not null, email text)')
    c.executemany('INSERT INTO contatos (nome, endereco, numero, email) VALUES (?, ?, ?, ?)', contato)
    conn.commit()
    conn.close()


def alterarcontato(contato):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute('UPDATE contatos SET nome=?, endereco=?, numero=?, email=? WHERE id = ?', contato)
    conn.commit()
    conn.close()


def removercontato(id):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute('DELETE FROM contatos WHERE id = ?', id)
    conn.commit()
    conn.close()
