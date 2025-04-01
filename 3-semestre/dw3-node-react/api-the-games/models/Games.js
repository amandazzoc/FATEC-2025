import mongoose from "mongoose";

const descriptionSchema = new mongoose.Schema({
  genre: String,
  plataform: String,
  rating: String
})

const gameSchema = new mongoose.Schema({
  title: String,
  year: Number,
  price: Number,
  description: [descriptionSchema]
});

// Aqui está sendo criado a coleção games no banco de dados
const Game = mongoose.model("Game", gameSchema);

export default Game;
