<template>
  <v-form @submit.prevent="submitNumber">
    <v-text-field v-model="number" type="number" :error-messages="errorMessages"  label="Enter a number"
      @blur="validateInput"></v-text-field>
    <v-btn type="submit">
      Submit
    </v-btn>
  </v-form>
</template>

<script>
import { z } from 'zod';
import Spinner from './../core/Spinner.vue';
import Card from './../core/Card.vue';

export default {
  components: { Spinner, Card },
  data() {
    return {
      number: '',
      errorMessages: [],
    };
  },
  methods: {
    validateInput() {
      const numberSchema = z.string().nonempty({
        message: "Number is required"
      }).transform(value => Number(value)).refine(value => !isNaN(value), {
        message: "Invalid number"
      }).refine(value => Math.abs(value) <= 999999999999999999999999999999999, {
        message: "The absolute value must not exceed 999999999999999999999999999999999"
      });

      const result = numberSchema.safeParse(this.number);
      if (result.success) {
        this.errorMessages = [];
      } else {
        this.errorMessages = result.error.errors.map(e => e.message);
      }
    },
    submitNumber() {
      const { $bus } = useNuxtApp();
      this.validateInput();
      if (this.errorMessages.length === 0) {
        $bus.$emit('loading');
        this.$router.push(`/result/${this.number}`);
      }
    }
  }
};
</script>
