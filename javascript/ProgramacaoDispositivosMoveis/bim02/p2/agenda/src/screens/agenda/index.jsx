// AgendaScreen.js
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import { Agenda } from 'react-native-calendars';
import ModalComponent from './modal';

const AgendaScreen = () => {
  const [items, setItems] = useState({});
  const [selectedItem, setSelectedItem] = useState(null);
  const [isModalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    loadItems({ timestamp: Date.now() });
  }, []);

  const loadItems = (day) => {
    if (Object.keys(items).length === 0) {
      const newItems = {};
      for (let i = -15; i <= 30; i++) {
        const time = day.timestamp + i * 24 * 60 * 60 * 1000;
        const strTime = timeToString(time);
        if (!newItems[strTime]) {
          newItems[strTime] = Array.from(
            { length: 1 },
            (_, j) => ({
              height: 50,
              timestamp: strTime,
              name: `Item for ${strTime} #${j}`,
              notes: ``,
            })
          );
        }
      }

      setItems(newItems);
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
          {item.notes == "" ? "No activities" : item.notes }
        </Text>
      </TouchableOpacity>
    );
  };

  const timeToString = (time) => {
    const date = new Date(time);
    return date.toISOString().split('T')[0];
  };

  const saveNotes = (newNotes) => {
    try {
      setModalVisible(false);
    } finally {
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

        return newItems;
      });
    }
  };

  return (
    <View style={{ flex: 1 }}>
      <Agenda
        items={items}
        renderItem={renderItem}
        loadItemsForMonth={() => loadItems}
        markingType={'period'}
        monthFormat={'mm'}
        theme={{ calendarBackground: '#F8F8FF', selectedDayTextColor: '#ADD8E6' }}
        hideExtraDays={false}
      />

      <ModalComponent
        isVisible={isModalVisible}
        setSelectedItem={setSelectedItem}
        selectedItem={selectedItem}
        closeModal={() => setModalVisible(false)}
        saveNotes={saveNotes}
      />

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
    fontSize: 20,
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
