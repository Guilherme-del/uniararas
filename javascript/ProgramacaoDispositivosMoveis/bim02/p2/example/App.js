import React, { Component, useState } from 'react';
import { StyleSheet, Text, View, ScrollView, Dimensions, Image, TouchableHighlight, SafeAreaView, Modal, Alert, SectionList, StatusBar } from 'react-native';
import AsyncStorage from '@react-native-community/async-storage'

//import the_data from './data/test_data.json'; //Test data in a json file that can be imported into the app for testing purposes

const deviceWidth = Dimensions.get('window').width;
const STATUS_BAR = StatusBar.statusBarHeight || 24;

//Shows the day of the week at the top of the screen 
function DateText({ day, current }) {
  //Underline the current date only - need to change to something more visually appealing
  let underline = "none"

  if (current) {
    underline = "underline"

  }
  return (
    <View style={{
      backgroundColor: '#ffffff',
      shadowColor: '#000000',
      shadowOffset: { width: 1, height: 1 },
      shadowOpacity: 0.4,
      shadowRadius: 3,
      elevation: 5,
    }}>

      <Text style={{
        fontSize: 30,
        textAlign: "center",
        margin: 0,
        color: 'black',
        fontWeight: "bold",
        marginTop: STATUS_BAR,
        padding: 10,
        textDecorationLine: underline,
      }}>{day}</Text>

    </View>
  );
}


//A horizontal line that will be used to divide the day into hours
function GridLine({ time, left }) {
  return (
    <View
      style={{
        borderBottomColor: '#E8E8E8',
        borderBottomWidth: 1,
        marginVertical: time,
        marginLeft: left,
        position: 'absolute',
        width: '100%'
      }} />
  );
}


//Text that shows an hour of the day
function Time({ time }) {
  return (
    <View style={styles.time}>
      <View
        style={{
          marginTop: (60) - 10,
          marginLeft: '15%',
          position: 'absolute',
        }}>
        <Text style={{ color: "#606060" }}>{time}</Text>
      </View>
    </View>


  );
}

//TRY REWRITING TO USE FEWER LINES
//The grid of horizontal lines and times - could perhaps add a AM/PM option in future
function TimeLabels() {
  return (
    <View style={styles.timelabels}>
      <GridLine time={60} left={'80%'} />
      <Time time="01:00" />
      <Time time="" />
    </View>
  );
}

//TRY REWRITING TO USE FEWER LINES
//The grid that goes behind the day items
function DayGrid() {
  return (
    <View>
      <GridLine time={60} />
    </View>
  );

}


//A vertical line that separates the two halves of the grid
function VerticalLine() {
  return (
    <View
      style={{
        borderLeftColor: '#E8E8E8',
        borderLeftWidth: 1,
        position: 'absolute',
        height: '100%'
      }}
    />
  );

}

//A line that indicates the current time of day
function CurrentTimeLine() {
  return (
    <View>
      <View
        style={{
          backgroundColor: 'black',
          height: 1,
          marginTop: currentTime,
          marginLeft: 0,
          position: 'absolute',
          width: '100%',
        }}
      />

      <View style={{
        backgroundColor: 'black',
        height: 11,
        width: 11,
        alignItems: 'center',
        position: 'absolute',
        marginTop: currentTime - 5,
        marginLeft: -5,
        borderRadius: 50
      }} />
    </View>
  );
}


//Currently this adds a new event to Monday - a menu to set the features of the event needs to be added
function AddEvent({ addFunction }) {
  const [modalVisible, setModalVisible] = useState(false);
  return (
    <View style={styles.addButton}>
      <TouchableHighlight style={{
        backgroundColor: 'white',
        borderColor: 'white',
        borderWidth: 0,
        height: 60,
        width: 60,
        borderRadius: 50,
        alignItems: 'center',
        justifyContent: 'center',
        position: 'absolute',
      }}
        underlayColor='#f8f8f8' delayPressIn={0} onPress={() => { addFunction(); setModalVisible(!modalVisible); }}>
        <Image source={require('./assets/add.png')}
          style={styles.FloatingButtonStyle} />
      </TouchableHighlight>

      <Modal
        animationType="slide"
        transparent={true}
        statusBarTranslucent={true}
        visible={modalVisible}
        onRequestClose={() => {
          setModalVisible(!modalVisible);

        }}
      >
        <View style={{
          alignSelf: 'center',
          marginTop: '30%',
          width: '80%',
          height: '70%',
          backgroundColor: '#ffffff',
          shadowColor: '#000000',
          shadowOffset: { width: 1, height: 1 },
          shadowOpacity: 0.4,
          shadowRadius: 3,
          elevation: 5,
          borderRadius: 10,
          justifyContent: 'center',
          alignItems: 'center'
        }}>
          <Text style={{
            textAlign: "center",
            fontSize: 14,
          }}>This will eventually become a menu to add a new item. Currently the add button just creates a new event on Monday.</Text>
        </View>
      </Modal>
    </View>
  );

}




