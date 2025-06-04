from app_factory import db
from sqlalchemy.orm import relationship

class Estado(db.Model):
    __tablename__ = 'estado'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=True)
    uf = db.Column(db.String(2), nullable=False)
    
    cidades = relationship("Cidade", back_populates="estado")

class Cidade(db.Model):
    __tablename__ = 'cidade'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey("estado.id"), nullable=False)

    estado = relationship("Estado", back_populates="cidades")
    escolas = relationship("Escola", back_populates="cidade")

class Prestadora(db.Model):
    __tablename__ = 'prestadora'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    escolas = relationship("Escola", back_populates="prestadora")

class Escola(db.Model):
    __tablename__ = 'escolas'

    codigo_inep = db.Column(db.String, primary_key=True)
    nome_escola = db.Column(db.String)
    projeto_gape = db.Column(db.String)
    ano_censo = db.Column(db.Integer)
    matriculas = db.Column(db.Integer)
    internet = db.Column(db.String)
    uso_internet_alunos = db.Column(db.String)
    banda_larga = db.Column(db.String)
    laboratorio_informatica = db.Column(db.String)
    velocidade_internet = db.Column(db.String)
    atende_capacidade_minima = db.Column(db.String)
    cobertura_4g = db.Column(db.String)
    localizacao = db.Column(db.String)
    dependencia = db.Column(db.String)
    situacao_funcionamento = db.Column(db.String)
    quantidade_profissionais_educacao = db.Column(db.Integer)
    endereco = db.Column(db.String)
    bairro = db.Column(db.String)
    
    id_cidade = db.Column(db.Integer, db.ForeignKey("cidade.id"))
    id_prestadora = db.Column(db.Integer, db.ForeignKey("prestadora.id"))

    cidade = relationship("Cidade", back_populates="escolas")
    prestadora = relationship("Prestadora", back_populates="escolas")
