from app import app
from flask import render_template, request, redirect, url_for
from app.models.categoria_model import CategoriaModel
from app.service.categoria_service import CategoriaService
from app.models.produto_model import ProdutoModel
from app.service.produto_service import ProdutoService

categoria_service = CategoriaService()
produto_service = ProdutoService()

@app.route('/')
def index():
    return redirect(url_for('listar_categorias'))

@app.route('/categorias')
def listar_categorias():
    categorias = categoria_service.get_all_categorias()
    return render_template('categorias/listar_categorias.html', categorias=categorias)

@app.route('/categorias/novo', methods=['GET', 'POST'])
def criar_categoria():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        categoria_service.create_categoria(CategoriaModel(id=None, nome=nome, descricao=descricao))
        return redirect(url_for('listar_categorias'))
    return render_template('categorias/criar_categoria.html')

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = categoria_service.get_categoria_by_id(id)
    if request.method == 'POST':
        categoria_service.update_categoria(
            CategoriaModel(
                id,
                request.form['nome'],
                request.form['descricao']
            ))
        return redirect(url_for('listar_categorias'))
    return render_template('categorias/criar_categoria.html', categoria=categoria)

@app.route('/categorias/excluir/<int:id>')
def excluir_categoria(id):
    categoria_service.delete_categoria(id)
    return redirect(url_for('listar_categorias'))

#PRODUTOS

@app.route('/produtos')
def listar_produtos():
    produtos = produto_service.get_all_produtos()
    return render_template('produtos/listar_produtos.html', produtos=produtos)

@app.route('/produtos/novo', methods=['GET', 'POST'])
def criar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        categoria_id = int(request.form['categoria_id'])
        produto = ProdutoModel(
            id=None,
            nome=nome,
            preco=preco,
            quantidade=quantidade,
            categoria_id=categoria_id
        )
        produto_service.create_produto(produto)
        return redirect(url_for('listar_produtos'))
    return render_template('produtos/criar_produto.html', categorias=categoria_service.get_all_categorias())

@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = produto_service.get_produto_by_id(id)
    if request.method == 'POST':
        produto_service.update_produto(
            ProdutoModel(
                id,
                request.form['nome'],
                float(request.form['preco']),
                int(request.form['quantidade']),
                int(request.form['categoria_id'])
            ))
        return redirect(url_for('listar_produtos'))
    return render_template('produtos/criar_produto.html', produto=produto, categorias=categoria_service.get_all_categorias())

@app.route('/produtos/excluir/<int:id>')
def excluir_produto(id):
    produto_service.delete_produto(id)
    return redirect(url_for('listar_produtos'))