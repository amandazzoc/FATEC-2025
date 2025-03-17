<?php
// Inclui o autoload do Composer, que carrega automaticamente todas as dependências do projeto
require_once 'vendor/autoload.php';

// Usa a classe Factory do pacote Kreait\Firebase
use Kreait\Firebase\Factory;

// Define a classe FirebaseCRUD
class FirebaseCRUD {
    // Declara uma propriedade privada chamada $database
    private $database;

    // Define o método construtor da classe
    public function _construct() {
        // Cria uma instância da Factory e configura com a conta de serviço e a URI do banco de dados
        $firebase = (new Factory)
            ->withServiceAccount(__DIR__.'/chave.json') // Define o caminho para o arquivo de chave do serviço
            ->withDatabaseUri('https://biblioteca-dsm3-68b6f-default-rtdb.firebaseio.com/') // Define a URI do banco de dados
            ->createDatabase(); // Cria a instância do banco de dados

        // Inicializa a conexão com o Realtime Database
        $this->database = $firebase;
    }

    // Adicionar um novo nó ao banco de dados
    public function create($livro) {
        // Adiciona um novo nó ao banco de dados
        $ref = $this->database->getReference('livros')->push($livro);
    }

    // Consultar os dados do banco de dados
    public function read() {
        $ref = $this->database->getReference('livros');
        $livros = $ref->getValue();
    }

    // Atualizar um nó do banco de dados
    public function update($id, $livro){
        $ref = $this->database->getReference('livros/'.$id)->set($livro);
    }

    // Excluir um nó do banco de dados
    public function delete($id){
        $ref = $this->database->getReference('livros/'.$id)->remove();
    }
}
?>