<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" xs="12" sm="8" md="6" lg="6" xl="6">
        <Card title="Number converted in words:">
          <CopyDisplay :copy-text="numInWords" />
        </Card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Card from "./../../components/core/Card.vue";
import CopyDisplay from "./../../components/result/CopyDisplay.vue";
export default {
  components: { Card, CopyDisplay },
  data() {
    return {
      numInWords: "",
      number: "",
    };
  },
  created() {
    this.fetchNumToWords();
  },
  methods: {
    notifyError(error) {
      const { $bus } = useNuxtApp();
      console.log({ error });

      const defaultError =
        "Unknown error please enter in contact with the administrator ";
      const message = error ? error : defaultError;
      console.log({ message });

      $bus.$emit("notify", { message, type: "error" });
    },
    async fetchNumToWords() {
      const { number } = this.$route.params;
      this.number = number;

      let numInWords;
      let errorMessage;
      const config = useRuntimeConfig();
      console.log({ baseUrl: config.public.backed_base_url });
      const baseURL = config.public.backed_base_url
      await useFetch(`${baseURL}/num_to_english/${number}`, {
        server: false,
        headers: {
          "Access-Control-Allow-Origin": "*"
        },
        method: "get",

        onResponse({ response }) {
          if (response.ok) {
            const data = response._data.data;
            const { num_in_english } = data;
            numInWords = num_in_english;
          } else {
            const error = response._data.error;
            const { message } = error;
            errorMessage = message;
          }
        },
      });

      if (numInWords) this.numInWords = numInWords;
      else {
        this.notifyError(errorMessage);
        this.$router.push(`/`);
      }
    },
  },
};
</script>
