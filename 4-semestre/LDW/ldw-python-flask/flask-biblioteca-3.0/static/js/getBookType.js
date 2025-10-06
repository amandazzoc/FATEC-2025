function getBookTypeText(type) {
  switch (type) {
    case 1:
      return "Lido";
    case 2:
      return "Lendo";
    case 3:
      return "Quero ler";
    case 4:
      return "Relendo";
    case 5:
      return "Abandonei";
    default:
      return "Desconhecido";
  }
}