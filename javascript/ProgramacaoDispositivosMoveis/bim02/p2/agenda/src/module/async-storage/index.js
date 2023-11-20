import AsyncStorage from '@react-native-async-storage/async-storage';

export const storeData = async (value) => {
  try {
    const jsonValue = JSON.stringify(value);
    await AsyncStorage.setItem('date-values', jsonValue);
  } catch (e) {
    // saving error
  }
};

export const getData = async () => {
  try {
    const value = await AsyncStorage.getItem('date-values');
    if (value !== null) {
      return JSON.parse(value);
    }
  } catch (e) {
    // error reading value
  }
};