import Ionicons from "@react-native-vector-icons/ionicons";
import { useEffect, useState } from "react";
import { FlatList, Image, StyleSheet, Text, View } from "react-native";
import { API_URL } from "./constants/ApiUrl";
import { Product } from "./types/Product";

export default function App() {
  const [data, setData] = useState<Product[]>([]);

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error(error));
  }, []);

  const renderStars = (rating: number) => {
    const stars = [];
    for (let i = 1; i <= 5; i++) {
      if (rating >= i) {
        stars.push(<Ionicons key={i} name="star" size={22} color="#f4a261" />);
      } else if (rating >= i - 0.66) {
        stars.push(
          <Ionicons key={i} name="star-half" size={22} color="#f4a261" />
        );
      } else if (rating >= i - 0.33) {
        stars.push(
          <Ionicons key={i} name="star-outline" size={22} color="#f4a261" />
        );
      } else {
        stars.push(
          <Ionicons key={i} name="star-outline" size={22} color="#ccc" />
        );
      }
    }
    return stars;
  };

  const renderItem = (item: Product) => (
    <View style={styles.card}>
      <Image source={{ uri: item.image }} style={styles.image} />

      <Text style={styles.title} numberOfLines={2}>
        {item.title}
      </Text>

      <Text style={styles.description} numberOfLines={2}>
        {item.description}
      </Text>

      <Text style={styles.category}>Categoria: {item.category}</Text>

      <Text style={styles.price}>R$ {item.price.toFixed(2)}</Text>

      <View style={styles.ratingBox}>
        <View style={styles.ratingStars}>{renderStars(item.rating.rate)}</View>
        <Text style={styles.ratingText}>
          {item.rating.rate.toFixed(1)} ({item.rating.count} avaliações)
        </Text>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => renderItem(item)}
        contentContainerStyle={{ padding: 16 }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0f0f0f",
  },

  card: {
    backgroundColor: "#1a1a1a",
    borderRadius: 16,
    overflow: "hidden",
    marginBottom: 18,

    borderWidth: 1,
    borderColor: "#2a2a2a",

    shadowColor: "#000",
    shadowOpacity: 0.2,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 4 },
    elevation: 8,
  },

  image: {
    width: "100%",
    height: 420,
    resizeMode: "cover",
    backgroundColor: "#111",
  },

  title: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "600",
    marginTop: 12,
    marginHorizontal: 16,
  },

  description: {
    color: "#a5a5a5",
    fontSize: 14,
    marginTop: 6,
    marginHorizontal: 16,
    lineHeight: 20,
  },

  category: {
    marginTop: 8,
    marginHorizontal: 16,
    fontSize: 13,
    color: "#777",
    fontStyle: "italic",
  },

  price: {
    backgroundColor: "#2ecc71",
    alignSelf: "flex-start",
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 6,

    marginTop: 14,
    marginLeft: 16,

    fontSize: 17,
    fontWeight: "bold",
    color: "#0a0a0a",
  },

  ratingBox: {
    marginTop: 14,
    marginHorizontal: 16,
    marginBottom: 16,
    padding: 10,

    backgroundColor: "#242424",
    borderRadius: 8,
    flexDirection: "row",
    alignItems: "center",
  },

  ratingStars: {
    flexDirection: "row",
    alignItems: "center",
    marginRight: 6,
  },

  ratingText: {
    color: "#ccc",
    fontSize: 14,
  },
});
