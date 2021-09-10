import React from 'react';
import {Text, StyleSheet, View} from 'react-native';

const BoxScreen = () => {

  return (
    <View style={styles.viewStyle}>
      <Text style={styles.text1Style}>Child 1</Text>
      <Text style={styles.text2Style}>Child 2</Text>
      <Text style={styles.text3Style}>Child 3</Text>
    </View>
    );
};

const styles = StyleSheet.create({
  viewStyle: {
    borderWidth: 1,
    borderColor: 'black',

    // defaults to flexDirection: 'column
    // flexDirection: 'row'

    height: 200,

    // defaults to justifyContext: 'flex-start'
    // options: space-between || space-around || center || 
    // justifyContent: 'center'
  },
  text1Style: {
    borderWidth: 1,
    borderColor: 'red',

    // overrides all child items alignment with respect to parent.
    // alignItems: 'center',

    // defaults to position: 'relative'
    // options: 'absolute' || 'relative'
    // position: 'absolute'
  },
  text2Style: {
    borderWidth: 1,
    borderColor: 'red',

    // will expand based on flexDirection of parent element
    // will be allocated based on 100%. 1 == 10%.
    // flex: 1

    // add "margin" with respect to another element position. IF POSITION != absolute.
    // options: 'top', 'right', 'bottom', 'left'
    // top: 5

    // to fill a child to the parent container use .absoluteFillObject.
    // postion needs to be absolute and need to copy style (...Stylesheet)
    // position: 'absolute',
    // fontSize: 60,
    // ...StyleSheet.absoluteFillObject
  },
  text3Style: {
    borderWidth: 1,
    borderColor: 'red',

    // overrides alignment of child with respect to parent.
    // options: 'flex-start' || 'felx-end' || 'stretch'
    // alignSelf: 'flex-end'
  }
});

export default BoxScreen;