import React from 'react';
import {View, Text, StyleSheet, FlatList} from 'react-native';

const ListScreen = () => {
  const friends = [
    { name: "Friend 1", age: 20},
    { name: "Friend 2", age: 21},
    { name: "Friend 3", age: 22},
    { name: "Friend 4", age: 23},
    { name: "Friend 5", age: 24},
    { name: "Friend 6", age: 25},
    { name: "Friend 7", age: 26},
  ];

  // return <Text>My Awe..wait 4 it...List</Text>
  return (
  <FlatList
    // horizontal -> sets the list to scroll horizontally
    // showsHorizontalScrollIndicator = {false} -> to hide the horizontal scroll bar
    keyExtractor = { (friend) => friend.name }
    data={friends}
    renderItem={( {item} ) => {
      // If we used (element) we'd access the object like this:   element == { item : { name: 'Friend #1' }, index: 0 }
      // if we used ( {item} ) we'd access the object like this: item == { name: 'Friend #1' }
      // we have to return something
      return <Text style={styles.textStyle}>{item.name} - Age {item.age}</Text>
    }}
  />);
};

const styles = StyleSheet.create({
  textStyle: {
    marginVertical: 50
  }
});

export default ListScreen;