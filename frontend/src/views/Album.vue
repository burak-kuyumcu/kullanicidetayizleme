<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/useUserStore';


const route = useRoute()
const router = useRouter()
const store = useUserStore()
const userId = computed(() => Number(route.params.id))
const albumId = computed(() => Number(route.params.albumId))
const photos = ref([])
const albumName = ref('Albüm')

const currentUser = computed(() =>{
    
    store.users.find((u) => u.id === userId.value)
})

onMounted(async () => {

    if (!store.users.length){
        await store.fetchFromAPI()
    }
    await fetchPhotos()
})

async function fetchPhotos() {

    const res = await fetch(`http://127.0.0.1:8000/api/photos/?album=${albumId.value}`)
    if (!res.ok){
        return
    }
    const data = await res.json()
    photos.value = data
    
}

function goBack(){

    router.push(`/users/${userId.value}/gallery`)
}
</script>

<template>
  <div class="space-y-6">
    
    <div class="flex items-center gap-3">
      <button
        @click="goBack"
        class="w-10 h-10 flex items-center justify-center rounded-full border border-slate-200 hover:bg-slate-100 transition"
        aria-label="go gallery"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      <h1 class="text-xl font-semibold text-slate-800">Go Gallery</h1>
    </div>

    
    <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      <div
        v-for="photo in photos"
        :key="photo.id"
        class="bg-white rounded-xl overflow-hidden shadow-sm border border-slate-100"
      >
        <img :src="photo.image_url" class="w-full h-40 object-cover" alt="" />
        <div class="px-4 py-2 text-sm text-slate-700">
          {{ photo.title || 'Photo' }}
        </div>
      </div>
    </div>
  </div>
</template>