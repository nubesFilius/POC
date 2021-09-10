import React, {useReducer} from 'react';
import {View, Text, StyleSheet, Button} from 'react-native';

const COUNTER_INCREMENT = 1;

const reducer = (state, action) => {
  // state === { counter : number }
  // action === { type: "increase_counter" || "decrease_counter" , payload: number}
    
  switch(action.type) {
    case "increase_counter":
      return {...state, counter: state.counter + action.payload};
    case "decrease_counter":
      return {...state, counter: state.counter - action.payload};
  }
}

const CounterScreen = () => {

  const [state, dispatch] = useReducer(reducer, {counter: 0} )

  return (
    <View>
      <Button title="Increase" onPress={() => {
        dispatch({ type: "increase_counter", payload: COUNTER_INCREMENT});
      }} />
      <Button title="Decrease" onPress={() => {
        dispatch({ type: "decrease_counter", payload: COUNTER_INCREMENT});
      }}/>
      <Text>Current Count: {state.counter}</Text>
    </View>
  );
};

const styles = StyleSheet.create({});

export default CounterScreen;