// LoginForm.js
import React, { useState } from "react";
import {
  View,
  TextInput,
  Button,
  StyleSheet,
  Image,
  TouchableOpacity,
  Text,
} from "react-native";
import { useNavigation } from "expo-router";
import { Ionicons } from "@expo/vector-icons"; // Adjust import based on your icon library

const LoginForm = () => {
  const navigation = useNavigation();
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  const handleSubmit = () => {
    // Handle form submission here, e.g., send data to a server
    console.log("Name:", name);
    console.log("Age:", age);
  };

  return (
    <View style={styles.container}>
      <Image
        source={require("@/assets/images/back2.png")}
        style={styles.backLogo}
      />
      <Text
        style={{
          alignSelf: "center",
          width: "70%",
          textAlign: "right",
          fontSize: 20,
          marginTop: 50,
          marginBottom: 10,
          color: "#0A2074",
        }}
      >
        أدخل إسمك :
      </Text>
      <TextInput
        style={styles.input}
        placeholder=""
        onChangeText={setName}
        value={name}
      />
      <Text
        style={{
          alignSelf: "center",
          width: "70%",
          textAlign: "right",
          fontSize: 20,
          marginVertical: 10,
          color: "#0A2074",
        }}
      >
        أدخل عمرك :
      </Text>
      <TextInput
        style={styles.input}
        placeholder=""
        onChangeText={setAge}
        value={age}
        keyboardType="numeric"
      />
      <TouchableOpacity
        style={styles.button}
        onPress={() =>
          navigation.navigate("category", { name: name, age: age })
        }
      >
        <Text style={{ color: "white", fontSize: 20 }}>التالي</Text>
      </TouchableOpacity>
      <Image
        source={require("@/assets/images/allamStory.png")}
        style={styles.logo}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    backgroundColor: "white",
  },
  logo: {
    width: "40%",
    height: "20%",
  },
  backLogo: {
    width: "100%",
    height: "15%",
    opacity: 0.8,
    borderRadius: 20,
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 10,
    marginBottom: 10,
    width: "70%",
    borderRadius: 10,
  },
  button: {
    backgroundColor: "#96308F",
    textDecorationColor: "white",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
  },
});

export default LoginForm;
