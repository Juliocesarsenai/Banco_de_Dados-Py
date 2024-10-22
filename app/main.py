from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session



def main():
    session=Session()
    repository=UsuarioRepository(session)
    service=UsuarioService(repository)

    #Criando um usuario.
    service.criar_usuario("Julio Cesar","juliocesar@gmail.com","123")

    #Listando usuarios
    print("\nListando todoso os usuarios")
    lista_usuarios=service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__=="__main__":
    main() #Chamada para função.
    