import { Button, Image, StyleSheet, Text, View } from "react-native";
import { useRouter } from "expo-router";
import { FavoriteButton } from "./FavoriteButton";

export default function Card() {
    const router = useRouter();

    const handleOnPress = () => {
      router.push("/github"); 
    };

  return (
    <View style={styles.card}>
      <Image
        source={{ uri: "https://github.com/amandazzoc.png" }}
        style={styles.profileImage}
      />
      <Text style={styles.title}>Amanda de Oliveira Costa</Text>
      <View style={styles.button}>
        <Button title="Abrir Github" onPress={handleOnPress} />
      </View>
      <FavoriteButton />
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: "#ffffff",
    padding: 20,
    borderRadius: 16,
    shadowColor: "#0b1226",
    shadowOpacity: 0.08,
    shadowOffset: { width: 0, height: 8 },
    shadowRadius: 20,
    elevation: 6,
    marginVertical: 12,
    marginHorizontal: 20,
    alignItems: "center",
    borderWidth: 1,
    borderColor: "rgba(11,18,38,0.04)",
  },
  profileImage: {
    width: 128,
    height: 128,
    borderRadius: 64,
    borderWidth: 4,
    borderColor: "#ffffff",
    backgroundColor: "#f0f2f5",
    marginTop: -84,
    shadowColor: "#000",
    shadowOpacity: 0.12,
    shadowOffset: { width: 0, height: 6 },
    shadowRadius: 12,
    elevation: 4,
  },
  title: {
    fontSize: 20,
    fontWeight: "700",
    color: "#0f1724",
    marginTop: 12,
    marginBottom: 4,
    textAlign: "center",
  },
  content: {
    fontSize: 14,
    color: "#475569",
    textAlign: "center",
    marginBottom: 12,
    lineHeight: 20,
  },
  button: {
    marginTop: 12,
    width: "70%",
    borderRadius: 999,
    overflow: "hidden",
    alignSelf: "center",
  },
  badge: {
    position: "absolute",
    top: 12,
    right: 12,
    backgroundColor: "#fffbeb",
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "rgba(255,200,0,0.2)",
  },
  badgeText: {
    fontSize: 12,
    color: "#92400e",
    fontWeight: "600",
  },
});
