<template>
  <HelloWorld />
  <h1>{{ message }}</h1>
</template>
<script setup lang="ts">
import HelloWorld from "./components/HelloWorld.vue";
import { ref,  unref, onMounted } from "vue";
const message = ref<any>(null);
const fetchData = async () => {
  const response = await fetch("/api");
  const data = await response.json();
  message.value = unref(data);
};
onMounted(async() => {
  await fetchData();
});
</script>