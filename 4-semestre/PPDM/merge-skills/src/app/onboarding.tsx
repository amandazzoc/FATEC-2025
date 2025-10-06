import { Button, StyleSheet, Text, View } from "react-native";
import { useState } from "react";

const onboardingSteps = [
    {
        title: 'Explore trilhas',
        subtitle: 'Descubra trilhas de aprendizado personalizadas para suas necessidades.'
    },
    { 
        title: 'Resolva desafios',
        subtitle: 'Supere obstáculos e teste suas habilidades'
    },
    {
        title: 'Crie e compartilhe',
        subtitle: 'Crie e compartilhe seu próprio conteúdo de aprendizado'
    }
];

export default function OnboardingScreen() {
    const [step, setStep] = useState(1);

    const handleNext = () => {
        if (step < onboardingSteps.length - 1) {
            setStep(step + 1);
        } else {
            // Finalizar o onboarding
        }
    }

  return (
    <View style={styles.container}>
        <View style={styles.content}>
            <Text style={styles.title}>Bem-vindo ao App!</Text>
            <Text style={styles.subtitle}>Seu guia para uma experiência incrível.</Text>
        </View>
        <View style={styles.footer}>
            <Button title={step === onboardingSteps.length - 1 ? "COMEÇAR" : "PRÓXIMO"} onPress={handleNext} />
            <Button title="Pular" onPress={() => setStep(3)} />
        </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    backgroundColor: "#ffffff",
  },
  content: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  logo: {
    width: 150,
    height: 150,
    resizeMode: "contain",
    marginBottom: 40,
  },
  footer: {
    width: "100%",
    gap: 12,
    paddingBottom: 40,
  },
  title: {
    fontSize: 32,
    fontWeight: "bold",
    marginBottom: 10,
    textAlign: "center",
    color: "#112437",
  },
  subtitle: {
    fontSize: 18,
    color: "#4a4a4a",
    textAlign: "center",
    marginBottom: 30,
  },
});
