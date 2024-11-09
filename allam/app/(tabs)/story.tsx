import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  Image,
  TouchableOpacity,
  TouchableHighlight,
  ScrollView,
  ImageBackground,
  ActivityIndicator,
} from "react-native";
import { useNavigation, useLocalSearchParams } from "expo-router";
import { Audio } from "expo-av";
import AntDesign from "@expo/vector-icons/AntDesign";
import axios from "axios";

const LoadingScreen = () => {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <ActivityIndicator size="large" color="#0000ff" />
    </View>
  );
};
interface ResponseData {
  story: string;
}

const StoryScreen = () => {
  const navigation = useNavigation();
  const [sound, setSound] = useState<Audio.Sound | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const { name, age, type, subType, story } = useLocalSearchParams();
  const apiUrl = "http://127.0.0.1:3000/process_json";
  const [response, setResponse] = useState<ResponseData | null>(null);

  useEffect(() => {
    console.log({
      type: type,
      subType: subType,
      story: story,
      name: name,
      age: age,
    });
    async function fetchData() {
      try {
        const result = await axios.post<ResponseData>(apiUrl, {
          type: type,
          subType: subType,
          story: story,
          name: name,
          age: parseInt(age),
        });
        console.log(result.data);
        setResponse(result.data);
        setIsLoading(false);
      } catch (error) {
        console.error("Error calling the API:", error);
        setResponse(null);
      }
    }
    fetchData();
    return () => {
      if (sound) {
        sound.unloadAsync();
      }
    };
  }, [sound]);

  const handlePlayPause = async () => {
    if (sound) {
      if (isPlaying) {
        await sound.pauseAsync();
      } else {
        await sound.playAsync();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleBackToHome = () => {
    navigation.navigate("index");
  };

  return (
    <View style={{ flex: 1 }}>
      {isLoading ? (
        <LoadingScreen />
      ) : (
        <View
          style={{
            flex: 1,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <ImageBackground
            source={require("@/assets/images/2.png")}
            style={styles.image}
          >
            <Image
              source={require("@/assets/images/story.jpg")}
              style={styles.storyImage}
            />
            <Text
              style={{
                fontSize: 25,
                height: "5%",
                fontWeight: "bold",
                color: "white",
                fontFamily: "Tajawal_700Bold",
                textAlign: "center",
              }}
            >
              Back to Home
            </Text>
            <ScrollView
              style={{
                height: "20%",
                overflow: "scroll",
              }}
            >
              <Text style={styles.storyText}>{story}</Text>
            </ScrollView>
            <View style={styles.buttonContainer}>
              <TouchableOpacity
                style={styles.button}
                onPress={handleBackToHome}
              >
                <AntDesign
                  name="download"
                  size={24}
                  color="white"
                  style={{ alignSelf: "center" }}
                />
              </TouchableOpacity>
              <TouchableOpacity
                style={{ ...styles.button, width: "30%", height: "40%" }}
                onPress={handlePlayPause}
              >
                {isPlaying ? (
                  <AntDesign
                    name="pause"
                    size={50}
                    color="white"
                    style={{ alignItems: "center" }}
                  />
                ) : (
                  <AntDesign
                    name="caretright"
                    size={50}
                    color="white"
                    style={{ alignSelf: "center" }}
                  />
                )}
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.button}
                onPress={handleBackToHome}
              >
                <AntDesign
                  name="home"
                  size={24}
                  color="white"
                  style={{ alignSelf: "center" }}
                />
              </TouchableOpacity>
            </View>
          </ImageBackground>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  storyImage: {
    width: "100%",
    height: "30%",
    marginBottom: 20,
    borderBottomEndRadius: 30,
    borderBottomStartRadius: 30,
  },
  storyText: {
    fontSize: 25,
    textAlign: "center",
    marginBottom: 20,
    color: "white",
    fontFamily: "Tajawal_400Regular",
  },
  buttonContainer: {
    flexDirection: "row",
    alignSelf: "center",
    justifyContent: "space-between",
    width: "100%",
    height: "30%",
    paddingHorizontal: "5%",
  },
  button: {
    backgroundColor: "#96308F",
    borderRadius: 50,
    height: "30%",
    alignItems: "center",
    alignSelf: "center",
    alignContent: "center",
    padding: "6%",
    width: "20%",
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
    alignSelf: "center",
  },
  image: {
    height: "100%",
    width: "100%",
  },
});

export default StoryScreen;
