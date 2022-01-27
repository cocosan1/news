import sqlite3

conn = sqlite3.connect('word.db', check_same_thread=False)
c = conn.cursor()

def select_word():
    c.execute('SELECT * FROM wordstable ORDER BY RANDOM() LIMIT 3')
    data = c.fetchall()
    return data

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS wordstable(word TEXT)')

def add_data(word):
    c.execute('INSERT INTO wordstable(word) VALUES (?)', (word,)) 
    #引数一つの時要カンマ。無いと？が一文字扱いになる。
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM wordstable')
    data = c.fetchall()
    return data

def view_unique_words():
    c.execute('SELECT DISTINCT word FROM wordstable') # DISTINCT 重複行を一つにまとめる。
    data = c.fetchall()
    return data

def get_word(word):
    c.execute('SELECT * FROM wordstable WHERE word="{}"'.format(word))
    # c.execute('SELECT * FROM wordstable WHERE word=?', (word,))
    data = c.fetchall()
    return data

def edit_word_data(new_word, word):
    c.execute('UPDATE wordstable SET word=? WHERE word=?', (new_word, word))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(word):
    c.execute('DELETE FROM wordstable WHERE word=?', (word,))
    conn.commit()


