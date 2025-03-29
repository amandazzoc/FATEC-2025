import mongoose from "mongoose";

const dbUser = "mandica7b";
const dbPassword = "cKbU97oY9xrkUfot";
const connect = () => {
  mongoose.connect(
    `mongodb+srv://${dbUser}:${dbPassword}@cluster0.edrnwkp.mongodb.net/api-thegames?retryWrites=true&w=majority&appName=Cluster0`
  );
  const connection = mongoose.connection;
  connection.on("error", () => console.error("Error to connect to database"));
  connection.once("open", () => console.log("Connected to database"));
};
connect();
export default connect;
