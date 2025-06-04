from database import init_app, db
from models import Cidade, Estado, Prestadora
import csv
import os
 
app = init_app()
 
def preenche_estatico():

    with app.app_context():
        if Cidade.query.count() > 0:
            print("Tabela 'cidade' já populada. Pulando carga.")
            return
        
        
        pasta_csv = "arquivos_csv"
        arquivos = [arq for arq in os.listdir(pasta_csv) if arq.endswith(".csv")]

        for nome_arquivo in arquivos:
            caminho = os.path.join(pasta_csv, nome_arquivo)
            print(f"Processando: {caminho}")

            with open(caminho, newline='', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    #uf = row["UF"] 
                    estado = Estado.query.filter_by(uf=row["UF"]).first()
                    if not estado:
                        #print(uf)
                        estado = Estado(uf=row["UF"])
                        db.session.add(estado)
                        db.session.flush()
                    
                    cidade = Cidade.query.filter_by(nome=row['Município']).first()
                    if not cidade:
                        cidade = Cidade(nome=row['Município'], estado=estado)
                        db.session.add(cidade)

                    
                    prestadora = Prestadora.query.filter_by(nome=row['Prestadora PBLE-CER']).first()
                    if not prestadora:
                        prestadora = Prestadora(nome=row['Prestadora PBLE-CER'])
                        db.session.add(prestadora)
                        
        db.session.commit()

if __name__ == "__main__":
    preenche_estatico()    