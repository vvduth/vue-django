import { defineStore } from "pinia";
import axios from "axios";


interface UserState {
    isAuthenticated: boolean;
    id: string | null;
    name: string | null;
    email: string | null;
    accessToken: string | null;
    refreshToken: string | null;
}
export const useUserStore = defineStore("user", {
   
    state: () =>  ({
        user: {
            isAuthenticated: false,
            id: null, 
            name: null,
            email: null,
            accessToken: null,
            refreshToken: null,
        } as UserState
    }),
    actions: {
        initStore() {
            if (localStorage.getItem('user.accessToken')) {
                this.user.accessToken = localStorage.getItem('user.accessToken');
                this.user.refreshToken = localStorage.getItem('user.refreshToken');
                this.user.id = localStorage.getItem('user.id');
                this.user.name = localStorage.getItem('user.name');
                this.user.email = localStorage.getItem('user.email');
                this.user.isAuthenticated = true;

                this.refreshToken();
                console.log("User store initialized with local storage data.", this.user);
            }
        },
        setToken(data : UserState){
            console.log("Setting user token:", data);
            this.user.accessToken = data.accessToken;
            this.user.refreshToken = data.refreshToken;
            this.user.isAuthenticated = true;

            localStorage.setItem('user.accessToken', data.accessToken as string);
            localStorage.setItem('user.refreshToken', data.refreshToken as string);
        },
        removeToken() {
            console.log("Removing user token.");
            this.user.accessToken = null;
            this.user.refreshToken = null;
            this.user.isAuthenticated = false;
            this.user.id = null
            this.user.name = null;
            this.user.email = null;

            localStorage.removeItem('user.id');
            localStorage.removeItem('user.name');
            localStorage.removeItem('user.email');
            localStorage.removeItem('user.accessToken');
            localStorage.removeItem('user.refreshToken');
        },
        setUserInfo(user: UserState) {
            console.log("Setting user info:", user);
            this.user.id = user.id;
            this.user.name = user.name;
            this.user.email = user.email;

            localStorage.setItem('this.user.id', this.user.id as string);
            localStorage.setItem('this.user.name', this.user.name as string);
            localStorage.setItem('this.user.email', this.user.email as string);
        },
        async refreshToken() {
            try {
                const result = await axios.post('/api/account/refresh/', {
                    refresh: this.user.refreshToken
                });
                this.user.accessToken = result.data.access;
                localStorage.setItem('user.accessToken', this.user.accessToken as string);
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.user.accessToken}`;
                console.log("Token refreshed successfully:", this.user.accessToken);
            } catch (error) {
                console.error("Failed to refresh token:", error);
                this.removeToken();
                // Optionally, you can notify the user here using a notification system
            }
        }
    }
})