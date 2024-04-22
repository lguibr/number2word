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
      maxAbsoluteValue: new BigNumber("999999999999999999999999999999999"),
    };
  },
  methods: {
    validateInput() {
      const numberSchema = z.preprocess(
        (val) => {
          const isEmpty = !val || val === "";
          console.log({ val });

          if (isEmpty) return null;

          const bigNumber = new BigNumber(val);
          const isValidBigNumber = bigNumber.isFinite();
          return isValidBigNumber ? bigNumber.toPrecision() : val;
        },

        z
          .custom()
          .refine((val) => val !== null, { message: "Number is required" })
          .refine((val) => !new BigNumber(val).isNaN(), {
            message: `Number is invalid ${this.number}`,
          })
          .refine(
            (val) =>
              !new BigNumber(val).absoluteValue() <= this.maxAbsoluteValue,
            {
              message: `Number is out of supported range receive: ${this.number}; Max absolute value allowed is ${this.maxAbsoluteValue.toString()}`,
            },
          ),
      );

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
