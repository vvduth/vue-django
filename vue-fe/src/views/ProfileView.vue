<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

        <p><strong>{{ user?.name || 'Loading...' }}</strong></p>

        <div class="mt-6 flex space-x-8 justify-around">
          <RouterLink
            :to="`/profile/${route.params.id}/friends`"
          class="text-xs text-gray-500">{{ user?.friends_count }} friends</RouterLink>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>
        <div class="mt-6">
          <button class="w-full bg-sky-700 text-white text-xs py-2 rounded-lg"
                  @click="addFriend">
          
            Add friend
          </button>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <template v-for="post in userPosts" :key="post.id">
        <PostItem :post="post" />
      </template>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";
import Trends from "@/components/Trends.vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import {  useRouter } from "vue-router";
import type { User } from "@/types";
import type { Post } from "@/types";
import { useRoute } from "vue-router";
import PostItem from "@/components/PostItem.vue";

const userStore = useUserStore();

const userPosts = ref<Post[]>([]);
const user = ref<User|null>(null)
const route = useRoute()




const getUserPost = async () => {
  try {
    const userId = route.params.id;
    const response = await axios.get(`/api/posts/profile/${userId}/`);
    if (response.status !== 200) {
      throw new Error("Failed to fetch user posts");
    }
    
    userPosts.value = response.data.posts;
    user.value = response.data.user;
  } catch (error) {
    console.error("Error fetching user posts:", error);
  }
}

const addFriend = async () => {
  try {
    const addFriendRes = await axios.post(`/api/friends/${route.params.id}/request/`)
    // user.value = addFriendRes.data.user;
  } catch (error) {
    console.error("Error adding friend:", error); 
  }
}

watch(
  () => route.params.id,
  (newId, oldId) => {
    if (newId && newId !== oldId) {
      getUserPost();
    }
  },
  { immediate: true } // This will run immediately when component mounts
);

</script>
