<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <!-- Post form -->
      <div class="bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="submitPostForm" action="POST">
          <div class="p-4">
            <textarea
              v-model="postBody"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What are you thinking about?"
            ></textarea>
          </div>

          <div class="p-4 border-t border-gray-100 flex justify-between">
            <a
              href="#"
              class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg"
              >Attach image</a
            >

            <button
              href="#"
              class="inline-block py-4 px-6 bg-sky-600 text-white rounded-lg"
            >
              Post
            </button>
          </div>
        </form>
      </div>

      <template v-for="post in posts" :key="post.id">
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
import { onMounted, ref } from "vue";
import PeopleYouMayKnow from "./PeopleYouMayKnow.vue";
import Trends from "./Trends.vue";
import axios from "axios";
import type { Post } from "@/types";
import PostItem from "./PostItem.vue";

const posts = ref<Post[]>([]);
const postBody = ref<string>("");

const submitPostForm = async () => {
  console.log("Submitting post:", postBody.value);

  try {
    const res = await axios.post("/api/posts/create/", {
      body: postBody.value,
    });
    posts.value.unshift(res.data); // Add the new post to the beginning of the posts array
    postBody.value = ""; // Clear the input field after submission
  } catch (error) {
    console.error("Error submitting post:", error);
  }
};

const fetchAllPosts = async () => {
  try {
    const res = await axios.get("/api/posts/");
    posts.value = res.data;
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
};
onMounted(() => {
  fetchAllPosts();
});
</script>
