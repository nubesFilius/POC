import React, {useState} from 'react';
import {Text, StyleSheet, View, TextInput} from 'react-native';

const TextScreen = () => {
  const [text, setText] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View>
      <Text>Enter whatever you want here:</Text>
      <TextInput 
        style={styles.input}
        autoCapitalize = "none"
        autoCorrect = {false}
        value = {text}
        onChangeText = {(newValue) => {setText(newValue)}}
      />
      <Text>My cool text from above right here: {text}</Text>
      <View>
        <Text>
        </Text>
      </View>
      <Text>Enter a password to test</Text>
      <TextInput 
        style={styles.input}
        autoCapitalize = "none"
        autoCorrect = {false}
        value = {password}
        onChangeText = {(newPassword) => {setPassword(newPassword)}}
      />
      { password.length > 15 
        ? <Text>Your password length is gtg</Text>
        : <Text>Your password is too short</Text>
      }
    </View>
    );
};

const styles = StyleSheet.create({
  input: {
    margin: 15,
    borderColor: 'black',
    borderWidth: 1
  }
});

export default TextScreen;