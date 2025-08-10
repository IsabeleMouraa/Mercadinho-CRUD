# 🛒 Mercado EliteGoldVm

Um sistema web simples e estiloso para gerenciamento de **produtos** e **categorias**, desenvolvido em **Python + Flask**, com **SQLite** como banco de dados.  

---

## 📌 Funcionalidades

- Criar, listar, editar e excluir **categorias** e **produtos**.
- Relacionamento **1:N** → uma categoria pode ter vários produtos.
- **Proteção contra exclusão de categorias com produtos associados** — só é possível deletar categorias vazias.
- Exibição de **descrição da categoria** ao passar o mouse sobre o nome dela na listagem de produtos.

##  Executando o projeto

### Clone o repositório
```bash
git clone https://github.com/IsabeleMouraa/Mercadinho-CRUD.git
cd Mercadinho-CRUD
```

### Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate
```

### Instalar o pip e o Flask
```bash
pip install --upgrade pip
pip install Flask
```

### Execute o servidor
```bash
python run.py
```