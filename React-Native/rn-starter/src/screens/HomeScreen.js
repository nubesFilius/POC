import React from "react";
import { Text, StyleSheet, View, Button, TouchableOpacity } from "react-native";

const HomeScreen = ({ navigation }) => {
  return (
    <View> 
      <Text style={styles.text}>React Native POC</Text>
      <Button 
        onPress={() => navigation.navigate('Components')}
        title="My views below"/>
      {/* <TouchableOpacity onPress={() => navigation.navigate("List")}>
        <Text>Take me to List view</Text>
      </TouchableOpacity> */}
      <Button 
        onPress={() => navigation.navigate('Image')}
        title="Go to Images"/>
      <Button 
        onPress={() => navigation.navigate('Counter')}
        title="Go to Counter"/>
      <Button 
        onPress={() => navigation.navigate('Color')}
        title="Go to Color"/>
      <Button 
        onPress={() => navigation.navigate('Square')}
        title="Go to Square"/>
      <Button 
        onPress={() => navigation.navigate('Text')}
        title="Go to Text"/>
      <Button 
        onPress={() => navigation.navigate('Box')}
        title="Go to Box"/>
    </View>
  );  
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30
  }
});

export default HomeScreen;
