import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import RootStackScreen from './src/components/navigator/stackScreen';
import Toast from 'react-native-toast-message';
import { toastConfig } from './src/components/toastConfig/toastify';
import SplashScreen from 'react-native-splash-screen'



const App = () => {

  useEffect(() => {
    SplashScreen.hide();
  }, []);

  return (
    <NavigationContainer>
      <Toast config={toastConfig} />
      <RootStackScreen />
    </NavigationContainer>
  );
}

export default App;