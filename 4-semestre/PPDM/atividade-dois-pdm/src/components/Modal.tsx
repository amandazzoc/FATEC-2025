import { Modal, Pressable, Text, TextInput, View } from "react-native";
import styles from "../styles/styles";

type Props = {
  readonly modalVisible: boolean;
  readonly setModalVisible: (visible: boolean) => void;
  readonly githubUser: string;
  readonly setGithubUser: (user: string) => void;
  readonly handleAtualizarFoto: () => void;
};

export default function CustomModal({
  modalVisible,
  setModalVisible,
  githubUser,
  setGithubUser,
  handleAtualizarFoto,
}: Props) {
  return (
    <Modal transparent visible={modalVisible} animationType="fade">
      <View style={styles.modalOverlay}>
        <View style={styles.modalContent}>
          <Text style={styles.modalTitle}>Alterar foto</Text>

          <TextInput
            style={styles.modalInput}
            placeholder="Digite o usuário do GitHub"
            placeholderTextColor="#9ca3af"
            value={githubUser}
            onChangeText={setGithubUser}
          />

          <View style={styles.modalButtons}>
            <Pressable
              style={styles.modalCancel}
              onPress={() => setModalVisible(false)}
            >
              <Text style={styles.modalCancelText}>Cancelar</Text>
            </Pressable>

            <Pressable
              style={styles.modalConfirm}
              onPress={handleAtualizarFoto}
            >
              <Text style={styles.modalConfirmText}>Atualizar</Text>
            </Pressable>
          </View>
        </View>
      </View>
    </Modal>
  );
}
