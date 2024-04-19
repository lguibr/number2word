<template>
  <v-form @submit.prevent="submitNumber">
    <v-text-field
      v-model="number"
      type="number"
      :error-messages="errorMessages"
      label="Enter a number"
      @blur="validateInput"
    />
    <v-btn type="submit"> Submit </v-btn>
  </v-form>
</template>

<script>
import { BigNumber } from "bignumber.js";
import { z } from "zod";

export default {
  data() {
    return {
      number: "",
      errorMessages: [],
    };
  },
  methods: {
    validateInput() {
      const maxNumber = new BigNumber("999999999999999999999999999999999");
      const numberSchema = z
        .string()
        .nonempty({ message: "Number is required" })
        .transform((value) => new BigNumber(value))
        .refine((num) => !num.isNaN(), { message: "Invalid number" })
        .refine((num) => num.abs().lte(maxNumber), {
          message: `The absolute value must not exceed ${maxNumber.toString()}`,
        });

      const result = numberSchema.safeParse(this.number);
      if (result.success) {
        this.errorMessages = [];
      } else {
        this.errorMessages = result.error.errors.map((e) => e.message);
      }
    },
    submitNumber() {
      const { $bus } = useNuxtApp();
      this.validateInput();
      if (this.errorMessages.length === 0) {
        $bus.$emit("loading");
        this.$router.push(`/result/${this.number}`);
      }
    },
  },
};
</script>
