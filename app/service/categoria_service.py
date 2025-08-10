from app.repository.categoria_repository import CategoriaRepository 
from app.models.categoria_model import CategoriaModel
from app.repository.produto_repository import ProdutoRepository

class CategoriaService:
    def __init__(self):
        self.categoria_repository = CategoriaRepository()
        self.produto_repository = ProdutoRepository()
        
    def get_all_categorias(self):
        return self.categoria_repository.get_all_categorias()
    
    def get_categoria_by_id(self, categoria_id):
        if categoria_id is None:
            raise ValueError("O ID da categoria não pode ser None.")
        return self.categoria_repository.get_categoria_by_id(categoria_id)
    
    def create_categoria(self, categoria: CategoriaModel):
        if categoria.get_id() is not None:
            raise ValueError("Não é possível criar uma categoria com ID já definido.")
        if not categoria.get_nome() or not categoria.get_descricao():
            raise ValueError("Nome e descrição da categoria são obrigatórios.")
        if len(categoria.get_nome()) < 3:
            raise ValueError("O nome da categoria deve ter pelo menos 3 caracteres.")
        if categoria.get_nome().isdigit():
            raise ValueError("O nome da categoria não pode ser apenas numérico.")
        if categoria.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode ser apenas numérica.")
        if len(categoria.get_descricao()) < 10:
            raise ValueError("A descrição da categoria deve ter pelo menos 10 caracteres.")
        self.categoria_repository.create_categoria(categoria)
        
    def update_categoria(self, categoria: CategoriaModel):
        if categoria.get_id() is None:
            raise ValueError("O ID da categoria não pode ser None.")
        if not categoria.get_nome() or not categoria.get_descricao():
            raise ValueError("Nome e descrição da categoria são obrigatórios.")
        if len(categoria.get_nome()) < 3:
            raise ValueError("O nome da categoria deve ter pelo menos 3 caracteres.")
        if categoria.get_nome().isdigit():
            raise ValueError("O nome da categoria não pode ser apenas numérico.")
        if categoria.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode ser apenas numérica.")
        if len(categoria.get_descricao()) < 10:
            raise ValueError("A descrição da categoria deve ter pelo menos 10 caracteres.")
        self.categoria_repository.update_categoria(categoria)
        
    def delete_categoria(self, categoria_id):
        if categoria_id is None:
            raise ValueError("O ID da categoria não pode ser None.")
        produtos = self.produto_repository.get_all_produtos()
        for produto in produtos:
            if produto.get_categoria_id() == categoria_id:
                raise ValueError("Não é possível excluir uma categoria que possui produtos associados.")
        self.categoria_repository.delete_categoria(categoria_id)
        