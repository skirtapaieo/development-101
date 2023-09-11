// tailwind.config.js
module.exports = {
  mode: "jit",
  purge: [
    // Add your paths here
  ],
  plugins: [],
  theme: {
    extend: {
      backdropBlur: {
        none: "blur(0)",
        sm: "blur(4px)",
        md: "blur(12px)",
        lg: "blur(16px)",
      },
    },
  },
  variants: {
    extend: {},
  },
};
