<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/useUserStore';
import { IconSquareRoundedArrowLeft } from '@tabler/icons-vue'


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
    
   <div class="flex items-center gap-3 mb-6">
      <button
        @click="goBack"
        class="flex items-center justify-center text-[#26303E] hover:text-[#4F359B] transition"
        aria-label="go gallery"
      >
        
        <IconSquareRoundedArrowLeft class="w-6 h-6" stroke-width="1.7" />
      </button>
      <h1 class="text-xl font-semibold text-[#26303E] leading-none">
        Go Gallery
      </h1>
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