//The detail that appears when a day item is clicked on - needs to be changed so that each day item can have it's own details - needs to be stored with the other info
const DETAIL = [
  { title: 'To Do', data: ['Assignment One | due 24/8', 'Read Lecture 4 Notes', 'Read Textbook Chapter 2'] },
  { title: 'Notes', data: ['Lecture 1', 'Lecture 2', 'Lecture 3', 'Tutorial 1'] },
];


function DayItem({ day, item_key, content, start_h, start_m, end_h, end_m, bgColour, detail, removeEvent }) {
  const [modalVisible, setModalVisible] = useState(false);
  detail = DETAIL; //Need to change this to be passed at the creation of the item (and presumably eventually put it in the state)
  //The header for the item detail
  function Header({ title }) {
    return (
      <Text style={{
        paddingTop: 2,
        paddingLeft: 10,
        paddingRight: 10,
        paddingBottom: 2,
        fontSize: 14,
        fontWeight: 'bold',
        backgroundColor: 'rgba(247,247,247,1.0)',
      }}>{title}</Text>
    );
  }

  //An item in the list of details
  function Item({ title, type }) {

    if (type === "Notes") {
      return (
        <View style={{}}>

          <Text style={{
            padding: 10,
            fontSize: 18,
            color: 'black'
          }}>{title}
          </Text>

        </View>
      );
    } else {
      return (
        <View style={{
          borderColor: 'black', borderWidth: 0,
          flex: 1,
          flexDirection: 'row'
        }}>

          <View style={{ borderColor: 'black', borderWidth: 1, width: 18, height: 18, marginLeft: 10, alignSelf: 'center', borderRadius: 4 }}></View>

          <Text style={{
            padding: 10,
            marginRight: 30,
            fontSize: 18,
          }}>{title}
          </Text>

        </View>
      );
    }

  }

  //A dividing line between items
  function Line() {
    return (
      <View
        style={{
          height: 1,
          width: "100%",
          backgroundColor: "#E8E8E8",
        }}
      />
    );
  }





  return (
    <View
      style={{
        marginTop: 60 * start_h + start_m,
        marginLeft: 0,
        position: 'absolute',
        width: '100%',
        borderRadius: 4,
        overflow: 'hidden'
      }}
    >

      <Modal //The modal that shows the details when the day item is clicked
        animationType="slide"
        transparent={true}
        statusBarTranslucent={true}
        visible={modalVisible}
        onRequestClose={() => {
          setModalVisible(!modalVisible);

        }}
      >



        <View style={styles.centeredView}>

          <View style={{ width: deviceWidth, height: 90 + STATUS_BAR }}>

            <TouchableHighlight //The button to close the modal
              underlayColor="#f8f8f8"
              style={styles.closeButton}
              delayPressIn={0}
              onPress={() => {
                setModalVisible(!modalVisible);
              }}
            >
              <Image source={require('./assets/close.png')}
                style={{

                  resizeMode: 'contain',
                  width: 50,
                  height: 50,
                }} />
            </TouchableHighlight>

            <TouchableHighlight //The button to edit the details - still needs to be implemented and change the image
              underlayColor="#f8f8f8"
              style={styles.editButton}
              delayPressIn={0}
              onPress={() => {
                alert("Pressed edit");

              }}
            >
              <Image source={require('./assets/edit.png')}
                style={{

                  resizeMode: 'contain',
                  width: 30,
                  height: 30,
                }} />
            </TouchableHighlight>

            <TouchableHighlight //The button to delete the event - need to change the image
              underlayColor="#f8f8f8"
              style={styles.deleteButton}
              delayPressIn={0}
              onPress={() => {
                Alert.alert(
                  "Delete",
                  "Are you sure you would like to delete this event?",
                  [
                    {
                      text: "Cancel",
                      onPress: () => console.log("Cancel Pressed"),
                      style: "cancel"
                    },
                    { text: "OK", onPress: () => removeEvent(day, item_key) }
                  ],
                  { cancelable: false }
                );

              }}
            >
              <Image source={require('./assets/delete.png')}
                style={{

                  resizeMode: 'contain',
                  width: 30,
                  height: 30,
                }} />
            </TouchableHighlight>

          </View>

          <SafeAreaView style={{
            flex: 1,
            marginTop: 0,
            marginHorizontal: 16
          }}>
            <SectionList //The list of details for the item
              sections={detail}
              renderItem={({ item, section }) => <Item title={item} type={section.title} />}
              renderSectionHeader={({ section }) => <Header title={section.title} />}
              keyExtractor={(item, index) => index}
              ItemSeparatorComponent={Line}
            />
          </SafeAreaView>



        </View>
      </Modal>



      <TouchableHighlight //The day item that is shown on the grid
        activeOpacity={0.6}
        underlayColor="#ffffff"
        delayPressIn={0}
        onPress={() => {
          setModalVisible(true);
        }}>
        <View style={styles.item} backgroundColor={bgColour} height={60 * (end_h - start_h) + (end_m - start_m)}>
          <Text style={styles.title}>{content}</Text>
        </View>
      </TouchableHighlight>
    </View>
  );


}


