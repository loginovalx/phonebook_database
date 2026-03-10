import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="phonebook",
        user="user",       
        password="qwert1234", 
        host="db",     
        port="5432"
    )

def add_contact(first_name, last_name, phone, note):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, phone, note) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, phone, note)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_all_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, phone, note FROM contacts ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_contact_by_id(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, phone, note FROM contacts WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_contact(id, first_name, last_name, phone, note):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE contacts SET first_name=%s, last_name=%s, phone=%s, note=%s WHERE id=%s",
        (first_name, last_name, phone, note, id)
    )
    updated_row = cur.rowcount #флаг если обновили
    conn.commit()
    cur.close()
    conn.close()
    return updated_row > 0

def delete_contact(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s", (id,))
    updated_row = cur.rowcount #флаг если обновили
    conn.commit()
    cur.close()
    conn.close()
    return updated_row > 0