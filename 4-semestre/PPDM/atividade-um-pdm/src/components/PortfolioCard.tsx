import { useRouter } from "expo-router";
import { TouchableOpacity, Text, View, Image, StyleSheet } from "react-native";

export function PortfolioCard() {

    const router = useRouter();

    const handleOnPress = () => {
        router.push("/amandas-world"); 
    };

  return (
    <TouchableOpacity style={styles.container} activeOpacity={0.7} onPress={handleOnPress}>
      <Text style={styles.title}>Veja também o meu portfólio!</Text>
      <View style={{ marginTop: 8 }}>
        <Image
            source={require('@/assets/images/portfolio.png')}
            style={styles.image}
        />
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#c0ffcc",
    padding: 16,
    borderRadius: 12,
    marginTop: 24,
  },
  title: {
    fontWeight: "bold",
    fontSize: 16,
  },
  image: {
    width: 300,
    height: 150,
    borderRadius: 8,
    marginTop: 8,
  },
});
