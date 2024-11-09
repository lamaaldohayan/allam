import {
  Image,
  StyleSheet,
  TouchableOpacity,
  ImageBackground,
  View,
} from "react-native";
import AntDesign from "@expo/vector-icons/AntDesign";
import { useNavigation } from "expo-router";
import React, { useState } from "react";
import axios from "axios";
import AppLoading from "expo-app-loading";
import {
  useFonts,
  Tajawal_200ExtraLight,
  Tajawal_300Light,
  Tajawal_400Regular,
  Tajawal_500Medium,
  Tajawal_700Bold,
  Tajawal_800ExtraBold,
  Tajawal_900Black,
} from "@expo-google-fonts/tajawal";
interface RequestData {
  data: string;
}
interface ResponseData {
  story: string;
}

export default function HomeScreen() {
  let [fontsLoaded] = useFonts({
    Tajawal_200ExtraLight,
    Tajawal_300Light,
    Tajawal_400Regular,
    Tajawal_500Medium,
    Tajawal_700Bold,
    Tajawal_800ExtraBold,
    Tajawal_900Black,
  });
  const navigation = useNavigation();
  const [data, setData] = useState<string>("");
  const [response, setResponse] = useState<ResponseData | null>(null);

  // API URL (change to your actual local IP address if using a physical device)
  const apiUrl = "http://127.0.0.1:5000/process_json"; // Localhost for emulator

  // Function to handle the form submission and make the API call
  const handleSubmit = async () => {
    navigation.navigate("explore");
  };

  if (!fontsLoaded) {
    return <AppLoading />;
  } else {
    return (
      <View
        style={{
          flex: 1,
        }}
      >
        <ImageBackground
          source={require("@/assets/images/3.png")}
          style={styles.image}
        >
          <View
            style={{
              height: "69%",
              borderRadius: 10,
              shadowColor: "black",
              shadowOpacity: 0.2,
              shadowRadius: 10,
              shadowOffset: {
                width: 2,
                height: 2,
              },
            }}
          >
            <Image
              source={require("@/assets/images/logoAllam.png")}
              style={styles.reactLogo}
            />
            <TouchableOpacity
              style={styles.button}
              onPress={() => handleSubmit()}
            >
              <AntDesign name="caretright" size={30} color="white" />
            </TouchableOpacity>
          </View>
        </ImageBackground>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: "25%",
    width: "77%",
    marginTop: "20%",
    alignSelf: "center",
  },
  backLogo: {
    width: "100%",
    height: "15%",
    opacity: 0.8,
    borderRadius: 20,
  },
  button: {
    alignSelf: "center",
    backgroundColor: "#762271",
    padding: 15,
    borderRadius: 20,
    marginTop: "10%",
  },
  image: {
    height: "100%",
    width: "100%",
  },
});
