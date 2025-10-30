import CustomModal from "@/src/components/Modal";
import { ProfileStorage } from "@/src/service/profileStorage";
import styles, { colors } from "@/src/styles/styles";
import { router, useFocusEffect } from "expo-router";
import { useCallback, useState } from "react";
import {
  Image,
  KeyboardAvoidingView,
  Platform,
  Pressable,
  ScrollView,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";

export default function EditarPerfilScreen() {
  const [loading, setLoading] = useState(true);
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [age, setAge] = useState("");
  const [institution, setInstitution] = useState("");
  const [course, setCourse] = useState("");

  const [githubUser, setGithubUser] = useState("");
  const [modalVisible, setModalVisible] = useState(false);

  const handleLoadProfile = async () => {
    const savedProfile = await ProfileStorage.load();

    if (savedProfile) {
      setName(savedProfile.name);
      setSurname(savedProfile.surname);
      setAge(String(savedProfile.age));
      setInstitution(savedProfile.institution);
      setCourse(savedProfile.course);
      setGithubUser(savedProfile.githubUser);
    }
  };

  useFocusEffect(
    useCallback(() => {
      handleLoadProfile();
      setLoading(false);
    }, [])
  );

  const handleCancel = () => {
    setName("");
    setSurname("");
    setAge("");
    setInstitution("");
    setCourse("");
    setGithubUser("");
    router.back();
  };

  const handleSave = async () => {
    const updatedProfile = {
      githubUser,
      name,
      surname,
      age: Number(age),
      institution,
      course,
    };

    await ProfileStorage.save(updatedProfile);
    router.back();
  };

  const handleAtualizarFoto = () => {
    setModalVisible(false);
  };

  if (loading) {
    return (
      <View style={[styles.container, { justifyContent: "center" }]}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <KeyboardAvoidingView
      style={{ flex: 1, backgroundColor: "#0D1117" }} // Cor de fundo aqui também
      behavior={Platform.OS === "ios" ? "padding" : "height"}
    >
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.header}>
          <Text style={styles.title}>Editar Perfil</Text>
        </View>

        <TouchableOpacity
          style={styles.avatarContainer}
          onPress={() => setModalVisible(true)}
        >
          <Image
            source={{ uri: `https://github.com/${githubUser}.png` }}
            style={styles.avatar}
          />
          <Text style={styles.changePhotoText}>Alterar foto</Text>
        </TouchableOpacity>

        <View style={styles.form}>
          <View style={{ flexDirection: "row", gap: 8, width: "100%" }}>
            <TextInput
              style={[styles.input, { flex: 1 }]}
              placeholder="Nome"
              placeholderTextColor={colors.textSecondary}
              value={name}
              onChangeText={setName}
            />
            <TextInput
              style={[styles.input, { flex: 1 }]}
              placeholder="Sobrenome"
              placeholderTextColor={colors.textSecondary}
              value={surname}
              onChangeText={setSurname}
            />
          </View>
          <TextInput
            style={styles.input}
            placeholder="Idade"
            placeholderTextColor={colors.textSecondary}
            keyboardType="numeric"
            value={age}
            onChangeText={setAge}
          />
          <TextInput
            style={styles.input}
            placeholder="Instituição"
            placeholderTextColor={colors.textSecondary}
            value={institution}
            onChangeText={setInstitution}
          />
          <TextInput
            style={styles.input}
            placeholder="Curso"
            placeholderTextColor={colors.textSecondary}
            value={course}
            onChangeText={setCourse}
          />

          <Pressable
            style={({ pressed }) => [
              styles.saveButton,
              pressed && { transform: [{ scale: 0.98 }], opacity: 0.9 },
            ]}
            onPress={handleSave}
          >
            <Text style={styles.saveButtonText}>Salvar alterações</Text>
          </Pressable>

          <Pressable
            style={({ pressed }) => [
              styles.cancelButton,
              pressed && { transform: [{ scale: 0.98 }], opacity: 0.9 },
            ]}
            onPress={handleCancel}
          >
            <Text style={styles.cancelButtonText}>Cancelar</Text>
          </Pressable>
        </View>
      </ScrollView>

      <CustomModal
        modalVisible={modalVisible}
        setModalVisible={setModalVisible}
        githubUser={githubUser}
        setGithubUser={setGithubUser}
        handleAtualizarFoto={handleAtualizarFoto}
      />
    </KeyboardAvoidingView>
  );
}
