/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {

      colors: {
    primary: '#4F359B',
    subtitle: '#5C6672',
    title: '#26303E',
    border: '#D8D9DD',
      },
      fontFamily: {
      sans: ['Poppins', 'ui-sans-serif', 'system-ui'],
    },
    },
  },
  plugins: [],
}
