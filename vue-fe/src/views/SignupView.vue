<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-2">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Sign up</h1>

        <p class="mb-6 text-gray-500">
          Create a new account to access your dashboard and manage your
          preferences. If you already have an account, you can log in instead.
        </p>

        <p class="font-bold">
          Already have an account?
          <RouterLink to="/login" class="underline">Click here</RouterLink> to
          log in!
        </p>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div>
            <label>E-mail</label><br />
            <input type="email" placeholder="Your e-mail address" v-model="form.email"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>
          <div>
            <label>Name</label><br />
            <input type="text" v-model="form.name" placeholder="Your name"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>

          <div>
            <label>Password</label><br />
            <input type="password" placeholder="Your password" v-model="form.password1"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>

          <div>
            <label>Confirm password</label><br />
            <input type="password" v-model="form.password2" placeholder="Confirm your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>

          <div>
            <button type="submit" class="py-4 px-6 bg-sky-600 text-white rounded-lg">
              Sign up
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
  name: '',
  password1: '',
  password2: ''
});

const errors = ref<string[]>([]);

const submitForm = async () => {
  errors.value = [];

  if (!form.value.email || !form.value.name || !form.value.password1 || !form.value.password2) {
    errors.value.push('All fields are required');
    return;
  }
  if (form.value.password1 !== form.value.password2) {
    errors.value.push('Passwords do not match');
    return;
  }



  if (errors.value.length === 0) {
    try {
      const response = await axios.post('/api/signup/', {
        email: form.value.email,
        name: form.value.name,
        password1: form.value.password1,
        password2: form.value.password2
      });
      if (response.status === 201) {

        console.log('Signup successful:', response.data);
        toastStore.showToast(
          5000,
          'Signup successful! Please check your email to confirm your account.',
          'bg-green-500'
        );

        form.value = {
          email: '',
          name: '',
          password1: '',
          password2: ''
        };
      } else {
        console.error('Signup failed:', response.data);
        toastStore.showToast(
          5000,
          'Signup failed. Please try again.',
          'bg-red-500'
        );
      }
    } catch (error) {
      toastStore.showToast(
        5000,
        'An error occurred during signup. Please try again later.',
        'bg-red-500'
      );
      console.error('Error during signup:', error);

    }
  }
};
</script>
