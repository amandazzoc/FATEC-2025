import { router, useFocusEffect } from "expo-router";
import { useCallback, useState } from "react";
import { Image, Pressable, Text, View } from "react-native";
import { ProfileStorage } from "../service/profileStorage";
import styles from "../styles/styles";
import { UserProfile } from "../types/profile";

export default function Card() {
  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState<UserProfile>({
    githubUser: "",
    name: "Seu",
    surname: "Nome",
    age: 0,
    institution: "Sua Instituição",
    course: "Seu Curso",
  });

  const handleLoadProfile = async () => {
    const savedProfile = await ProfileStorage.load();

    if (savedProfile) {
      setProfile(savedProfile);
    }
  };

  useFocusEffect(
    useCallback(() => {
      handleLoadProfile();
      setLoading(false);
    }, [])
  );

  const handleOnPress = () => {
    router.push("/editar-perfil");
  };

  if (loading) {
    return (
      <View style={styles.loading}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <View style={styles.card}>
      <Image
        source={{ uri: `https://github.com/${profile?.githubUser}.png` }}
        style={styles.profileImage}
      />
      <Text style={styles.title}>
        {profile?.name} {profile?.surname}
      </Text>

      <View style={styles.content}>
        <Text style={styles.contentText}>{profile?.age} anos</Text>
        <Text style={styles.contentText}>{profile?.institution}</Text>
        <Text style={styles.contentText}>{profile?.course}</Text>
      </View>

      <Pressable
        style={({ pressed }) => [
          styles.saveButton,
          pressed && { opacity: 0.8, transform: [{ scale: 0.98 }] },
        ]}
        onPress={handleOnPress}
      >
        <Text style={styles.saveButtonText}>Editar perfil</Text>
      </Pressable>
    </View>
  );
}
