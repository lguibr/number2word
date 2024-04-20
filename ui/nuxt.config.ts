import vuetify from "vite-plugin-vuetify";
export default defineNuxtConfig({
  eslint: {
    checker: true,
  },
  runtimeConfig: {
    public: {
      backed_base_url:
        process.env.BACKEND_BASE_URL ??
        "https://word2vector.luisguilher.me",
    },
  },
  ssr: false,
  pages: true,
  build: {
    transpile: ["vuetify"],
  },

  modules: [
    "@nuxt/eslint",
    (_options, nuxt) => {
      nuxt.hooks.hook("vite:extendConfig", (config) => {
        // @ts-expect-error Workaround provided in the vuetify official docs
        config.plugins.push(vuetify({ autoImport: true }));
      });
    },
  ],
});
