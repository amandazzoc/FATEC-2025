/* eslint-disable @next/next/no-img-element */
import styles from "@/components/HomeContent/HomeContent.module.css";
import Loading from "../Loading";
import axios from "axios";
import { useState, useEffect } from "react";
import Image from "next/image";

const HomeContent = () => {
  // Estado para armazenar os jogos
  const [games, setGames] = useState([]);
  // Estado para o loading
  const [loading, setLoading] = useState(true);

  const fetchGames = async () => {
    try {
      const response = await axios.get("http://localhost:4000/games");
      const data = response.data.games;
      setGames(data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  // Função para deletar um jogo
  const handleDeleteGame = async (id) => {
    try {
      const response = await axios.delete(`http://localhost:4000/games/${id}`);
      if (response.status === 204) {
        alert("Jogo deletado com sucesso!");
      }
      setGames(games.filter(game => game._id !== id)) // Atualiza a lista de jogo, deixa na lista apenas os jogos que tiverem o id diferente do ID deletado
    } catch (error) {
      console.log(error);
    }
  };

  // Efeito colateral para buscar os jogos
  useEffect(() => {
    fetchGames();
  }, []);

  return (
    <>
      <div className={styles.homeContent}>
        {/* CARD LISTA DE JOGOS */}
        <div className={styles.listGamesCard}>
          {/* TITLE */}
          <div className={styles.title}>
            <h2>Lista de jogos</h2>
          </div>
          {/* LOADING */}
          <Loading loading={loading} />

          <div className={styles.games} id={styles.games}>
            {/* Lista de jogos irá aqui */}
            {games.map((game) => (
              <ul key={game._id} className={styles.listGames}>
                <div className={styles.gameImg}>
                  <img src="images/game_cd_cover.png" alt="Jogo em estoque" />
                </div>
                <div className={styles.gameInfo}>
                  <h3>{game.title}</h3>
                  <li>Plataforma: {game.descriptions.platform}</li>
                  <li>Gênero: {game.descriptions.genre}</li>
                  <li>Classificação: {game.descriptions.rating}</li>
                  <li>Ano: {game.year}</li>
                  <li>
                    Preço:{" "}
                    {game.price.toLocaleString("pt-br", {
                      style: "currency",
                      currency: "BRL",
                    })}
                  </li>
                  <button
                    className={styles.btnDel}
                    onClick={() => {
                      const confirmed = window.confirm(
                        "Deseja mesmo excluir o jogo?"
                      );
                      if (confirmed) {
                        handleDeleteGame(game._id);
                      }
                    }}
                  >
                    Deletar
                  </button>
                </div>
              </ul>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default HomeContent;
