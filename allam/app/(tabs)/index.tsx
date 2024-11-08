import {
  Image,
  StyleSheet,
  Platform,
  TouchableOpacity,
  Text,
  ImageBackground,
  View,
} from "react-native";

import { HelloWave } from "@/components/HelloWave";
import ParallaxScrollView from "@/components/ParallaxScrollView";
import { ThemedText } from "@/components/ThemedText";
import { ThemedView } from "@/components/ThemedView";
import { useNavigation } from "expo-router";
import React, { useState } from "react";
import { RotateInDownLeft } from "react-native-reanimated";
import axios from "axios";

// Define the shape of the data you're sending
interface RequestData {
  data: string;
}

// Define the shape of the response data you're expecting
interface ResponseData {
  story: string;
}

export default function HomeScreen() {
  const navigation = useNavigation();
  const [data, setData] = useState<string>(""); // Type for data as string
  const [response, setResponse] = useState<ResponseData | null>(null); // Type for response

  // API URL (change to your actual local IP address if using a physical device)
  const apiUrl = "http://127.0.0.1:5000/process_json"; // Localhost for emulator

  // Function to handle the form submission and make the API call
  const handleSubmit = async () => {
    console.log("hi");
    try {
      // Make the POST request to the API
      const result = await axios.post<ResponseData>(apiUrl, {
        data: "اسمي خالد عمري 10 سنوات قصص خياليه  أدخل عمر الطفل: 10 احكي لي عن سبايدر مان القصة موجهة للأطفال بعمر 8-10. نهاية القصة يجب أن تكون مفتوحة. عدد الشخصيات في القصة يجب أن يكون 3. تجري الأحداث في مملكة خيالية.  القصة يجب أن تكون باللغة العربية الفصحى وموجهة للأطفال.",
      });

      // Store the response in the state
      console.log(result.data);
      setResponse(result.data);
    } catch (error) {
      // Handle error
      console.error("Error calling the API:", error);
      setResponse(null);
    }
  };

  return (
    <View
      style={{
        flex: 1,
        backgroundColor: "white",
      }}
    >
      <Image
        source={require("@/assets/images/back2.png")}
        style={styles.backLogo}
      />
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
          source={require("@/assets/images/allamStory.png")}
          style={styles.reactLogo}
        />
        <TouchableOpacity style={styles.button} onPress={() => handleSubmit()}>
          <Text style={{ color: "white", fontSize: 20 }}>إبدأ !</Text>
        </TouchableOpacity>
      </View>
      <Image
        source={require("@/assets/images/back2.png")}
        style={{
          ...styles.backLogo,
          transform: [{ scaleY: -1 }],
          position: "absolute",
          bottom: 0,
        }}
      />
    </View>
  );
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
    height: "40%",
    width: "60%",
    alignSelf: "center",
    alignItems: "center",
    alignContent: "center",
  },
  backLogo: {
    width: "100%",
    height: "15%",
    opacity: 0.8,
    borderRadius: 20,
  },
  button: {
    alignSelf: "center",
    backgroundColor: "#96308F",
    padding: 15,
    borderRadius: 20,
  },
});
