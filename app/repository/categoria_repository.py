from app.database.connection import get_db
from app.models.categoria_model import CategoriaModel

class CategoriaRepository:
    def get_all_categorias(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias")
        rows = cursor.fetchall()
        return [
            CategoriaModel(id=row[0], nome=row[1], descricao=row[2]) for row in rows
        ]
        
    def get_categoria_by_id(self, categoria_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias WHERE id = ?", (categoria_id,))
        row = cursor.fetchone()
        if row:
            return CategoriaModel(id=row[0], nome=row[1], descricao=row[2])
        return None
    
    def create_categoria(self, categoria):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO categorias (nome, descricao) VALUES (?, ?)",
            (categoria.get_nome(), categoria.get_descricao())
        )
        connection.commit()
    
    def update_categoria(self, categoria):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE categorias SET nome = ?, descricao = ? WHERE id = ?",
            (categoria.get_nome(), categoria.get_descricao(), categoria.get_id())
        )
        connection.commit()
        
    def delete_categoria(self, categoria_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
        connection.commit()
        