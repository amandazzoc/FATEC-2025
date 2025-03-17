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

  // update jogo
  async Update(id, title, plataform, year, price){
    try{
      const updatedGame = await Game.findByIdAndUpdate(
        id, 
        {
          title, 
          plataform, 
          year, 
          price
        }, 
        {
          new: true
        }
      );
      console.log(`Dados do game de id: ${id} foram atualizados.`);
      return updatedGame;
    } catch(error){
      console.log(error);
    }
  }

  async getById(id){
    try{
      const game = await Game.findById({_id: id});
      return game;
    } catch(error){
      console.log(error);
    }
  }
}

export default new gameService();
