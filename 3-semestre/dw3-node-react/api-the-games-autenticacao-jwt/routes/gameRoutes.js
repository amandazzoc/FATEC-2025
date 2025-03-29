import express from "express";
const gameRoutes = express.Router();
import gameController from "../controllers/gameController.js";
// Importando o middleware de autenticação
import {Authorization} from '../middleware/Auth.js'

// Endpoint para listar todos os games (rota)
gameRoutes.get("/games", Authorization, gameController.getAllGames);

// Endpoint para cadastrar um jogo
gameRoutes.post("/games", Authorization, gameController.createGame);

// Endpoint para excluir um jogo
gameRoutes.delete("/games/:id", Authorization, gameController.deleteGame);

// Endpoint para alterar um jogo
gameRoutes.put("/games/:id", Authorization, gameController.updateGame);

// Endpoint para listar um único jogo
gameRoutes.get("/games/:id", Authorization, gameController.getOneGame);

export default gameRoutes;
