import jtw from "jsonwebtoken";
import userController from "../controllers/userController.js";

// função para checagem da autenticação
const Authorization = (req, res, next) => {
  // Coletar o token do cabeçalho da requisição
  const authToken = req.headers["authorization"];
  if (authToken != undefined) {
    // Dividindo o token
    const bearer = authToken.split(" ");
    const token = bearer[1];
    // Validando o token
    jtw.verify(token, userController.JWTSecret, (error, data) => {
      if (error) {
        res.status(401).json({ error: `Token inválido. Não autorizado` });
      } else {
        req.token = token;
        req.loggerUser = {
          id: data.id,
          email: data.email,
        };
        next();
      }
    });
  } else {
    res.status(401).json({ error: "Token inválido" });
  }
};

export {Authorization};
