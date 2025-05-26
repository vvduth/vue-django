<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import Feed from "./components/Feed.vue";
import Toast from "./components/Toast.vue";
import { useUserStore } from "./stores/user";
import axios from "axios";
const userStore = useUserStore();
userStore.initStore();
const accessToken = userStore.user.access
if (accessToken) {
  axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
} else {
  axios.defaults.headers.common["Authorization"] = "";
}

</script>

<template>
  <Navbar />
  <main class="px-8 py-6 ">
    <RouterView />
    <Toast />
  </main>
</template>

<style scoped></style>
