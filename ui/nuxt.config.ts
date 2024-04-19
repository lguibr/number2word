import vuetify, { transformAssetUrls } from "vite-plugin-vuetify";
export default defineNuxtConfig({
  ssr: false,
  pages: true,
  build: {
    transpile: ["vuetify"],
  },
  modules: [
    "nuxt-proxy",
    (_options, nuxt) => {
      nuxt.hooks.hook("vite:extendConfig", (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }));
      });
    },
  ],
  proxy: {
    options: {
      target:
        "http://infras-djang-phu6uswnjk0h-891179164.us-east-1.elb.amazonaws.com",
      changeOrigin: true,
      pathRewrite: {
        "^/api/": "/",
      },
      pathFilter: ["/api/num_to_english"],
    },
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
});
