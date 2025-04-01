const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')   
const {ObjectId} = require('mongodb')

//Configuração do EJS como Template Engine
app.set('view engine', 'ejs')

mongoose.connect("mongodb://localhost:27017/receitaDB", {
    useNewUrlParser: true, 
    useUnifiedTopology: true
})

// Módulo de receita
const Receita = mongoose.model("Receita", {
    nome: String,
    ingredientes: [String],
    instrucoes: String,
})


app.get("/", async(req, res) => {
    const searchQuery = req.query.search
    const page = parseInt(req.query.page) || 1
    const perPage = 5

    let query
})

app.get('/editar/:id', async(req, res) => {
    try{
        const receita = await Receita.findById(req.params.id)
        res.render('editar', {receita})
    }catch(err){
        console.error(err)
        res.status(500).send("Erro ao buscar receita")
    }
})

app.post('/editar/:id', async(req, res)=> {
    try{
        await Receita.findByIdAndUpdate(req.params.id, {
            nome, 
            ingredientes: ingredientesArray,
            instrucoes
        })
        res.redirect('/')
    }catch(err){
        console.error(err)
        res.status(500).send("Erro ao editar receita")
    }
})

//Iniciar servidor
const port = 3000
app.listen(port, ()=> {
    console.log('Servidor rodando em http://localhost:${port}');
})