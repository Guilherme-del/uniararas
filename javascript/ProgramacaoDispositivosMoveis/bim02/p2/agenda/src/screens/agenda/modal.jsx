// ModalComponent.js
import React from 'react';
import { View, ScrollView, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';
import Modal from 'react-native-modal';

const ModalComponent = ({ isVisible, selectedItem, closeModal, saveNotes, setSelectedItem }) => {
  return (
    <Modal isVisible={isVisible} style={styles.modal}>
      <ScrollView contentContainerStyle={styles.scrollViewContent}>
        <View style={styles.modalContainer}>
          <TextInput
            style={styles.input}
            placeholder="Enter notes"
            multiline
            placeholderTextColor="gray"
            value={selectedItem?.notes}
            onChangeText={(text) => selectedItem && setSelectedItem({ ...selectedItem, notes: text })}
          />
          <View style={styles.buttonContainer}>
            <TouchableOpacity style={styles.button} onPress={() => selectedItem && saveNotes(selectedItem?.notes)}>
              <Text style={styles.buttonText}>Save</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={() => closeModal()}>
              <Text style={styles.buttonText}>Cancel</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modal: {
    justifyContent: 'center',
    alignItems: 'center',
    margin: 0,
  },
  scrollViewContent: {
    flexGrow: 1,
    justifyContent: 'center',
    marginBottom: 300,
  },
  modalContainer: {
    backgroundColor: 'white',
    padding: 22,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 4,
    borderColor: 'rgba(0, 0, 0, 0.1)',
  },
  input: {
    textAlign: 'left',
    color: 'black',
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
    width: 100,
  },
  buttonText: {
    color: 'white',
    textAlign: 'center',
  },
});

export default ModalComponent;
