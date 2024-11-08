import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
      }}
    >
      <Stack.Screen name="index" />
      <Stack.Screen name="explore" />
      <Stack.Screen name="category" />
      <Stack.Screen name="subCategory" />
      <Stack.Screen name="story" />
    </Stack>
  );
}
