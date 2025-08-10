class ProdutoModel:
    def __init__(self, id, nome, preco, quantidade, categoria_id):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__categoria_id = categoria_id
        
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade

    def get_categoria_id(self):
        return self.__categoria_id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_preco(self, preco):
        self.__preco = preco
    
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    def set_categoria_id(self, categoria_id):
        self.__categoria_id = categoria_id