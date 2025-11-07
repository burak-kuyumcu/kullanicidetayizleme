<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/useUserStore';

const route = useRoute()
const router = useRouter()
const store = useUserStore()
const userId = computed(() => Number(route.params.id))
const albums = ref([])
const currentUser = computed(() => store.users.find((u) => u.id === userId.value))

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
  <div class="space-y-6">
   
    <div class="flex items-center gap-3">
      <button
        @click="goHome"
        class="w-10 h-10 flex items-center justify-center rounded-full border border-slate-200 hover:bg-slate-100 transition"
        aria-label="go home"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      <h1 class="text-xl font-semibold text-slate-800">Go Home</h1>
    </div>

    
    <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      <div
        v-for="album in albums"
        :key="album.id"
        @click="goAlbum(album.id)"
        class="cursor-pointer bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md transition hover:-translate-y-1"
      >
        <div class="grid grid-cols-2 grid-rows-2 w-full aspect-square">
          <img
            v-for="(photo, i) in album.sample_photos?.slice(0, 4)"
            :key="i"
            :src="photo"
            class="object-cover w-full h-full"
            alt="album photo"
          />
          <div
            v-if="!album.sample_photos?.length"
            class="flex items-center justify-center bg-slate-100 text-slate-400 text-sm col-span-2 row-span-2"
          >
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