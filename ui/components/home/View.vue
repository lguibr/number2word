<template>
  <v-container class="center_container">
    <v-col cols="12" xs="12" sm="8" md="6" lg="6" xl="6">
      <Card title="Convert number to words">
        <NumberForm />
      </Card>
    </v-col>
  </v-container>
</template>

<script>
import Card from "./../components/core/Card.vue";
import NumberForm from "./../components/home/Form.vue";
export default { components: { Card, NumberForm } };
</script>

<style>
.center_container {
  display: flex;
  justify-content: center;
  align-items: center;
  justify-items: center;
  align-content: center;
  flex-direction: column;
  height: 100%;
}
</style>
