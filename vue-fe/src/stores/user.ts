import { defineStore } from "pinia";
import axios from "axios";


interface UserState {
    isAuthenticated: boolean;
    id: string | null;
    name: string | null;
    email: string | null;
    access: string | null;
    refresh: string | null;
}
export const useUserStore = defineStore("user", {
   
    state: () =>  ({
        user: {
            isAuthenticated: false,
            id: null, 
            name: null,
            email: null,
            access: null,
            refresh: null,
        } as UserState
    }),
    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access');
                this.user.refresh = localStorage.getItem('user.refresh');
                this.user.id = localStorage.getItem('user.id');
                this.user.name = localStorage.getItem('user.name');
                this.user.email = localStorage.getItem('user.email');
                this.user.isAuthenticated = true;

                this.refresh();
                console.log("User store initialized with local storage data.", this.user);
            }
        },
        isAuthenticated() {
            return this.user.isAuthenticated;
        },
        setToken(data : UserState){
            console.log("Setting user token:", data);
            this.user.access = data.access;
            this.user.refresh = data.refresh;
            this.user.isAuthenticated = true;

            localStorage.setItem('user.access', data.access as string);
            localStorage.setItem('user.refresh', data.refresh as string);
        },
        removeToken() {
            console.log("Removing user token.");
            this.user.access = null;
            this.user.refresh = null;
            this.user.isAuthenticated = false;
            this.user.id = null
            this.user.name = null;
            this.user.email = null;

            localStorage.removeItem('user.id');
            localStorage.removeItem('user.name');
            localStorage.removeItem('user.email');
            localStorage.removeItem('user.access');
            localStorage.removeItem('user.refresh');
        },
        setUserInfo(user: UserState) {
            console.log("Setting user info:", user);
            this.user.id = user.id;
            this.user.name = user.name;
            this.user.email = user.email;

            localStorage.setItem('user.id', this.user.id as string);
            localStorage.setItem('user.name', this.user.name as string);
            localStorage.setItem('user.email', this.user.email as string);
        },
        async refresh() {
            try {
                const result = await axios.post('/api/refresh/', {
                    refresh: this.user.refresh
                });
                this.user.access = result.data.access;
                localStorage.setItem('user.access', this.user.access as string);
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.user.access}`;
                console.log("Token refreshed successfully:", this.user.access);
            } catch (error) {
                console.error("Failed to refresh token:", error);
                this.removeToken();
                // Optionally, you can notify the user here using a notification system
            }
        }
    }
})