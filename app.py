from flask import request, jsonify, url_for
from app_factory import init_app, db
from models import Escola

app = init_app()


@app.route("/escolas")
def listar_escolas():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=100, type=int)

    paginacao = Escola.query.order_by(Escola.nome_escola).paginate(page=page, per_page=per_page, error_out=False)

    

    escolas = []

    for escola in paginacao.items:
        escolas.append({
              "codigo_inep": escola.codigo_inep,
            "nome_escola": escola.nome_escola,
            "ano_censo": escola.ano_censo,
            "matriculas": escola.matriculas,
            "internet": escola.internet,
            "cidade": escola.cidade.nome if escola.cidade else None,
            "estado": escola.cidade.estado.uf if escola.cidade else None,
            "prestadora": escola.prestadora.nome if escola.prestadora else None  
        })

    next_url = url_for('listar_escolas', page=paginacao.next_num, per_page=per_page) if paginacao.has_next else None
    prev_url = url_for('listar_escolas', page=paginacao.prev_num, per_page=per_page) if paginacao.has_prev else None
    
    # escolas = Escola.query.limit(100).all()
    return jsonify({
        'page': page,
        'per_page': per_page,
        'total': paginacao.total,
        'pages': paginacao.pages,
        'escolas': escolas,
        'next':next_url,
        'prev':prev_url
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
