import sqlite3

# Conecta ao banco de dados 'users.db'
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Cria a tabela 'users' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song integer,
    FOREIGN KEY (favorite_song) REFERENCES musics(id)
        )
    ''')
connection.commit()

# Função para criar um utilizador na tabela 'users'
def create_user(username, age, favorite_song):
    cursor.execute('INSERT INTO users (username, age, favorite_song) VALUES (?, ?, ?)', (username, age, favorite_song))
    connection.commit()

# Função para encontrar um utilizador na tabela 'users'
def find_user(username):
    cursor.execute('SELECT * from users WHERE username = ?', username)
    connection.commit()
    return cursor.fetchall()

# Função para remover um utilizador da tabela 'users' com base no username
def delete_user(username):
    cursor.execute('DELETE FROM users WHERE username = ?', username)
    connection.commit()

# Função para obter todos os utilizadores da tabela 'users'
def get_all_users():
    cursor.execute('SELECT * FROM users')
    connection.commit()
    return cursor.fetchall()

# Exclui a tabela 'users'
cursor.execute('DROP TABLE users')
connection.commit()

# Fecha a conexão com o banco de dados
connection.close()