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
  ImageBackground,
} from "react-native";
import { useNavigation, useLocalSearchParams } from "expo-router";
import { Ionicons } from "@expo/vector-icons"; // Adjust import based on your icon library
import AntDesign from "@expo/vector-icons/AntDesign";

const PromptForm = () => {
  const navigation = useNavigation();
  const [story, setStory] = useState("");
  const { name, age, type, subType } = useLocalSearchParams();

  return (
    <View style={styles.container}>
      <ImageBackground
        source={require("@/assets/images/2.png")}
        style={styles.image}
      >
        <View
          style={{
            height: "20%",
            width: "100%",
            padding: "5%",
            flexDirection: "row",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <AntDesign
            name="left"
            size={24}
            color="white"
            onPress={() => {
              navigation.goBack();
            }}
          />
          <Text
            style={{
              color: "white",
              fontFamily: "Tajawal_700Bold",
              fontSize: 20,
            }}
          >
            الخطوة ٣ من ٣
          </Text>
        </View>
        <Image source={require("@/assets/images/5.png")} style={styles.logo2} />
        <Text
          style={{
            alignSelf: "center",
            width: "70%",
            textAlign: "right",
            fontSize: 20,
            marginBottom: 10,
            color: "white",
            fontFamily: "Tajawal_400Regular",
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
          <Text
            style={{
              color: "white",
              fontSize: 20,
              textAlign: "center",
              fontFamily: "Tajawal_400Regular",
            }}
          >
            التالي
          </Text>
        </TouchableOpacity>
        <Image source={require("@/assets/images/4.png")} style={styles.logo} />
      </ImageBackground>
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
    width: "22%",
    height: "9%",
    alignSelf: "center",
    marginTop: "40%",
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
    alignSelf: "center",
    color: "white",
  },
  button: {
    backgroundColor: "#96308F",
    textDecorationColor: "white",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
    fontFamily: "Tajawal_400Regular",
    width: "30%",
    alignSelf: "center",
  },
  image: {
    height: "100%",
    width: "100%",
  },
  logo2: {
    width: "32%",
    height: "15%",
    marginLeft: "55%",
  },
});

export default PromptForm;
