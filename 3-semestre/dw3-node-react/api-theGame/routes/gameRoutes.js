import express from "express";
const gameRoutes = express.Router();
import gameController from "../controllers/gameController.js";

// Endpoint para listar todos os games
gameRoutes.get("/games", gameController.getAllGames);

// Endpoint para cadastrar jogo
gameRoutes.post("/games", gameController.createGame)

// Endpoint para excluir o jogo
gameRoutes.delete("/games/:id", gameController.deleteGame)

gameRoutes.put("/games/:id", gameController.updateGame)

gameRoutes.get("/games/:id", gameController.getOneGame)

export default gameRoutes;
