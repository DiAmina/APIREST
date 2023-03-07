import sqlite3

def ajouter_entite_bd(id,label):
    try:
        conn = sqlite3.connect('entite.db')
        conn.execute(f"INSERT INTO ENTITE (ID, LABEL) VALUES ({id},'{label}')")
        conn.commit()
        return True
    except:
        return False

def obtenir_entite_bd(id):
    conn = sqlite3.connect('entite.db')
    cursor = conn.execute(f"SELECT ID,LABEL from ENTITE WHERE ID = {id}");
    entite = None
    for row in cursor:
        entite = {
            'id': row[0],
            'libellé_entité': row[1]
         }
        break
    return entite

def supprimer_entite_bd(id):
    try:
        conn = sqlite3.connect('entite.db')
        conn.execute(f"DELETE from ENTITE where ID={id};")
        conn.commit()
        return True
    except:
        return False

def mettre_a_jour_db(id,label):
    try:
        conn = sqlite3.connect('entite.db')
        conn.execute(f"UPDATE  ENTITE set LABEL = '{label}' where ID = {id}")
        conn.commit()
        return True
    except:
        return False

def obtenir_toutes_entite_bd():
    conn = sqlite3.connect('entite.db')
    cursor = conn.execute("SELECT ID, LABEL from ENTITE")
    entities = []
    for row in cursor:
        entities.append({
            'id': row[0],
            'libellé_entité': row[1]
        }
        )
    return entities
