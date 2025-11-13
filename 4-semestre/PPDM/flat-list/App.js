import { useEffect, useState } from 'react';
import { Flatlist, Text, View } from 'react-native';

const LOCAL_DATA = [
  {id: '1', title: 'First Item', description: 'This is the first item'},
  {id: '2', title: 'Second Item', description: 'This is the second item'},
  {id: '3', title: 'Third Item', description: 'This is the third item'},
  {id: '4', title: 'Fourth Item', description: 'This is the fourth item'},
  {id: '5', title: 'Fifth Item', description: 'This is the fifth item'},
  {id: '6', title: 'Sixth Item', description: 'This is the sixth item'},
  {id: '7', title: 'Seventh Item', description: 'This is the seventh item'},
]

const API_URL = 'https://jsonplaceholder.typicode.com/photos?_limit=1000';

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  })

  const render = ({ item }) => (
    <View>
      <Text>{item.title}: {item.description}</Text>
      <Button title="Adicionar Item" color="#841584" onPress={() => {}} />
    </View>
  )

  return (
    <Flatlist
      data={LOCAL_DATA}
      renderItem={render}
      keyExtractor={item => item.id}
    />
  );
}
