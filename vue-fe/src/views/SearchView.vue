<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="submitSearch" class="p-4 flex space-x-4">
          <input v-model="searchQuery" type="search" class="p-4 w-full bg-gray-100 rounded-lg"
            placeholder="What are you looking for?" />

          <button href="#" class="inline-block py-4 px-6 bg-sky-600 text-white rounded-lg">Search</button>
        </form>
      </div>

      <!-- user result -->
      <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
        <div class="p-4 text-center bg-gray-100 rounded-lg" v-for="user in searchResultsUsers" :key="user.id">

          <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

          <p><strong>
              <RouterLink :to="{ name: 'profile', params: { 'id': user.id } }">
                {{ user.name }}
              </RouterLink>
            </strong></p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>

      <!-- post result feed -->
      <div class="p-4 bg-white border border-gray-200 rounded-lg" 
      v-for="post in searchResultsPosts" 
      :key="post.id">

        <PostItem :post="post" />
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>

<script setup lang="ts">
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import PostItem from '@/components/PostItem.vue';
import Trends from '@/components/Trends.vue';
import type { Post, SerachResponse, User } from '@/types';
import axios from 'axios';
import { ref } from 'vue';
const searchQuery = ref('');
const searchResultsUsers = ref<User[]>([]);
const searchResultsPosts = ref<Post[]>([]);

const submitSearch = async (event: Event) => {

  event.preventDefault() // Optional since you're using .prevent

  if (!searchQuery.value.trim()) {
    return // Don't search with empty query
  }

  try {


    const res = await axios.post('/api/search/', {
      query: searchQuery.value
    }) as SerachResponse

    searchResultsUsers.value = res.data.users
    searchResultsPosts.value = res.data.posts

    console.log('Search results:', res.data)

  } catch (error) {
    console.error('Search failed:', error)
  }
}
</script>