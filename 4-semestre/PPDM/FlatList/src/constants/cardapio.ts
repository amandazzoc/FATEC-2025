export type Pizza = {
  id: number;
  nome: string;
  imagem: string;
  descricao: string;
  preco: number;
};

const CARDAPIO_PIZZAS = [
  {
    id: 1,
    nome: "Margherita",
    imagem:
      "https://images.unsplash.com/photo-1564936281291-294551497d81?q=80&w=752&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Clássica com molho de tomate, mussarela e manjericão fresco.",
    preco: 25.0,
  },
  {
    id: 2,
    nome: "Pepperoni",
    imagem:
      "https://images.unsplash.com/photo-1692737580547-b45bb4a02356?q=80&w=915&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Mussarela generosa e fatias crocantes de pepperoni.",
    preco: 30.0,
  },
  {
    id: 3,
    nome: "Quatro Queijos",
    imagem:
      "https://images.unsplash.com/photo-1732223229355-95a1433404bf?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao:
      "Combinação cremosa de mussarela, parmesão, gorgonzola e catupiry.",
    preco: 35.0,
  },
  {
    id: 4,
    nome: "Portuguesa",
    imagem:
      "https://images.unsplash.com/photo-1681567604770-0dc826c870ae?q=80&w=900&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Presunto, ovo, cebola e azeitonas sobre molho de tomate.",
    preco: 32.0,
  },
  {
    id: 5,
    nome: "Frango com Catupiry",
    imagem:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTqXdkQccDwNjqDufFvUROoVfI7GTQJbg5PRRDyuFhHxEnqFv__cb5zWMzwCqFzUrS1RY&usqp=CAU",
    descricao: "Frango desfiado e muito catupiry cremoso.",
    preco: 33.0,
  },
  {
    id: 6,
    nome: "Calabresa",
    imagem:
      "https://plus.unsplash.com/premium_photo-1733259709671-9dbf22bf02cc?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Rodelas de calabresa e cebola levemente dourada.",
    preco: 28.0,
  },
  {
    id: 7,
    nome: "Vegetariana",
    imagem:
      "https://plus.unsplash.com/premium_photo-1722945691819-e58990e7fb27?q=80&w=721&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Legumes frescos: tomate, pimentão, cebola, milho e azeitonas.",
    preco: 29.0,
  },
  {
    id: 8,
    nome: "Baiana",
    imagem:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5aDENWPYZ3n18iZQZXd6iS6EEWr1NkBVAFw&s",
    descricao:
      "Picante, com calabresa, pimenta e ovo para quem gosta de sabor forte.",
    preco: 34.0,
  },
  {
    id: 9,
    nome: "Havaiana",
    imagem:
      "https://images.unsplash.com/photo-1671572579989-fa11cbd86eef?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Presunto e abacaxi: combinação doce e salgada clássica.",
    preco: 31.0,
  },
  {
    id: 10,
    nome: "Champignon",
    imagem:
      "https://images.unsplash.com/photo-1662805524260-e357ebe326b5?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    descricao: "Mussarela com fatias de champignon fresquinho e orégano.",
    preco: 36.0,
  },
];

export default CARDAPIO_PIZZAS;
