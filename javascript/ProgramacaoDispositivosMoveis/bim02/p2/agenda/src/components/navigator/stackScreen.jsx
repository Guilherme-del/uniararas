import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import MenuScreen from '../../screens/menu/index';
import AgendaScreen from '../../screens/agenda/index';

export default function RootStackScreen() {
  const Stack = createNativeStackNavigator();

  return (
      <Stack.Navigator initialRouteName="Menu">
        <Stack.Screen name="Menu" component={MenuScreen} />
        <Stack.Screen name="Agenda" component={AgendaScreen} />
      </Stack.Navigator>
  );
}
