import { useEffect, useState } from "react";
import { FlatList, View, Text } from "react-native"

const API_URL = "https://jsonplaceholder.typicode.com/photos?_limit=1000";

type Photo = {
    albumId: number;
    id: number;
    title: string;
    url: string;
    thumbnailUrl: string;
}

export default function FlatListFetch() {
    const [data, setData] = useState<Photo[]>([]);
    const [loading, setLoading] = useState(true);

    const fetchData = async () => {
       fetch(API_URL)
         .then(response => response.json())
         .then(json => setData(json))
         .catch(error => console.error(error))
         .finally(() => setLoading(false));
    };

    useEffect(() => {
       fetchData();
    }, []);

    const loadingComponent = () => (
        <Text>Carregando...</Text>
    )

    return (
        <FlatList 
            data={data}
            keyExtractor={(item: Photo) => item.id.toString()}
            onViewableItemsChanged={({ viewableItems, changed }) => {
                console.log("Itens visíveis:", viewableItems.map(item => item.key));
                console.log("Itens alterados:", changed.map(item => item.key));
            }}
            renderItem={({ item }) => (
                <View>
                    {loading ? loadingComponent() : (
                        <Text numberOfLines={2}>
                            {item.id}: {item.title}
                        </Text>
                    )}
                </View>
            )}
        />
    )
};