//Get the current day and time
let minutes = new Date().getMinutes();
let hours = new Date().getHours();
let currentDay = new Date().getDay();
let currentTime = hours * 60 + minutes;

//Make Sunday have the correct index to be at the end of the list
if (currentDay === 0) {
  currentDay = 7;
}


export default class App extends Component {

  constructor(props) {
    super(props);
    this.removeEvent = this.removeEvent.bind(this);
    this.addNew = this.addNew.bind(this);
    this.state = {
      showSplash: true,
      name: '',
      day_data: [],
      all_data: [],
      mon_data: [],
      tue_data: [],
      wed_data: [],
      thu_data: [],
      fri_data: [],
      sat_data: [],
      sun_data: [],
    }
  }

  componentDidMount = () => this.loadData()

  //Load all of the data from storage and create day items for all the events
  async loadData() {
    await AsyncStorage.getItem('day_data').then((value) => this.setState({ 'day_data': value }))

    let data = JSON.parse(this.state.day_data);

    this.setState({ all_data: data, });

    //REWRITE THIS SECTION AS A FUNCTION?
    let monday_data = [];

    for (let i = 0; i < this.state.all_data[0]["events"].length; i++) {
      monday_data.push(
        <View key={this.state.all_data[0]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[0]["day"]} item_key={this.state.all_data[0]["events"][i]["key"]} content={this.state.all_data[0]["events"][i]["title"]} start_h={this.state.all_data[0]["events"][i]["start_time_h"]} start_m={this.state.all_data[0]["events"][i]["start_time_m"]} end_h={this.state.all_data[0]["events"][i]["end_time_h"]} end_m={this.state.all_data[0]["events"][i]["end_time_m"]} bgColour={this.state.all_data[0]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ mon_data: monday_data, });


    let tuesday_data = [];

    for (let i = 0; i < this.state.all_data[1]["events"].length; i++) {
      tuesday_data.push(
        <View key={this.state.all_data[1]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[1]["day"]} item_key={this.state.all_data[1]["events"][i]["key"]} content={this.state.all_data[1]["events"][i]["title"]} start_h={this.state.all_data[1]["events"][i]["start_time_h"]} start_m={this.state.all_data[1]["events"][i]["start_time_m"]} end_h={this.state.all_data[1]["events"][i]["end_time_h"]} end_m={this.state.all_data[1]["events"][i]["end_time_m"]} bgColour={this.state.all_data[1]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ tue_data: tuesday_data, });


    let wednesday_data = [];

    for (let i = 0; i < this.state.all_data[2]["events"].length; i++) {
      wednesday_data.push(
        <View key={this.state.all_data[2]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[2]["day"]} item_key={this.state.all_data[2]["events"][i]["key"]} content={this.state.all_data[2]["events"][i]["title"]} start_h={this.state.all_data[2]["events"][i]["start_time_h"]} start_m={this.state.all_data[2]["events"][i]["start_time_m"]} end_h={this.state.all_data[2]["events"][i]["end_time_h"]} end_m={this.state.all_data[2]["events"][i]["end_time_m"]} bgColour={this.state.all_data[2]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ wed_data: wednesday_data, });


    let thursday_data = [];

    for (let i = 0; i < this.state.all_data[3]["events"].length; i++) {
      thursday_data.push(
        <View key={this.state.all_data[3]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[3]["day"]} item_key={this.state.all_data[3]["events"][i]["key"]} content={this.state.all_data[3]["events"][i]["title"]} start_h={this.state.all_data[3]["events"][i]["start_time_h"]} start_m={this.state.all_data[3]["events"][i]["start_time_m"]} end_h={this.state.all_data[3]["events"][i]["end_time_h"]} end_m={this.state.all_data[3]["events"][i]["end_time_m"]} bgColour={this.state.all_data[3]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ thu_data: thursday_data, });


    let friday_data = [];

    for (let i = 0; i < this.state.all_data[4]["events"].length; i++) {
      friday_data.push(
        <View key={this.state.all_data[4]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[4]["day"]} item_key={this.state.all_data[4]["events"][i]["key"]} content={this.state.all_data[4]["events"][i]["title"]} start_h={this.state.all_data[4]["events"][i]["start_time_h"]} start_m={this.state.all_data[4]["events"][i]["start_time_m"]} end_h={this.state.all_data[4]["events"][i]["end_time_h"]} end_m={this.state.all_data[4]["events"][i]["end_time_m"]} bgColour={this.state.all_data[4]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ fri_data: friday_data, });


    let saturday_data = [];

    for (let i = 0; i < this.state.all_data[5]["events"].length; i++) {
      saturday_data.push(
        <View key={this.state.all_data[5]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[5]["day"]} item_key={this.state.all_data[5]["events"][i]["key"]} content={this.state.all_data[5]["events"][i]["title"]} start_h={this.state.all_data[5]["events"][i]["start_time_h"]} start_m={this.state.all_data[5]["events"][i]["start_time_m"]} end_h={this.state.all_data[5]["events"][i]["end_time_h"]} end_m={this.state.all_data[5]["events"][i]["end_time_m"]} bgColour={this.state.all_data[5]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ sat_data: saturday_data, });


    let sunday_data = [];

    for (let i = 0; i < this.state.all_data[6]["events"].length; i++) {
      sunday_data.push(
        <View key={this.state.all_data[6]["events"][i]["key"]}>
          <DayItem day={this.state.all_data[6]["day"]} item_key={this.state.all_data[6]["events"][i]["key"]} content={this.state.all_data[6]["events"][i]["title"]} start_h={this.state.all_data[6]["events"][i]["start_time_h"]} start_m={this.state.all_data[6]["events"][i]["start_time_m"]} end_h={this.state.all_data[6]["events"][i]["end_time_h"]} end_m={this.state.all_data[6]["events"][i]["end_time_m"]} bgColour={this.state.all_data[6]["events"][i]["colour"]} removeEvent={this.removeEvent} />
        </View>
      );
    }

    this.setState({ sun_data: sunday_data, });

  }

  //Save the data to storage
  saveData = (value) => {
    AsyncStorage.setItem('day_data', value);
    this.setState({ 'day_data': value });
  }

  //Remove the splash screen after a few seconds
  fadeOut() {
    setTimeout(() => {
      this.removeView();
    }, 1000);
  }

  //Remove the splash screen
  removeView() {
    this.setState({
      showSplash: false,
    });
  }

  //Scroll the current date to have the current time near the top, other days start at 7:30am
  scrollDate() {
    this.mondayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.tuesdayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.wednesdayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.thursdayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.fridayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.saturdayScrollView.scrollTo({ y: 60 * 7.5, animated: false })
    this.sundayScrollView.scrollTo({ y: 60 * 7.5, animated: false })

    switch (currentDay) {
      case 1:
        this.mondayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 2:
        this.tuesdayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 3:
        this.wednesdayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 4:
        this.thursdayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 5:
        this.fridayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 6:
        this.saturdayScrollView.scrollTo({ y: 60 * (hours), animated: false })
        break;
      case 7:
        this.sundayScrollView.scrollTo({ y: 60 * (hours), animated: false })
    }

  }

  //Add a new day item - currently this defaults to adding a new Monday event, need to change once the detail modal is complete
  addNew() {
    this.state.all_data[0]["events"].push({
      "key": 3,
      "title": "TEST4",
      "start_time_h": 9,
      "start_time_m": 0,
      "end_time_h": 10,
      "end_time_m": 45,
      "colour": "pink"

    })

    let monday_data = [...this.state.mon_data];

    monday_data.push(
      <View key={3}>
        <DayItem day={"Monday"} item_key={3} content={"TEST4"} start_h={9} start_m={0} end_h={10} end_m={45} bgColour={"pink"} removeEvent={this.removeEvent} />
      </View>
    );

    this.setState({ mon_data: monday_data, });

    this.setState({ all_data: this.state.all_data, });

    //Uncomment the below line to PERMANENTLY SAVE THE DATA
    //this.saveData(JSON.stringify(this.state.all_data));
  }

  //Remove an event from a given day using it's key
  removeEvent(day, key) {

    let modified_array = [];
    let modified_day = [];

    //Could probably do this better - maybe using reflection?
    switch (day) {
      case "Monday":
        modified_array = this.state.all_data[0]["events"].filter(o => o.key !== key);
        this.state.all_data[0]["events"] = modified_array;

        modified_day = this.state.mon_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ mon_data: modified_day, });
        break;
      case "Tuesday":
        modified_array = this.state.all_data[1]["events"].filter(o => o.key !== key);
        this.state.all_data[1]["events"] = modified_array;

        modified_day = this.state.tue_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ tue_data: modified_day, });
        break;
      case "Wednesday":
        modified_array = this.state.all_data[2]["events"].filter(o => o.key !== key);
        this.state.all_data[2]["events"] = modified_array;

        modified_day = this.state.wed_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ wed_data: modified_day, });
        break;
      case "Thursday":
        modified_array = this.state.all_data[3]["events"].filter(o => o.key !== key);
        this.state.all_data[3]["events"] = modified_array;

        modified_day = this.state.thu_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ thu_data: modified_day, });
        break;
      case "Friday":
        modified_array = this.state.all_data[4]["events"].filter(o => o.key !== key);
        this.state.all_data[4]["events"] = modified_array;

