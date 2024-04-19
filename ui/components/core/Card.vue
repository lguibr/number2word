<template>
  <v-card>
    <template #title>
      <span class="title">{{ title }}</span>
    </template>

    <v-card-text>
      <slot />
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      default: "Default Card Value",
    },
  },
};
</script>

<style scoped>
.title {
  font-weight: bold;
  width: 100%;
  justify-content: center;
  padding: 0.5em;
}
</style>
