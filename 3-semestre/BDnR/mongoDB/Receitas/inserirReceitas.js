import mongoose from 'mongoose'

mongoose.connect('mongodb://localhost/receitas', {useNewUrlParser: true, useUnifiedTopology: true})

// Lista de receitas para inserir
const receitas = [
    {
        nome: "Bolo de chocolate",
        ingredientes: ["farinha", "açúcar", "chocolate", "ovos", "leite"],
        instrucoes: "Misturar tudo e assar"
    }
]

// Inserir receitas no banco de dados
async function inserirReceitas() {
    try{
        await Receita.deleteMany({})
        await Receita.insertMany(receitas)
        console.log('Receitas inseridas com sucesso')
        mongoose.connection.close()
    }catch(err){
        console.error('Erro ao inserir as receitas: ' + err)
        mongoose.connection.close()
    }
}

inserirReceitas()