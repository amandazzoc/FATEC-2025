import { StyleSheet, Text, View } from "react-native";
import Card from "../components/Card";
import { PortfolioCard } from "../components/PortfolioCard";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Card />
      <PortfolioCard />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f2f2f2",
  },
  header: {
    fontSize: 22,
    fontWeight: "bold",
    marginBottom: 24,
  },
});
