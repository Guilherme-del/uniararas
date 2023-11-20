import React from 'react';
import {
  ScrollView,
  View,
  TouchableOpacity,
  Text,
  Image,
  StyleSheet,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';

const appIcon = require('../../img/app-icon-120x120.png');

function MenuScreen() {
  const navigation = useNavigation();

  const pushScreen = (screen, props) => {
    navigation.navigate(screen, props);
  }

  return (
    <ScrollView>
      <View style={styles.container}>
        <Image source={appIcon} style={styles.image} />
        <TouchableOpacity
          style={styles.menu}
          onPress={() => pushScreen('Agenda')}>
          <Text style={styles.menuText}>Agenda</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
  },
  image: {
    margin: 30,
    width: 90,
    height: 90,
  },
  menu: {
    width: 300,
    padding: 10,
    margin: 10,
    alignItems: 'center',
    borderRadius: 20,
    borderWidth: 1,
    borderColor: '#7a92a5',
  },
  menuText: {
    fontSize: 18,
    color: '#2d4150',
  },
});

export default MenuScreen;
