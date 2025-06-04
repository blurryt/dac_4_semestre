import csv
from database import init_app, db
from models import Escola, Cidade, Prestadora
import os

app = init_app()

def carregar_csv():
    with app.app_context():
        if Escola.query.count() > 0:
            print("Tabela 'escolas' já populada. Pulando carga.")
            return
        
        
        pasta_csv = "arquivos_csv"
        arquivos = [arq for arq in os.listdir(pasta_csv) if arq.endswith(".csv")]

        for nome_arquivo in arquivos:
            caminho = os.path.join(pasta_csv, nome_arquivo)
            print(f"Processando: {caminho}")

            with open(caminho, newline='', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    cidade = Cidade.query.filter_by(nome=row['Município']).first()
                    prestadora = Prestadora.query.filter_by(nome=row['Prestadora PBLE-CER']).first()

                    if not cidade or not prestadora:
                        print(f"Erro: Cidade ou Prestadora não encontrada para linha: {row}")
                        continue
                    
                    if Escola.query.filter_by(codigo_inep=row['Código INEP']).first():
                        continue

                    escola = Escola(
                        codigo_inep=row['Código INEP'],
                        nome_escola=row['Nome Escola'],
                        projeto_gape=row['Projeto Gape'],
                        ano_censo=int(row['Ano Censo']),
                        matriculas=int(float(row['Censo Escolar - Matrículas Educação Básica'] + '.0')),
                        internet=row['Internet'],
                        uso_internet_alunos=row['Censo Escolar - Uso Internet Alunos'],
                        banda_larga=row['Censo Escolar - Banda Larga'],
                        laboratorio_informatica=row['Censo Escolar - Laboratório de Informática'],
                        velocidade_internet=row['Velocidade de Acesso PBLE-CER'],
                        atende_capacidade_minima=row['Atende capacidade mínima'],
                        cobertura_4g=row['Anatel - Cobertura 4G'],
                        localizacao=row['Censo Escolar - Localização'],
                        dependencia=row['Censo Escolar - Dependência'],
                        situacao_funcionamento=row['Censo Escolas - Situação Funcionamento'],
                        quantidade_profissionais_educacao=int(float(row['Profissionais da Educação'] + '.0')),
                        endereco=row['DS_ENDERECO'],
                        bairro=row['NO_BAIRRO'],
                        cidade=cidade,
                        prestadora=prestadora
                    )
                    db.session.add(escola)

        db.session.commit()
        print("Escolas carregadas com sucesso.")

if __name__ == "__main__":
    carregar_csv()
