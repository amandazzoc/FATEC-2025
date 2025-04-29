import { useState } from "react";
import styles from "@/components/CreateContent/CreateContent.module.css";
import {useRouter} from "next/router";
import axios from "axios";

const CreateContent = () => {
  // Criando os estados para as informações do jogo
  const [title, setTitle] = useState("");
  const [platform, setPlatform] = useState("");
  const [genre, setGenre] = useState("");
  const [rating, setRating] = useState("");
  const [year, setYear] = useState("");
  const [price, setPrice] = useState("");
  const router = useRouter();

  // Tratando a submissão do formulário
  const handleSubmit = async(e) => {
    e.preventDefault()
    if(title && platform && genre && rating && year && price !== "") {
       const game = {
         title: title,
         year: year,
         price: price,
         descriptions: {
           platform: platform,
           genre: genre,
           rating: rating,
         },
       };
       
      // Post na api de cadastro
      try{
        const response = await axios.post("http://localhost:4000/games", game)
        console.log(response)
        if (response.status === 201) {
          alert("Jogo cadastrado com sucesso!");
          router.push("/home")
        }
      }catch(error) {
        console.log(error);
      }
    }else {
      alert("Preencha todos os campos corretamente!")
    }
  }

  return (
    <div className={styles.createContent}>
      <div className="title">
        <h2>Cadastrar novo jogo</h2>
      </div>
      <form id="createForm" className="formPrimary" onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          id="title"
          placeholder="Insira o título do jogo"
          className="inputPrimary"
          onChange={(e) => setTitle(e.target.value)}
          value={title}
          required
        />
        <input
          type="text"
          name="platform"
          id="platform"
          placeholder="Insira a plataforma do jogo"
          className="inputPrimary"
          onChange={(e) => setPlatform(e.target.value)}
          value={platform}
          required
        />
        <input
          type="text"
          name="genre"
          id="genre"
          placeholder="Insira o gênero do jogo"
          className="inputPrimary"
          onChange={(e) => setGenre(e.target.value)}
          value={genre}
          required
        />
        <input
          type="text"
          name="rating"
          id="rating"
          placeholder="Insira a classificação do jogo"
          className="inputPrimary"
          onChange={(e) => setRating(e.target.value)}
          value={rating}
          required
        />
        <input
          type="number"
          name="year"
          id="year"
          placeholder="Insira o ano do jogo"
          className="inputPrimary"
          onChange={(e) => setYear(e.target.value)}
          value={year}
          required
        />
        <input
          type="number"
          name="price"
          id="price"
          placeholder="Insira o preço do jogo"
          className="inputPrimary"
          onChange={(e) => setPrice(e.target.value)}
          value={price}
          required
        />
        <input
          type="submit"
          value="Cadastrar"
          id="createBtn"
          className="btnPrimary"
        />
      </form>
    </div>
  );
};

export default CreateContent;
