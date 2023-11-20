import React from 'react';
import { View  } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import RootStackScreen from './src/components/navigator/stackScreen';
import Toast from 'react-native-toast-message';
import {toastConfig } from './src/components/toastConfig/toastify';

const App = () => {
  return (
    <NavigationContainer>
      <Toast config={toastConfig} />
      <RootStackScreen />
    </NavigationContainer>
  );
}

export default App;