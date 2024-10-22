from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from contextlib import contextmanager

#URL de conexão par BD MySQL

#Parametros de Conexão com MySQL.

db_user="julio"
db_password="julio"
db_host="localhost"
db_port="3306"
db_name="meu_banco"
#DATABASE_URL=f"mysql + pmysql://usuario:senha@host:porta/nome_bd"

DATABASE_URL=f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db=create_engine(DATABASE_URL)
Session=sessionmaker(bind=db)
session=Session()

@contextmanager
def get_db():
    db=Session() #Cria uma sessão para ações no banco de dados.

    try:
        yield db #Caso a sessão realize todas as tarefas, salva a operação 
        db.commit()
    except Exception as erro:
        db.rollback()#Desfaz todas as alterações em caso de erro em alguma operação
        raise erro #Lança uma exception 
    finally:
        db.close()#Fecha conexão com o banco de dados
