import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Image,
  ImageBackground,
} from "react-native";
import { useNavigation, useLocalSearchParams } from "expo-router";
import AntDesign from "@expo/vector-icons/AntDesign";

interface Option {
  label: string;
}

const RadioOptionScreen: React.FC = () => {
  const navigation = useNavigation();
  const { name, age } = useLocalSearchParams();
  const [selectedOption, setSelectedOption] = useState<Option | null>(null);

  const handleOptionSelect = (option: Option) => {
    setSelectedOption(option);
  };

  const handleSubmit = () => {
    if (selectedOption) {
      if (selectedOption.label === "إسلامية") {
        navigation.navigate("subCategory", {
          name: name,
          age: age,
          type: "إسلامية",
        });
      } else {
        navigation.navigate("prompt", {
          name: name,
          age: age,
          type: selectedOption.label,
          subType: "بدون",
        });
      }
    } else {
      // Optional: Handle the case where no option is selected
      console.warn("Please select an option before submitting.");
    }
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
        <Text style={styles.title}>أختر نوع القصة :</Text>

        {options.map((option, index) => (
          <TouchableOpacity
            key={option.label}
            style={{
              ...styles.option,
              ...(selectedOption === option ? styles.selectedOption : null),
            }}
            onPress={() => handleOptionSelect(option)}
          >
            <Text
              style={[
                styles.optionText,
                selectedOption === option ? styles.selectedOptionText : null,
              ]}
            >
              {option.label}
            </Text>
          </TouchableOpacity>
        ))}

        <TouchableOpacity style={styles.submitButton} onPress={handleSubmit}>
          <Text style={styles.submitButtonText}>التالي</Text>
        </TouchableOpacity>
        <Image source={require("@/assets/images/4.png")} style={styles.logo} />
      </ImageBackground>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignContent: "center",
    alignItems: "center",
    backgroundColor: "white",
  },

  title: {
    fontSize: 20,
    marginBottom: 20,
    marginTop: 20,
    fontWeight: "bold",
    textAlign: "right",
    color: "white",
    fontFamily: "Tajawal_400Regular",
  },

  option: {
    padding: 10,
    borderWidth: 1,
    borderColor: "#96308F",
    marginBottom: 10,
    borderRadius: 50,
    width: "70%",
    alignSelf: "center",
  },

  selectedOption: {
    backgroundColor: "#96308F",
  },

  optionText: {
    fontSize: 18,
    textAlign: "center",
    color: "white",
    fontFamily: "Tajawal_400Regular",
  },

  selectedOptionText: { fontSize: 16, color: "white" },

  submitButton: {
    backgroundColor: "#0A2074",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
    width: "30%",
    alignSelf: "center",
  },

  submitButtonText: {
    color: "white",
    textAlign: "center",
    fontFamily: "Tajawal_400Regular",
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
  image2: {
    height: "10%",
    width: "100%",
  },
  btnText: {
    color: "white",
    fontSize: 20,
    textAlign: "center",
    fontFamily: "Tajawal_400Regular",
  },
});

const options: Option[] = [
  { label: "إسلامية" },
  { label: "تعليمية" },
  { label: "خيالية" },
  { label: "واقعية" },
  { label: "حضارات و تراث السعودية" },
];
const images: Option[] = [
  { label: "@/assets/images/11.png" },
  { label: "@/assets/images/12.png" },
  { label: "@/assets/images/13.png" },
  { label: "@/assets/images/14.png" },
  { label: "@/assets/images/15.png" },
];

export default RadioOptionScreen;
