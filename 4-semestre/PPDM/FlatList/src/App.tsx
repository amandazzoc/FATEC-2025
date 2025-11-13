import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image, Pressable } from 'react-native';
import CARDAPIO_PIZZAS, { Pizza } from './constants/cardapio';

export default function App() {
  const renderItem = ({ item }: { item: Pizza }) => (
    <View style={styles.card}>
      <Image 
        source={{ uri: item.imagem }}
        style={styles.image}
      />
      <View>
        <Text style={styles.name}>{item.nome}</Text>
        <Text style={styles.description}>{item.descricao}</Text>
        <Text style={styles.price}>R$ {item.preco.toFixed(2)}</Text>
        <Pressable style={styles.button}>
          <Text style={styles.buttonText}>Adicionar ao carrinho</Text>
        </Pressable>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Cardápio de Pizzas</Text>
        <Text style={styles.subtitle}>Escolha sua pizza favorita!</Text>
        <FlatList
          data={CARDAPIO_PIZZAS}
          renderItem={renderItem}
          keyExtractor={item => item.id.toString()}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#cd1c18',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 30,
    paddingTop: 80,
  },
  content: {
    height: '100%',
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 20,
  },
  card: {
    marginBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#fec817',
    paddingBottom: 10,
    flexDirection: 'row',
    alignItems: 'center',
    position: 'relative',
  },
  image: {
    width: 100,
    height: 100,
    borderRadius: 1000,
    marginRight: 10,
  },
  name: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  description: {
    fontSize: 14,
    color: '#555',
    width: 180,
  },
  price: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 5,
    color: '#cd1c18',
  },
  button: {
    position: 'relative',
    marginTop: 10,
    backgroundColor: '#cd1c18',
    padding: 10,
    borderRadius: 5,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#cd1c18',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#555',
    marginBottom: 20,
    textAlign: 'center',
  },
});
