import { router } from 'expo-router';
import { Button, Pressable, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function Buttons() {
    return (
        <View style={styles.container}>
            <Button title="Botão Padrão" />

            <TouchableOpacity activeOpacity={0.8} style={styles.button}>
                <Text>Pressione-me</Text>
            </TouchableOpacity>

            {/* Pressable é mais flexível que TouchableOpacity */}
            <Pressable
                onPress={() => alert('Pressionado!')}
                onLongPress={() => alert('Pressionado por muito tempo!')}
                onPressOut={() => alert('Pressionamento finalizado!')}
                delayLongPress={1000}
                style={styles.button}
            >
                <Text>Pressione-me também</Text>
            </Pressable>

            <TouchableOpacity onPress={() => router.back()}>
                <Text style={styles.backLink}>Voltar</Text>
            </TouchableOpacity>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 32,
        gap: 16,
        backgroundColor: "#f0f0f0"
    },

    button: {
        backgroundColor: "#DDD",
        padding: 16,
        borderRadius: 8,
        alignItems: 'center'
    },

    backLink: {
        color: "#1d1d1d",
        textAlign: "center",
        textDecorationLine: "underline"
    }
})