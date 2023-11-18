import React, { useState, useEffect } from 'react';
import { Alert, StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import { Agenda } from 'react-native-calendars';
import Modal from 'react-native-modal';

const AgendaScreen = () => {
  const [items, setItems] = useState({});
  const [selectedItem, setSelectedItem] = useState(null);
  const [isModalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    loadItems({ timestamp: Date.now() });
  }, []);

  const loadItems = (day) => {
    setTimeout(() => {
      setItems((prevItems) => {
        const newItems = { ...prevItems };

        for (let i = -15; i <= 30; i++) {
          const time = day.timestamp + i * 24 * 60 * 60 * 1000;
          const strTime = timeToString(time);
          if (!newItems[strTime]) {
            newItems[strTime] = Array.from(
              { length: 1 },
              (_, j) => ({
                timestamp: strTime,
                name: `Item for ${strTime} #${j}`,
                height: 50,
                notes: ``,
              })
            );
          }
        }

        return newItems;
      });
    });
  };

  const renderItem = (item) => (
    <TouchableOpacity
      style={[styles.item, { height: item.height }]}
      onPress={() => {
        setSelectedItem(item);
        setModalVisible(true);
      }}>
      <Text>{item.name}</Text>
    </TouchableOpacity>
  );

  const renderEmptyDate = () => (
    <View style={styles.emptyDate}>
      <Text>This is an empty date!</Text>
    </View>
  );

  const rowHasChanged = (r1, r2) => r1.name !== r2.name;

  const timeToString = (time) => {
    const date = new Date(time);
    return date.toISOString().split('T')[0];
  };

  const closeModal = () => {
    setModalVisible(false);
  };

  const saveNotes = (newNotes) => {
    // Update the notes for the selected item in the state
    setItems((prevItems) => {
      const newItems = { ...prevItems };
      const strTime = timeToString(selectedItem.timestamp);
      const updatedItem = {
        ...selectedItem,
        notes: newNotes,
      };

      // Map over the existing items for the specified day and update the selected item
      newItems[strTime] = (newItems[strTime] || []).map((item) =>
        item.name === selectedItem.name ? updatedItem : item
      );
      console.log("newItems",newItems,"items",items)
      return newItems;
    });

    // Close the modal
    setModalVisible(false);
  };


  return (
    <View style={{ flex: 1 }}>
      <Agenda
        items={items}
        loadItemsForMonth={loadItems}
        renderItem={renderItem}
        renderEmptyDate={renderEmptyDate}
        rowHasChanged={rowHasChanged}
        showClosingKnob={true}
        markingType={'multi-period'}
        monthFormat={'yyyy'}
        theme={{ calendarBackground: '#F8F8FF', agendaKnobColor: 'none', selectedDayTextColor: '#ADD8E6' }}
        hideExtraDays={false}
      />

      <Modal isVisible={isModalVisible}>
        <View style={styles.modalContent}>
          <TextInput
            style={styles.input}
            placeholder="Enter notes"
            multiline
            placeholderTextColor="gray"
            value={selectedItem?.notes}
            onChangeText={(text) => setSelectedItem({ ...selectedItem, notes: text })}
          />
          <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={() => saveNotes(selectedItem?.notes)}>
              <Text style={styles.buttonText}>Save</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={closeModal}>
              <Text style={styles.buttonText}>Cancel</Text>
            </TouchableOpacity>     
          </View>
        </View>
      </Modal>
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
  emptyDate: {
    height: 15,
    flex: 1,
    paddingTop: 30,
  },
  modalContent: {
    backgroundColor: 'white',
    padding: 22,
    justifyContent: 'center',
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
