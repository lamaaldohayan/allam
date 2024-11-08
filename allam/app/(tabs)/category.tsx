import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity, Image } from "react-native";
import { useNavigation, useLocalSearchParams } from "expo-router";

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
      <Image
        source={require("@/assets/images/back2.png")}
        style={styles.backLogo}
      />

      <Text style={styles.title}>أختر نوع القصة :</Text>

      {options.map((option) => (
        <TouchableOpacity
          key={option.label}
          style={[
            styles.option,
            selectedOption === option ? styles.selectedOption : null,
          ]}
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
    alignContent: "center",
    alignItems: "center",
    backgroundColor: "white",
  },

  title: {
    fontSize: 20,
    marginBottom: 20,
    marginTop: 20,
    fontWeight: "bold",
  },

  option: {
    padding: 10,
    borderWidth: 1,
    borderColor: "#96308F",
    marginBottom: 10,
    borderRadius: 50,
    width: "70%",
  },

  selectedOption: {
    backgroundColor: "#96308F",
  },

  optionText: {
    fontSize: 18,
    textAlign: "center",
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
    fontWeight: "bold",
  },

  logo: {
    width: "40%",
    height: "20%",
  },
  backLogo: {
    width: "100%",
    height: "15%",
    opacity: 0.8,
  },
});

const options: Option[] = [
  { label: "إسلامية" },
  { label: "تعليمية" },
  { label: "خيالية" },
  { label: "واقعية" },
  { label: "حضارات و تراث السعودية" },
];

export default RadioOptionScreen;
