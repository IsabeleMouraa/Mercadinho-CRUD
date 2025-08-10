from app.repository.produto_repository import ProdutoRepository
from app.models.produto_model import ProdutoModel

class ProdutoService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        
    def get_all_produtos(self):
        return self.produto_repository.get_all_produtos()
    
    def get_produto_by_id(self, produto_id):
        if produto_id is None:
            raise ValueError("O ID do produto não pode ser None.")
        return self.produto_repository.get_produto_by_id(produto_id)
    
    def create_produto(self, produto: ProdutoModel):
        if produto.get_id() is not None:
            raise ValueError("Não é possível criar um produto com ID já definido.")
        if not produto.get_nome() or produto.get_preco() is None or produto.get_quantidade() is None or produto.get_categoria_id() is None:
            raise ValueError("Nome, preço, quantidade e categoria são obrigatórios.")
        if len(produto.get_nome()) < 3:
            raise ValueError("O nome do produto deve ter pelo menos 3 caracteres.")
        if produto.get_nome().isdigit():
            raise ValueError("O nome do produto não pode ser apenas numérico.")
        if produto.get_preco() <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        if produto.get_quantidade() < 0:
            raise ValueError("A quantidade do produto não pode ser negativa.")
        self.produto_repository.create_produto(produto)
        
    def update_produto(self, produto: ProdutoModel):
        if produto.get_id() is None:
            raise ValueError("O ID do produto não pode ser None.")
        if not produto.get_nome() or produto.get_preco() is None or produto.get_quantidade() is None or produto.get_categoria_id() is None:
            raise ValueError("Nome, preço, quantidade e categoria são obrigatórios.")
        if len(produto.get_nome()) < 3:
            raise ValueError("O nome do produto deve ter pelo menos 3 caracteres.")
        if produto.get_nome().isdigit():
            raise ValueError("O nome do produto não pode ser apenas numérico.")
        if produto.get_preco() <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        if produto.get_quantidade() < 0:
            raise ValueError("A quantidade do produto não pode ser negativa.")
        self.produto_repository.update_produto(produto)
        
    def delete_produto(self, produto_id):
        if produto_id is None:
            raise ValueError("O ID do produto não pode ser None.")
        self.produto_repository.delete_produto(produto_id)
        
        