        modified_day = this.state.fri_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ fri_data: modified_day, });
        break;
      case "Saturday":
        modified_array = this.state.all_data[5]["events"].filter(o => o.key !== key);
        this.state.all_data[5]["events"] = modified_array;

        modified_day = this.state.sat_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ sat_data: modified_day, });
        break;
      case "Sunday":
        modified_array = this.state.all_data[6]["events"].filter(o => o.key !== key);
        this.state.all_data[6]["events"] = modified_array;

        modified_day = this.state.sun_data.filter(o => o.props.children.props.item_key !== key);
        this.setState({ sun_data: modified_day, });
    }

    this.setState({ all_data: this.state.all_data, });

    //Uncomment the below line to PERMANENTLY SAVE THE DATA
    //this.saveData(JSON.stringify(this.state.all_data));
  }



  render() {

    //Put everything together to display, could possibly turn each day into a function of it's own to save lines?
    return (
      <View style={styles.maincontainer}>



        {this.state.showSplash && (
          <StatusBar translucent={true} />
        )}

        {!this.state.showSplash && (
          <StatusBar backgroundColor="white" translucent={true} barStyle="dark-content" />
        )}


        <ScrollView horizontal={true} pagingEnabled={true} showsHorizontalScrollIndicator={false} ref={ref => { this.dayScrollView = ref }} onContentSizeChange={() => this.dayScrollView.scrollTo({ x: (currentDay - 1) * deviceWidth, animated: false })}>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="MONDAY" current={currentDay == 1} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.mondayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.mon_data}

                    {currentDay === 1 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="TUESDAY" current={currentDay == 2} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.tuesdayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.tue_data}

                    {currentDay === 2 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="WEDNESDAY" current={currentDay == 3} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.wednesdayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.wed_data}

                    {currentDay === 3 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="THURSDAY" current={currentDay == 4} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.thursdayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.thu_data}

                    {currentDay === 4 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="FRIDAY" current={currentDay == 5} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.fridayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.fri_data}

                    {currentDay === 5 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="SATURDAY" current={currentDay == 6} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.saturdayScrollView = ref }}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.sat_data}

                    {currentDay === 6 && (<CurrentTimeLine />)}

                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

          <View style={styles.dayView}>
            <View style={{ flex: 1 }}>
              <DateText day="SUNDAY" current={currentDay == 7} />

              <ScrollView showsVerticalScrollIndicator={false} ref={ref => { this.sundayScrollView = ref }} onLayout={() => this.scrollDate()}>
                <View style={styles.daycontainer}>

                  <TimeLabels />

                  <View style={styles.daygrid}>

                    <DayGrid />
                    <VerticalLine />

                    {this.state.sun_data}

                    {currentDay === 7 && (<CurrentTimeLine />)}


                  </View>

                </View>
              </ScrollView>

            </View>
          </View>

        </ScrollView>



        <AddEvent addFunction={this.addNew}></AddEvent>



        {this.state.showSplash && (
          <View style={{ position: 'absolute', backgroundColor: 'royalblue', width: '100%', height: '100%', elevation: 9 }} ref={ref => { this.splashScreen = ref }} onLayout={() => this.fadeOut()}>
            <Text style={{ color: 'white', fontSize: 40, fontWeight: 'bold', textAlign: 'center', marginVertical: '50%' }}>AGENDA</Text>
          </View>
        )}



      </View>
    );
  }
}


