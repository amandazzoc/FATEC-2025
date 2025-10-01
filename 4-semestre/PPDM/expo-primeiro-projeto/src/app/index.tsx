import { Image } from "expo-image"
//import * as WebBrowser from 'expo-web-browser';
import { Alert, Button, ScrollView, Text, View } from "react-native"
import Card from "../components/Card"

export default function Index() {
    return (
        /* JSX - HTML Javascript */
        <ScrollView>
            <View style={{ flex: 1, justifyContent: "center", padding: 32, gap: 16}}>

                <Image source="https://github.com/i-davies.png" style={{ width: 100, height: 100, borderRadius: 99}} />

                <Text style={{ fontSize: 32 }}>Hello World</Text>

                <Button title="Clique aqui" color={"#1d1d1d"} 
                onPress={ () => Alert.alert("Info", "Muito obrigado por clicar") } />

                {/* <Button title='Github' color={"#1d1d1d"} onPress={(e) => {
                    e.preventDefault();
    
                    WebBrowser.openBrowserAsync("https://github.com/i-davies");
                }
                }/> */}

                <Card title="Botões" body="Demonstração de Botões" href={"/buttons"}></Card>

                <Card title="FlatList" body="Demonstração de FlatList" href={"/flatlist-example"}></Card>

                <Card title="FlatList + Fetch" body="Demonstração de FlatList com Fetch" href={"/flatlist-fetch"}></Card>

                <Card title="FlashList + Fetch" body="Demonstração de FlashList com Fetch" href={"/flashlist"}></Card>

                <Card title="Inputs" body="Demonstração de Inputs" href={"/inputs"}></Card>
            </View>
        </ScrollView>
    )
}