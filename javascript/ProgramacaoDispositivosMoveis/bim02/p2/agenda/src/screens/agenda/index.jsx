import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { Agenda } from 'react-native-calendars';
import ModalComponent from '../../components/modal';
import Toast from 'react-native-toast-message';
//modules & components
import { storeData, getData } from '../../module/async-storage';
import { showToast, toastConfig } from '../../components/toastConfig/toastify';

const AgendaScreen = () => {
  const [items, setItems] = useState({});
  const [selectedItem, setSelectedItem] = useState(null);
  const [isModalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    loadItems({ timestamp: Date.now() });
  }, []);

  const generateNewItems = (day, count) => {
    const newItems = {};
    for (let i = 0; i <= count; i++) {
      const time = day.timestamp + i * 24 * 60 * 60 * 1000;
      const strTime = timeToString(time);
      if (!newItems[strTime]) {
        newItems[strTime] = Array.from(
          { length: 1 },
          (_, j) => ({
            height: 50,
            timestamp: strTime,
            name: `Item for ${strTime} #${j}`,
            notes: '',
          })
        );
      }
    }
    return newItems;
  };

  const loadItems = async (day) => {
    //await AsyncStorage.clear();
    const data = await getData();
    if (!data || Object.keys(data).length === 0) {
      // No data or empty data, generate new items for the next 30 days
      setItems(generateNewItems(day, 31));
      return;
    }
    const keys = Object.keys(data);
    const firstDate = keys[0];
    const todayStr = timeToString(new Date().getTime());
    if (firstDate === todayStr) {
      setItems(data);
    }
    else {
      const todayStr = timeToString(new Date().getTime());
      const todayIndex = keys.indexOf(todayStr);
      if (todayIndex === -1) {
        const newItems = generateNewItems(day, 31);
        setItems(newItems);
        return;
      }
      else {
        const slicedKeys = keys.slice(todayIndex - 1);
        const lastDay = slicedKeys[slicedKeys.length - 1];
        const startDate = new Date(lastDay);
        // Add x days
        startDate.setDate(startDate.getDate() + todayIndex - 1);
        const newDateString = timeToString(startDate.getTime());
        const dateObject = new Date(newDateString);
        const timestamp = dateObject.getTime();
        // If the first date is not today, generate new items for the remaining days  
        const daysNeeded = 31 - slicedKeys.length;
        // I want to slice the data object to remove the date from slicedKeys before passing it to newItems variable; 
        // Get the keys (dates) and remove the first three
        if (daysNeeded <= 1) {
          var keysToRemove = Object.keys(data).slice(0, 1);
          var additionalItems = generateNewItems({ timestamp: timestamp }, 1);
        }
        else {
          var keysToRemove = Object.keys(data).slice(0, daysNeeded);
          var additionalItems = generateNewItems({ timestamp: timestamp }, daysNeeded);
        }
        keysToRemove.forEach(key => {
          delete data[key];
        });

        const newItems = { ...data };
        // Generate new items for the remaining days and add them to the newItems object
        Object.entries(additionalItems).forEach(([date, items]) => {
          if (newItems[date] === undefined) {
            newItems[date] = items;
          }
        });
        setItems(newItems);
      }
    }
  };

  const renderItem = (item) => {
    return (
      <TouchableOpacity
        style={[styles.item, { height: item.height }]}
        onPress={() => {
          try {
            setModalVisible(true);
          }
          finally {
            setSelectedItem(item);
          }
        }}
      >
        <Text style={styles.text}>
          {item.notes == "" ? "No activities" : item.notes}
        </Text>
      </TouchableOpacity>
    );
  };

  const timeToString = (time) => {
    const date = new Date(time);
    return date.toISOString().split('T')[0];
  };

  const saveNotes = async (newNotes) => {
    setModalVisible(false);
    showToast("success", "Succes", `Task saved to the following date: ${selectedItem.timestamp}`);
    setItems((prevItems) => {
      const newItems = { ...prevItems };

      const strTime = timeToString(selectedItem.timestamp);
      const updatedItem = {
        ...selectedItem,
        notes: newNotes,
      };

      newItems[strTime] = (newItems[strTime] || []).map((item) =>
        item.name === selectedItem.name ? updatedItem : item
      );

      storeData(newItems);
      return newItems;
    });
  };

  return (
    <View style={{ flex: 1 }}>
      <ModalComponent
        isVisible={isModalVisible}
        setSelectedItem={setSelectedItem}
        selectedItem={selectedItem}
        closeModal={() => setModalVisible(false)}
        saveNotes={saveNotes}
      />
      <Agenda
        items={items}
        renderItem={renderItem}
        loadItemsForMonth={() => loadItems}
        markingType={'period'}
        monthFormat={'mm'}
        theme={{ calendarBackground: '#F8F8FF', selectedDayTextColor: '#ADD8E6' }}
        hideExtraDays={false}
      />
      <Toast config={toastConfig} />
    </View>
  );
};

const styles = StyleSheet.create({
  item: {
    backgroundColor: 'white',
    flex: 1,
    borderRadius: 5,
    padding: 10,
    marginRight: 10,
    marginTop: 17,
  },
  text: {
    textAlign: 'center',
    fontSize: 15,
    color: 'black'
  },
  emptyDate: {
    height: 15,
    flex: 1,
    paddingTop: 30,
  },
  modalContent: {
    backgroundColor: 'white',
    padding: 22,
    justifyContent: 'flex-start',
    alignItems: 'center',
    borderRadius: 4,
    borderColor: 'rgba(0, 0, 0, 0.1)',
  },
  input: {
    color: 'black',
    height: 100,
    width: 300,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    padding: 8,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: 20,
  },
  button: {
    padding: 10,
    backgroundColor: 'blue',
    borderRadius: 5,
    marginRight: 10,
  },
  buttonText: {
    color: 'white',
    textAlign: 'center',
  },
});

export default AgendaScreen;
