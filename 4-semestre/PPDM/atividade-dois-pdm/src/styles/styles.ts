import { StyleSheet, Platform } from "react-native";

export const colors = {
  bg: "#0D1117", // Fundo principal (preto do GitHub)
  bgSecondary: "#161B22", // Fundo de "cards" ou inputs
  text: "#C9D1D9", // Texto principal (cinza-claro)
  textSecondary: "#8B949E", // Texto de placeholders (cinza-médio)
  border: "#30363D", // Cor da borda
  green: "#238636", // Botão de salvar
  greenText: "#FFFFFF", // Texto do botão de salvar
  buttonGray: "#21262D", // Botão de cancelar
  blueLink: "#58A6FF", // Cor de link (para "Alterar foto")
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: colors.bg,
    padding: 24,
    paddingTop: Platform.OS === "ios" ? 50 : 24,
  },
  header: {
    alignItems: "center",
    marginBottom: 24,
  },
  title: {
    fontSize: 28,
    fontWeight: "bold",
    color: colors.text,
  },
  avatarContainer: {
    alignItems: "center",
    marginBottom: 32,
  },
  avatar: {
    width: 120,
    height: 120,
    borderRadius: 60,
    borderWidth: 2,
    borderColor: colors.border,
  },
  changePhotoText: {
    color: colors.blueLink,
    fontSize: 16,
    marginTop: 12,
  },
  form: {
    width: "100%",
    alignItems: "center",
  },
  input: {
    width: "100%",
    backgroundColor: colors.bgSecondary,
    color: colors.text,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 6,
    paddingHorizontal: 16,
    paddingVertical: 12,
    fontSize: 16,
    marginBottom: 16,
  },
  saveButton: {
    backgroundColor: colors.green,
    paddingVertical: 14,
    paddingHorizontal: 32,
    borderRadius: 6,
    width: "100%",
    alignItems: "center",
    marginTop: 16,
  },
  saveButtonText: {
    color: colors.greenText,
    fontSize: 16,
    fontWeight: "bold",
  },
  cancelButton: {
    backgroundColor: colors.buttonGray,
    paddingVertical: 14,
    borderRadius: 6,
    width: "100%",
    alignItems: "center",
    marginTop: 12,
    borderWidth: 1,
    borderColor: colors.border,
  },
  cancelButtonText: {
    color: colors.text,
    fontSize: 16,
    fontWeight: "bold",
  },

  // --- Estilos da Modal ---
  modalOverlay: {
    flex: 1,
    backgroundColor: "rgba(0, 0, 0, 0.75)",
    justifyContent: "center",
    alignItems: "center",
  },
  modalContent: {
    width: "90%",
    maxWidth: 400,
    backgroundColor: colors.bgSecondary,
    borderRadius: 8,
    padding: 24,
    borderWidth: 1,
    borderColor: colors.border,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 10,
  },
  modalTitle: {
    fontSize: 22,
    fontWeight: "bold",
    color: colors.text,
    marginBottom: 20,
  },
  modalInput: {
    width: "100%",
    backgroundColor: colors.bg,
    color: colors.text,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 6,
    paddingHorizontal: 16,
    paddingVertical: 12,
    fontSize: 16,
    marginBottom: 24,
  },
  modalButtons: {
    flexDirection: "row",
    justifyContent: "flex-end",
    width: "100%",
    gap: 12,
  },
  modalConfirm: {
    backgroundColor: colors.green,
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 6,
  },
  modalConfirmText: {
    color: colors.greenText,
    fontWeight: "bold",
    fontSize: 16,
  },
  modalCancel: {
    backgroundColor: colors.buttonGray,
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: colors.border,
  },
  modalCancelText: {
    color: colors.text,
    fontWeight: "bold",
    fontSize: 16,
  },

  // --- Estilos do Card de Perfil ---
  loading: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: colors.bg,
  },
  card: {
    backgroundColor: colors.bgSecondary, 
    borderRadius: 8,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 24,
    margin: 20, 
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 10,
  },
  profileImage: {
    width: 140,
    height: 140,
    borderRadius: 70,
    borderWidth: 2,
    borderColor: colors.border,
    marginBottom: 20,
  },
  titleField: {
    fontSize: 26,
    fontWeight: "bold",
    color: colors.text,
    marginBottom: 8,
  },
  content: {
    alignItems: "center",
    marginBottom: 24,
  },
  contentText: {
    fontSize: 16,
    color: colors.textSecondary,
    marginBottom: 5,
  },
});

export default styles;
