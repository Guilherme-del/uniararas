import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import MenuScreen from './src/screens/menu';
import CalendarsScreen from './src/screens/calendars';
import AgendaScreen from './src/screens/agenda';
import CalendarsList from './src/screens/calendarsList';
import HorizontalCalendarList from './src/screens/horizontalCalendarList';
import ExpandableCalendar from './src/screens/expandableCalendar';
import TimelineCalendar from './src/screens/timelineCalendar';

export default function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Menu">
        <Stack.Screen name="Menu" component={MenuScreen} />
        <Stack.Screen name="Calendars" component={CalendarsScreen} />
        <Stack.Screen name="Agenda" component={AgendaScreen} />
        <Stack.Screen name="CalendarsList" component={CalendarsList} />
        <Stack.Screen name="HorizontalCalendarList" component={HorizontalCalendarList} />
        <Stack.Screen name="ExpandableCalendar" component={ExpandableCalendar} />
        <Stack.Screen name="TimelineCalendar" component={TimelineCalendar} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
