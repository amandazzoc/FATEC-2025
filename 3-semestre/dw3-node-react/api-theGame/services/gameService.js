import Game from "../models/games.js";

class gameService {
  async getAll() {
    try {
      const games = await Game.find();
      return games;
    } catch (error) {
      console.log(error);
    }
  }

  // Cad jogos
  async Create(title, plataform, year, price) { // necessário passar os parametros que serão cadastrados para a função
    try {
      const newGame = new Game({ title, plataform, year, price }); // cria um novo Game com todos os parametros que serão recebidos pelo gameController
      await newGame.save(); //.save é o método que salva no banco de dados
    } catch (error) {
      console.log(error);
    }
  }

  // delete jogo
  async Delete(id){
    try{
        await Game.findByIdAndDelete(id)
        console.log(`Game com a id: ${id} foi excluído.`);
    } catch(error){
        console.log(error);
    }
  }
}

export default new gameService();
