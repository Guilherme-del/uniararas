import React, { useEffect, useState } from 'react';
import {
  ScrollView,
  View,
  TouchableOpacity,
  Text,
  Image,
  StyleSheet,
} from 'react-native';
import { useNavigation, useIsFocused } from '@react-navigation/native';
import { getData } from '../../module/async-storage';

const appIcon = require('../../img/app-icon-120x120.png');

function MenuScreen() {
  const isFocused = useIsFocused();
  const navigation = useNavigation();
  const pushScreen = (screen, props) => {
    navigation.navigate(screen, props);
  }

  const [textTobeShown, setTextTobeShown] = useState("No Tasks Scheduled");

  useEffect(() => {
    getData().then((jsonData) => {
      if (jsonData) {
        // Get today's date
        const todayDate = new Date().toISOString().split('T')[0];
        // Check if there's a non-empty item for today
        if (jsonData.hasOwnProperty(todayDate)) {
          const todayItems = jsonData[todayDate].filter(item => item.notes !== "");
          if (todayItems.length > 0) {
            setTextTobeShown(`Today's task is: ${todayItems[0].notes}`,)
          } else {
            // Find the closest non-empty item
            let nextDate = new Date(todayDate);
            let nextDateStr = nextDate.toISOString().split('T')[0];

            const allDates = Object.keys(jsonData);
            const sortedDates = allDates.sort();

            let index = sortedDates.indexOf(todayDate);

            while (index < sortedDates.length) {
              nextDateStr = sortedDates[index];

              if (jsonData[nextDateStr]) {
                const nextItems = jsonData[nextDateStr].filter(item => item.notes !== "");

                if (nextItems.length > 0) {
                  setTextTobeShown(`Nothing for today but ,your next task is: ${nextDateStr}, and you must do: ${nextItems[0].notes}`,)
                  break;
                }
              }

              index++;
            }

            if (index === sortedDates.length) {
              return;
            }
          }
        } else {
          // Find the closest non-empty item
          let nextDate = new Date(todayDate);
          let nextDateStr = nextDate.toISOString().split('T')[0];
          const allDates = Object.keys(jsonData);
          const sortedDates = allDates.sort();
          let index = sortedDates.indexOf(todayDate);
          while (index < sortedDates.length) {
            nextDateStr = sortedDates[index];
            if (jsonData[nextDateStr]) {
              const nextItems = jsonData[nextDateStr].filter(item => item.notes !== "");
              if (nextItems.length > 0) {
                setTextTobeShown(`Nothing for today but ,your next task is: ${nextDateStr}, and you must do: ${nextItems[0].notes}`,)
                break;
              }
            }
            index++;
          }
          if (index === sortedDates.length) {
            setTextTobeShown(`Relax mate , you have no task!`,)
          }
        }
      }
      else {
        setTextTobeShown(`Relax mate , you have no task!`,)
      }
    });
  }, [isFocused]);

  return (
    <ScrollView>
      <View style={styles.container}>
        <Image source={appIcon} style={styles.image} />
        <TouchableOpacity
          style={styles.menu}
          onPress={() => pushScreen('Agenda')}>
          <Text style={styles.menuText}>Agenda</Text>
        </TouchableOpacity>
        <View style={styles.panel}>
          <Text style={styles.panelText}> {textTobeShown}</Text>
        </View>
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
  panel: {
    width: 300,
    padding: 50,
    margin: 10,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#7a92a5',
    backgroundColor: '#e0e0e0', // Set background color as needed
  },
  panelText: {
    fontSize: 16,
    color: '#2d4150',
  },
});

export default MenuScreen;
