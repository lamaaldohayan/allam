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
import { useNavigation, useLocalSearchParams } from "expo-router";
import { Ionicons } from "@expo/vector-icons"; // Adjust import based on your icon library

const PromptForm = () => {
  const navigation = useNavigation();
  const [story, setStory] = useState("");
  const { name, age, type, subType } = useLocalSearchParams();

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
        أدخل وصف قصير للقصة :
      </Text>
      <TextInput
        editable
        multiline
        numberOfLines={4}
        maxLength={40}
        style={styles.input}
        placeholder=""
        onChangeText={setStory}
        value={story}
      />
      <TouchableOpacity
        style={styles.button}
        onPress={() =>
          navigation.navigate("story", {
            name: name,
            age: age,
            type: type,
            subType: subType,
            story: story,
          })
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
    height: "20%",
    borderRadius: 10,
    textAlign: "right",
  },
  button: {
    backgroundColor: "#96308F",
    textDecorationColor: "white",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
  },
});

export default PromptForm;
