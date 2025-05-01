import styles from "@/components/EditContent/EditContent.module.css";
import { useEffect } from "react";

const EditContent = ({ onClose }) => {
  // Criando os estados para as informações do jogo
  const [id, setId] = useState("");
  const [title, setTitle] = useState("");
  const [platform, setPlatform] = useState("");
  const [genre, setGenre] = useState("");
  const [rating, setRating] = useState("");
  const [year, setYear] = useState("");
  const [price, setPrice] = useState("");
  
  useEffect(() => {
    if(game){
      setTitle(game.title);
      setPlatform(game.descriptions.platform);
      setGenre(game.descriptions.genre);
      setRating(game.descriptions.rating);
      setYear(game.year);
      setPrice(game.price);
      setId(game._id);
    }
  }, [game])

  const handleSubmit = async (e) => {
    e.preventDefault()

    const updatedGame = {
      title,
      year,
      price,
      descriptions: {
        platform,
        genre,
        rating,
      },
    }
    try {
      const response = await axios.put(`http://localhost:4000/games/${id}`)
      if(response.status === 200){
        alert("Jogo editado com sucesso!")
        router.push("/home")
      }
    } catch(error) {
      console.error(error);
    }
  }

  // Enviando para API
  
  return (
    <>
      {/* CARD EDIÇÃO */}
      <div className={styles.editModal} id={styles.editModal}>
        <div className={styles.editContent}>
          <span className={styles.modalClose} onClick={onClose}>
            &times;
          </span>
          {/* TITLE */}
          <div className="title">
            <h2>Editar jogo</h2>
          </div>
          <form id="editForm">
            <input type="hidden" name="id" />
            <input
              type="text"
              name="title"
              placeholder="Insira o novo título"
              className="inputPrimary"
              required
              value={title}
            />
            <input
              type="text"
              name="platform"
              placeholder="Insira a nova plataforma do jogo"
              className="inputPrimary"
              required
              value={platform}
            />
            <input
              type="text"
              name="genre"
              placeholder="Insira o gênero do jogo"
              className="inputPrimary"
              required
              value={genre}
            />
            <input
              type="text"
              name="rating"
              placeholder="Insira a classificação do jogo"
              className="inputPrimary"
              required
              value={rating}
            />
            <input
              type="number"
              name="year"
              placeholder="Insira o novo ano"
              className="inputPrimary"
              required
              value={year}
            />
            <input
              type="text"
              name="price"
              placeholder="Insira o novo preço"
              className="inputPrimary"
              required
              value={price}
            />
            <input type="submit" value="Alterar" className="btnPrimary" />
          </form>
        </div>
      </div>
    </>
  );
};

export default EditContent;
