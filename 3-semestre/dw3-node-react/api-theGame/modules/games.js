import mongoose from "mongoose";

const gameSchema = new mongoose.Schema({
  title: String,
  plataform: String,
  year: Number,
  price: Number,
});

// Criação da coleção Game no banco de dados
const Game = mongoose.model("Game", gameSchema);

export default Game;
