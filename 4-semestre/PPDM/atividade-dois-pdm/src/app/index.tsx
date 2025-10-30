import { StyleSheet, View } from "react-native";
import Card from "../components/Card";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Card />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#0D1117",
  },
  header: {
    fontSize: 22,
    fontWeight: "bold",
    marginBottom: 24,
    color: "#C9D1D9",
  },
});