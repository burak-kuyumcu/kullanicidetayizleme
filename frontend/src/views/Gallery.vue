<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/useUserStore';
import { IconSquareRoundedArrowLeft } from '@tabler/icons-vue';

const route = useRoute()
const router = useRouter()
const store = useUserStore()
const userId = computed(() => Number(route.params.id))
const albums = ref([])
const currentUser = computed(() => store.users.find((user) => user.id === userId.value))

onMounted(async () => {

    if (!store.users.length){
        await store.fetchFromAPI()
    }
    await fetchAlbums()
})

async function fetchAlbums(){

    const res = await fetch(`http://127.0.0.1:8000/api/gallery-albums/?user=${userId.value}`)
    
    if (!res.ok){
        return
    }
    albums.value = await res.json()
}

function goAlbum(albumId) {
    router.push(`/users/${userId.value}/gallery/${albumId}`)
}

function goHome(){
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen">
    
    <div class="flex items-center gap-3 mb-6">

      <button @click="goHome" class="flex items-center justify-center text-[#26303E] hover:text-[#4F359B] transition" aria-label="go back">

        <IconSquareRoundedArrowLeft class="w-6 h-6" stroke-width="1.7" />
      </button>

      <h1 class="text-xl font-semibold text-[#26303E] leading-none">
        Go Home
      </h1>

    </div>

    
    <div class="pl-4 pr-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 justify-start">

      <div v-for="album in albums" :key="album.id" @click="goAlbum(album.id)" class="cursor-pointer bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md transition hover:-translate-y-1 max-w-[360px] w-full">
        
        <div class="grid grid-cols-2 grid-rows-2 w-full aspect-square">

          <img v-for="(photo, i) in album.sample_photos?.slice(0, 4)" :key="i" :src="photo" class="object-cover w-full h-full" alt="album photo"/>

          <div v-if="!album.sample_photos?.length" class="flex items-center justify-center bg-slate-100 text-slate-400 text-sm col-span-2 row-span-2">
            Fotoğraf yok
          </div>
        </div>

       
        <div class="px-3 py-2 text-slate-700 truncate text-sm">
          {{ album.name }}
        </div>
      </div>

    </div>



  </div>
  
</template>
