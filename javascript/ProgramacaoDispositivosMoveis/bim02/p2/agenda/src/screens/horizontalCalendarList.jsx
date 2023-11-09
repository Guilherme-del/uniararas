import React, {useState} from 'react';
// @ts-expect-error
import {CalendarList} from 'react-native-calendars';

const initialDate = '2020-05-16';

const HorizontalCalendarList = () => {
  const [selected, setSelected] = useState(initialDate);
  const markedDates = {
    [selected]: {
      selected: true,
      selectedColor: '#DFA460',
    },
  };

  const onDayPress = day => {
    setSelected(day.dateString);
  };

  return (
    <CalendarList
      markedDates={markedDates}
      current={initialDate}
      pastScrollRange={24}
      futureScrollRange={24}
      horizontal
      pagingEnabled
      onDayPress={onDayPress}
    />
  );
};

export default HorizontalCalendarList;