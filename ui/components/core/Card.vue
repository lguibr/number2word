<template>
  <v-card>
    <template v-slot:title>
      <span class="title">{{ title }}</span>
    </template>

    <v-card-text>
      <slot></slot>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      default: "Default Card Value"
    }
  }
}
</script> 

<style scoped>
.title {
  font-weight: bold;
  width: 100%;
  justify-content: center;
  padding: .5em;
}
</style>
