import { TextInput, StyleSheet, View } from "react-native";

export default function Inputs() {
    return (
        <View style={styles.container}>
            <TextInput placeholder="Digite algo aqui..." style={styles.input}/>

            <TextInput placeholder="Digite sua senha aqui..." style={styles.input} secureTextEntry={true}/>

            <TextInput placeholder="Digite seu email aqui..." style={styles.input} keyboardType="email-address"/>

            <TextInput placeholder="Digite seu telefone aqui..." style={styles.input} keyboardType="phone-pad"/>
        </View>
    )
}

const styles = StyleSheet.create({
    input: {
        borderWidth: 1,
        borderColor: "#ccc",
        borderRadius: 4,
        padding: 12,
        marginVertical: 8
    },

    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 32,
        gap: 16,
        backgroundColor: "#f0f0f0"
    }
})