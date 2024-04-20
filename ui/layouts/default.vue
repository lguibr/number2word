<template>
  <v-theme-provider :theme="theme" with-background>
    <Head>
      <Title>Number 2 Words</Title>
      <Meta
        name="description"
        content="A web app that converts numbers to english words"
      />
    </Head>

    <v-app @modal="setLoading">
      <v-app-bar app>
        <Logo size="50" class="clickable" @click="goHome" />
        <v-toolbar-title class="clickable" @click="goHome"
          >Number to Words</v-toolbar-title
        >
        <v-icon class="icon" icon="mdi-weather-sunny" end />
        <div class="vertical_align">
          <v-switch v-model="darkTheme" />
        </div>
        <v-icon class="icon" icon="mdi-weather-night" end />
      </v-app-bar>

      <v-main>
        <v-container>
          <NuxtPage />

          <Modal v-if="showModal" @close="showModal = false">
            <Spinner />
          </Modal>
          <v-snackbar
            v-model="showNotification"
            :timeout="5000"
            :color="notificationType"
          >
            {{ getnotificationMessage() }}
          </v-snackbar>
        </v-container>
      </v-main>

      <v-footer app class="align_end">
        <NuxtLink to="https://github.com/lguibr/trellis-law">
          <v-btn icon end>
            <v-icon class="icon" icon="mdi-github" />
          </v-btn>
        </NuxtLink>
      </v-footer>
    </v-app>
  </v-theme-provider>
</template>

<script>
import Logo from "./../components/core/Logo.vue";
import Modal from "./../components/core/Modal.vue";
import Spinner from "./../components/core/Spinner.vue";

export default {
  name: "DefaultLayout",
  components: { Logo, Modal, Spinner },
  data: () => ({
    darkTheme: false,
    showModal: false,
    showNotification: false,
    notificationType: "success",
    notification: null,
    type: "success",
  }),
  computed: {
    theme() {
      return this.darkTheme ? "dark" : "light";
    },
  },
  created() {
    const { $bus } = useNuxtApp();
    $bus.$on("loading", () => this.setLoading());
    $bus.$on("notify", ({ message, type }) => {
      console.log("notify!");
      this.showNotification = true;
      this.notification = message;
      this.notificationType = type;
      setTimeout(() => {
        this.showModal = false;
      }, 1000);
    });
  },
  methods: {
    getnotificationMessage: function () {
      this.notification = this.showNotification ? this.notification : "";
      return this.notification;
    },

    goHome: function () {
      this.$router.push(`/`);
    },
    setLoading: function () {
      this.showModal = true;
      setTimeout(() => {
        this.showModal = false;
      }, 5000);
    },
  },
};
</script>

<style scoped>
.vertical_align {
  display: flex;
  justify-items: center;
  align-content: center;
  max-height: 50px;
}

.clickable {
  cursor: pointer;
  padding: 0.5em;
}

.icon {
  padding: 0 1em;
}

.align_end {
  display: flex;
  flex-direction: row-reverse;
}
</style>
