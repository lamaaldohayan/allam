// LoginForm.js
import React, { useState } from "react";
import {
  View,
  TextInput,
  Button,
  StyleSheet,
  Image,
  TouchableOpacity,
  ImageBackground,
  Text,
} from "react-native";
import { useNavigation } from "expo-router";
import AntDesign from "@expo/vector-icons/AntDesign";

const LoginForm = () => {
  const navigation = useNavigation();
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  const handleSubmit = () => {
    console.log("Name:", name);
    console.log("Age:", age);
  };

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
            الخطوة ١ من ٣
          </Text>
        </View>
        <Image source={require("@/assets/images/9.png")} style={styles.logo2} />
        <Text
          style={{
            fontFamily: "Tajawal_400Regular",
            alignSelf: "center",
            width: "70%",
            textAlign: "right",
            fontSize: 20,
            marginTop: "5%",
            marginBottom: "5%",
            color: "white",
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
            fontFamily: "Tajawal_400Regular",
            alignSelf: "center",
            width: "70%",
            textAlign: "right",
            fontSize: 20,
            marginVertical: 10,
            color: "white",
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
          <Text style={styles.btnText}>التالي</Text>
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
  logo2: {
    width: "50%",
    height: "17%",
    marginLeft: "40%",
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
    alignSelf: "center",
    textAlign: "right",
  },
  button: {
    backgroundColor: "#96308F",
    textDecorationColor: "white",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
    width: "30%",
    alignSelf: "center",
  },
  image: {
    height: "100%",
    width: "100%",
  },
  btnText: {
    color: "white",
    fontSize: 20,
    textAlign: "center",
    fontFamily: "Tajawal_400Regular",
  },
});

export default LoginForm;
