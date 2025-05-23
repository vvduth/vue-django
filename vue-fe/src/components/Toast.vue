<template>
    <div
        v-if="store.isVisible"
        class="fixed bottom-0 right-0 mb-4 mr-4 bg-sky-600 text-white text-sm rounded-lg p-4 shadow-lg"
        role="alert"
        :class="store.classes"
    >
    {{ store.message }}
    </div>
</template>

<script setup lang="ts">
import { useToastStore } from '@/stores/toast';

const store = useToastStore();

</script>