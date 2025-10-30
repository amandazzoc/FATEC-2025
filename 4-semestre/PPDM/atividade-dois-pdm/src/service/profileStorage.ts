import AsyncStorage from "@react-native-async-storage/async-storage";
import { UserProfile } from "../types/profile";

const PROFILE_KEY = "user_profile";

export class ProfileStorage {
    static async load(): Promise<UserProfile | null> {
        const data = await AsyncStorage.getItem(PROFILE_KEY);

        if (!data)
            return null;

        const profile: UserProfile = JSON.parse(data);
        return profile;
    }

    static async save(profile: UserProfile): Promise<void> {
        const data = JSON.stringify(profile);
        await AsyncStorage.setItem(PROFILE_KEY, data);
    }
}