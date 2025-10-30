import { Pressable, Text } from "react-native";
import { useState } from "react";

export function FavoriteButton() {
  const [favorito, setFavorito] = useState(false);

  return (
    <Pressable
      style={{
        paddingVertical: 10,
        paddingHorizontal: 20,
        backgroundColor: favorito ? "#ffe4e6" : "#e2e8f0",
        borderRadius: 20,
        marginTop: 12,
      }}
      onPress={() => setFavorito(!favorito)}
    >
      <Text style={{ fontWeight: "600" }}>
        {favorito ? "★ Favorito" : "☆ Favoritar"}
      </Text>
    </Pressable>
  );
}
