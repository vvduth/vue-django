<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import Feed from "./components/Feed.vue";
import Toast from "./components/Toast.vue";
</script>

<template>
  <Navbar />
  <main class="px-8 py-6 ">
    <RouterView />
    <Toast />
  </main>
</template>

<style scoped></style>
