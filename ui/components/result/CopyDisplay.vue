<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <div class="text-display">
          {{ copyText }}
          <v-btn icon class="copy">
            <v-icon icon="mdi-content-copy" @click="copyToClipboard" />
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    copyText: {
      type: String,
      required: true,
    },
  },
  methods: {
    notifyCopy() {
      const { $bus } = useNuxtApp();
      $bus.$emit("notify", { message: "Copied", type: "success" });
    },
    copyToClipboard() {
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(this.copyText).then(
          () => {
            this.notifyCopy();
          },
          () => {
            alert("Failed to copy text.");
          },
        );
      } else {
        const textArea = document.createElement("textarea");
        textArea.value = this.copyText;
        textArea.style.position = "fixed";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
          document.execCommand("copy");
          this.notifyCopy();
        } catch (err) {
          alert("Failed to copy text.");
        }

        document.body.removeChild(textArea);
      }
    },
  },
};
</script>

<style scoped>
.text-display {
  padding: 1em;
  padding-bottom: 2px;
  padding-right: 2px;
  height: 50vh;
  border: 1px solid #ccc;
  border-radius: 4px;
  position: relative;
}

.copy {
  position: absolute;
  right: 1em;
  bottom: 1em;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
