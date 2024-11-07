import sqlite3

conexao = sqlite3.connect('musicas.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS musicas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    year INTEGER,
    album TEXT,
    added_by TEXT
        )
    ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilizadores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song TEXT
        )
    ''')

conexao.commit()

def find_user(username):
    cursor.execute('SELECT * from utilizadores WHERE username = ?', username)
    conexao.commit()
def inserir_livro(titulo, autor, ano):
    cursor.execute('INSERT INTO musicas (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    conexao.commit()

inserir_livro("Don Quixote", "Miguel de Cervantes", 1605)
inserir_livro("Ulysses", "James Joyce", 1908)
inserir_livro("1984", "George Orwell", 1949)


cursor.execute('SELECT * FROM livros')
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

cursor.execute('DROP TABLE livros')
conexao.commit()
conexao.close()