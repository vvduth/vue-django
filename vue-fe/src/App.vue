<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <Navbar />
  <main class="px-8 py-6 ">
    <RouterView />
  </main>
</template>

<style scoped></style>
