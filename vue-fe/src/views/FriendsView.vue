<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

        <p>
          <strong>{{ user?.name || "Loading..." }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">182 friends</p>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>
        <div class="mt-6">
          <button
            class="w-full bg-sky-700 text-white text-xs py-2 rounded-lg"
            @click="addFriend"
          >
            Add friend
          </button>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
      >
        <div
          class="p-4 text-center bg-gray-100 rounded-lg"
          v-for="user in userFriends"
          :key="user.id"
        >
          <img
            src="https://i.pravatar.cc/300?img=70"
            class="mb-6 rounded-full"
          />

          <p>
            <strong>
              <RouterLink :to="{ name: 'profile', params: { id: user.id } }">
                {{ user.name }}
              </RouterLink>
            </strong>
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
      <hr />
      <div
        v-if="friendShipRequests.length"
        class="p-4 bg-white border border-gray-200 rounded-lg grid"
      >
        <h2>Pending friendship request</h2>
        <div
          class="p-4 text-center bg-gray-100 rounded-lg"
          v-for="friendRequest in friendShipRequests"
          :key="friendRequest.id"
        >
          <img
            src="https://i.pravatar.cc/100?img=70"
            class="mb-6 rounded-full mx-auto"
          />

          <p>
            <strong>
              <RouterLink
                :to="{
                  name: 'profile',
                  params: { id: friendRequest.created_by.id },
                }"
              >
                {{ friendRequest.created_by.name }}
              </RouterLink>
            </strong>
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>

          <div class="mt-6 space-x-4">
            <button class="inline-block py-4 px-6 bg-sky-600
            text-white rounded-lg">Accept</button>
            <button class="inline-block py-4 px-6 bg-rose-700
            text-white rounded-lg">No no</button>
          </div>
        </div>
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";
import Trends from "@/components/Trends.vue";
import axios from "axios";
import type { Friendrequest, GetFriendsResponse, User } from "@/types";
import type { Post } from "@/types";
import { useRoute } from "vue-router";

const userFriends = ref<User[]>([]);
const friendShipRequests = ref<Friendrequest[]>([]);
const user = ref<User | null>(null);
const route = useRoute();

const getUserFriend = async () => {
  try {
    const userId = route.params.id;
    const response = (await axios.get(
      `/api/friends/${userId}/`
    )) as GetFriendsResponse;

    console.log("User friends response:", response.data);

    userFriends.value = response.data.friends;
    friendShipRequests.value = response.data.friendship_requests;
    user.value = response.data.user;
  } catch (error) {
    console.error("Error fetching user friends:", error);
  }
};

watch(
  () => route.params.id,
  (newId, oldId) => {
    if (newId && newId !== oldId) {
      getUserFriend();
    }
  },
  { immediate: true } // This will run immediately when component mounts
);

const addFriend = async () => {
  try {
    const addFriendRes = await axios.post(
      `/api/friends/request/${route.params.id}/`
    );
    // user.value = addFriendRes.data.user;
  } catch (error) {
    console.error("Error adding friend:", error);
  }
};
</script>
