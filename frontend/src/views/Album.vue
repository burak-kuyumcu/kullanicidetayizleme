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
    <div>
        <div class="flex items-center justify-between mb-6">
            <div>
                
            </div>
            <button @click="goBack" class="px-4 py-2 bg-slate-800 text-white rounded-lg hover:bg-slate-700">
                 ← Galeriye dön
            </button>
        </div>

        <div class="grid gap-4 md:grid-cols-3 lg:grid-cols-4">
            <div v-for="photo in photos" :key="photo.id" class="bg-white rounded-xl overflow-hidden border border-slate-100">
                <img :src="photo.image_url" class="w-full h-44 object-cover">
                <p class="p-3 text-sm text-slate-600 " v-if="photo.title">
                    {{ photo.title }}
                </p>
            </div>



        </div>






    </div>
</template>