//StyleSheet
const styles = StyleSheet.create({
  maincontainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#e5e5e5",
  },
  dayView: {
    width: deviceWidth,
    backgroundColor: '#ffffff',
    justifyContent: 'center',
    alignItems: 'baseline',
    flexDirection: 'row',
    flex: 1,
  },
  item: {
    padding: 0,
    marginVertical: 0,
    marginHorizontal: 0,
    marginLeft: 0,
    marginBottom: 0,
    borderRadius: 4,
  },
  title: {
    fontSize: 12,
    textAlign: "left",
    margin: 6,
    color: 'white',
    fontWeight: "bold",
    flex: 1,
  },

  daycontainer: {
    flex: 1,
    flexDirection: 'row',
    flexWrap: 'wrap',
    alignItems: 'flex-start'
  },
  timelabels: {
    flex: 0.2,
    flexDirection: 'column',
    flexWrap: 'wrap',
    alignItems: 'flex-start',
  },
  daygrid: {
    flex: 0.8,
    flexDirection: 'column',
    flexWrap: 'wrap',
    alignItems: 'flex-start'
  },
  time: {
    width: '100%',
    height: 60,
    marginLeft: 5,
  },


  FloatingButtonStyle: {
    resizeMode: 'contain',
    width: 50,
    height: 50,
  },


  centeredView: {
    flex: 1,
    backgroundColor: 'white',
  },


  addButton: {
    backgroundColor: 'white',
    borderColor: 'white',
    borderWidth: 0,
    height: 60,
    width: 60,
    borderRadius: 50,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    bottom: 20,
    right: 20,
    shadowColor: "#000000",
    shadowOpacity: 0.8,
    shadowRadius: 2,
    shadowOffset: {
      height: 1,
      width: 0
    },
    elevation: 6
  },

  //Clean up duplicates
  closeButton: {
    backgroundColor: 'white',
    borderColor: 'black',
    borderWidth: 0,
    height: 50,
    width: 50,
    borderRadius: 5,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    top: 20 + STATUS_BAR,
    left: 20,
    shadowColor: "#000000",
    shadowOpacity: 0.8,
    shadowRadius: 2,
    shadowOffset: {
      height: 1,
      width: 0
    },
    elevation: 6,
  },

  editButton: {
    backgroundColor: 'white',
    borderColor: 'black',
    borderWidth: 0,
    height: 50,
    width: 50,
    borderRadius: 5,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    top: 20 + STATUS_BAR,
    right: 90,
    shadowColor: "#000000",
    shadowOpacity: 0.8,
    shadowRadius: 2,
    shadowOffset: {
      height: 1,
      width: 0
    },
    elevation: 6,
  },

  deleteButton: {
    backgroundColor: 'white',
    borderColor: 'black',
    borderWidth: 0,
    height: 50,
    width: 50,
    borderRadius: 5,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    top: 20 + STATUS_BAR,
    right: 20,
    shadowColor: "#000000",
    shadowOpacity: 0.8,
    shadowRadius: 2,
    shadowOffset: {
      height: 1,
      width: 0
    },
    elevation: 6,
  },
});