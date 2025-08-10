from app.database.connection import get_db
from app.models.produto_model import ProdutoModel

class ProdutoRepository:
    
    def get_all_produtos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT p.id, p.nome, p.preco, p.quantidade, p.categoria_id, c.nome, c.descricao
                       FROM produtos p
                       JOIN categorias c ON p.categoria_id = c.id """)
        rows = cursor.fetchall()
        produtos = []
        for row in rows:
            produto = ProdutoModel(
                id=row[0],
                nome=row[1],
                preco=row[2],
                quantidade=row[3],
                categoria_id=row[4]
            )
            produto.categoria_nome = row[5]
            produto.categoria_descricao = row[6]
            produtos.append(produto)
        return produtos
    
    
    def get_produto_by_id(self, produto_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT p.id, p.nome, p.preco, p.quantidade, p.categoria_id, c.nome
                       FROM produtos p
                       JOIN categorias c ON p.categoria_id = c.id
                       WHERE p.id = ?""", (produto_id,))
        row = cursor.fetchone()
        if row:
            produto = ProdutoModel(
                id=row[0],
                nome=row[1],
                preco=row[2],
                quantidade=row[3],
                categoria_id=row[4]
            )
            produto.categoria_nome = row[5]
            return produto
        
        
    def create_produto(self, produto):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       INSERT INTO produtos (nome, preco, quantidade, categoria_id)
                       VALUES (?, ?, ?, ?)""",
                       (produto.get_nome(), produto.get_preco(), produto.get_quantidade(), produto.get_categoria_id()))
        connection.commit()
        
    def update_produto(self, produto):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE produtos
                       SET nome = ?, preco = ?, quantidade = ?, categoria_id = ?
                       WHERE id = ?""",
                       (produto.get_nome(), produto.get_preco(), produto.get_quantidade(), produto.get_categoria_id(), produto.get_id()))
        connection.commit()
        
    def delete_produto(self, produto_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        connection.commit()
        
    def get_produtos_by_categoria_id(self, categoria_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SElECT * FROM produtos WHERE categoria_id = ?", (categoria_id,))
        return cursor.fetchall()