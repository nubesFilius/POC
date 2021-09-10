import React from 'react';
import {Text, StyleSheet, View} from 'react-native';

const ComponentsScreen = () => {
  const greeting = "HEY!"
  const myAwesomeGreeting = <Text>Because you're smart</Text>


  return (
    <View>
      <Text style={styles.textStyle}>Because you get me</Text>
      {myAwesomeGreeting}
      <Text style={styles.textStyle}>Because you're beautiful</Text>
      <Text style={styles.textStyle}>Because I'm glad you're the mother of my son</Text>
    </View>
    );
};

const styles = StyleSheet.create({
  textStyle: {
    fontSize: 30
  }
});

export default ComponentsScreen;