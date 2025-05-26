<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-2">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Login</h1>

        <p class="mb-6 text-gray-500">
          Login to your account to access your dashboard and manage your preferences.
        </p>

        <p class="font-bold">
          Already have an account? <RouterLink to="/signup" class="underline">Click here</RouterLink> to log in!
        </p>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div>
            <label>E-mail</label><br />
            <input v-model="form.email" type="email" placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>


          <div>
            <label>Password</label><br />
            <input v-model="form.password" type="password" placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>



          <div>
            <button type="submit" class="py-4 px-6 bg-sky-600 text-white rounded-lg">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import { ref } from 'vue';
const toastStore = useToastStore();

const form = ref({
  email: '',
  password: ''
});

const errors = ref<string[]>([]);

const submitForm = async () => {
  errors.value = [];

  if (!form.value.email || !form.value.password) {
    errors.value.push('All fields are required');
    return;
  }




  if (errors.value.length === 0) {
    try {
      const response = await axios.post('/api/login/', {
        email: form.value.email,

        password: form.value.password,

      });
      if (response.status === 201) {

        console.log('Log in successful:', response.data);
        toastStore.showToast(
          5000,
          'Log in successful!',
          'bg-green-500'
        );

        form.value = {
          email: '',
          password: ''
        };
      } else {
        console.error('Log in failed:', response.data);
        toastStore.showToast(
          5000,
          'Log in failed. Please try again.',
          'bg-red-500'
        );
      }
    } catch (error) {
      toastStore.showToast(
        5000,
        'An error occurred during Log in. Please try again later.',
        'bg-red-500'
      );
      console.error('Error during Log in:', error);

    }
  }
};</script>