import gameService from "../services/gameService.js";
import { ObjectId } from "mongodb" // importação para identificar se o id é valido

const getAllGames = async (req, res) => {
  try {
    const games = await gameService.getAll(); // espera pegar todos os dados do service
    // Requisição feita com sucesso - Cod. 200 (OK)
    res.status(200).json({ games: games });
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Erro interno do servidor." });
  }
};

// Função para criar um novo jogo
const createGame = async (req, res) => {
    try {
        const {title, plataform, year, price} = req.body // pega da requisição
        await gameService.Create(title, plataform, year, price) // manda para o service
        res.sendStatus(201); // retorna a mensagem de sucesso, objeto criado
    }catch(error) {
        console.log(error);
        res.status(500).json({error: "Erro interno do servidor"})
    }
}

// Função para deletar jogos
const deleteGame = async (req, res) => {
    try{
        if(ObjectId.isValid(req.params.id)) {
            const id = req.params.id
            gameService.Delete(id)
            res.sendStatus(204); // código 204 confirma que foi excluido
        } else {
            res.sendStatus(400).json({ error:"O ID não existe" }); // bad request, requisição mal formada
        }
    }catch(error){
        console.log(error)
        res.status(500).json({ error: "Erro interno do servidor" });
    }
}
export default { getAllGames, createGame, deleteGame };
