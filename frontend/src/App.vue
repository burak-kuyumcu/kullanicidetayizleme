<script setup>
import { computed, onMounted } from 'vue';
import { RouterView, RouterLink, useRoute } from 'vue-router';
import { useUserStore } from './stores/useUserStore';

const store = useUserStore()
const route = useRoute()
const isAlbum = computed(() => route.name === 'user-album')

const selectedUserId = computed(() => {
  return route.params.id ? Number(route.params.id) : null
})

const selectedUser = computed(() => {

  if (!selectedUserId.value){
    return null
  }
  return store.users.find((u) => u.id === selectedUserId.value) || null
})

onMounted(async () => {

  if(!store.users.length){

    await store.fetchFromAPI()

  }
})

</script>

<template>
  <div class="flex min-h-screen bg-slate-50">

    <aside class="w-64 bg-slate-800 text-white flex flex-col">

      <div class="p-5 text-xl font-bold border-b border-slate-700">

        <div v-if="selectedUser" class="mt-4 flex items-center gap-3">

          <img v-if="selectedUser.url" :src="selectedUser.url" class="w-10 h-10 rounded-full object-cover border border-slate-600" alt="avatar"/>

          <div>
            <p class="text-sm font-semibold">{{ selectedUser.name }}</p>
            <p class="text-xs text-slate-300">{{ selectedUser.email || 'email yok' }}</p>

          </div>

        </div>

      </div>

      <nav v-if="!selectedUserId" class="p-4 space-y-2">
        <RouterLink to="/" class="block px-4 py-2 rounded-lg hover:bg-slate-700 transition hover: bg-slate-700" active-class="bg-slate-700 border-l-4 border-l-blue-400 pl-3" >
          Users
        </RouterLink>

      </nav>

      <nav v-else class="p-4 space-y-2">
        
        <RouterLink :to="`/users/${selectedUserId}/todos`" class="relative block px-4 py-2 rounded-lg transition hover:bg-slate-700" active-class="bg-slate-700 before:absolute before:left-0 before:top-0 before:h-full before:w-1 before:bg-blue-400" >
         Todos 
        </RouterLink>

        <RouterLink :to="`/users/${selectedUserId}/posts`" class="relative block px-4 py-2 rounded-lg transition hover:bg-slate-700" active-class="bg-slate-700 before:absolute before:left-0 before:top-0 before:h-full before:w-1 before:bg-blue-400">
          Posts
        </RouterLink>

        <RouterLink  :to="`/users/${selectedUserId}/gallery`" class="relative block px-4 py-2 rounded-lg transition hover:bg-slate-700" active-class="bg-slate-700 before:absolute before:left-0 before:top-0 before:h-full before:w-1 before:bg-blue-400">
          Albums
        </RouterLink>

       

      </nav>
    </aside>

    <main class="flex-1 p-6 overflow-y-auto">
      <router-view />
    </main>

  </div>



</template>