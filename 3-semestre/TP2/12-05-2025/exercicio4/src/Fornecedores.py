class Fornecedor:
    def __init__(self, nomeFornecedor, nomeProduto, descricaoProduto):
        self.__nomeFornecedor = nomeFornecedor
        self.__nomeProduto = nomeProduto
        self.__descricaoProduto = descricaoProduto

    def getNomeFornecedor(self):
        return self.__nomeFornecedor
    
    def setNomeFornecedor(self, nome):
        self.__nomeFornecedor = nome

    def getNomeProduto(self):
        return self.__nomeProduto
    
    def setNomeProduto(self, produto):
        self.__nomeProduto = produto
    
    def getDescricaoProduto(self):
        return self.__descricaoProduto

    def setDescricaoProduto(self, desc):
        self.__descricaoProduto = desc

    def cadastrarFornecedor(self, nome, produto, desc):
        self.setNomeFornecedor(nome)
        self.setNomeProduto(produto)
        self.setDescricaoProduto(desc)

    def listarFornecedor(self):
        print(f"Nome do Fornecedor: {self.getNomeFornecedor()}")
        print(f"Nome do Produto: {self.getNomeProduto()}")
        print(f"Descricao do Produto: {self.getDescricaoProduto()}")