<script setup>
import { computed, onMounted } from 'vue'
import { RouterView, RouterLink, useRoute } from 'vue-router'
import { useUserStore } from './stores/useUserStore'
import { IconCheckupList, IconNotebook, IconPhotoHeart, IconUsers } from '@tabler/icons-vue'

const store = useUserStore()
const route = useRoute()


const selectedUserId = computed(() =>

  route.params.id ? Number(route.params.id) : null

)


const selectedUser = computed(() => {

  if (!selectedUserId.value) return null

  return store.users.find((u) => u.id === selectedUserId.value) || null

})


onMounted(async () => {

  if (!store.users.length) {

    await store.fetchFromAPI()

  }

})
</script>

<template>
  <div class="flex min-h-screen bg-[#FFFFFF] text-[#26303E] font-[Poppins,sans-serif]">
    
    <div class="w-[260px] bg-[#F5F6FA] border-r border-[#D8D9DD] flex flex-col">
      
      <div class="px-6 pt-6 pb-5 border-b border-[#D8D9DD] bg-[#F5F6FA]">

        <div v-if="selectedUser" class="flex items-center gap-3">

          <div class="w-12 h-12 rounded-full bg-[#E5E7EB] overflow-hidden flex items-center justify-center">

            <img v-if="selectedUser.url" :src="selectedUser.url" alt="avatar" class="w-full h-full object-cover"/>

            <span v-else class="text-base font-bold">

              {{ selectedUser.name?.[0] || 'U' }}

            </span>

          </div>


          <div class="leading-tight">

            <p class="text-base font-bold tracking-tight">

              {{ selectedUser.name }}

            </p>

            <p class="text-[12px] text-[#5C6672]">

              {{ selectedUser.email || 'email yok' }}

            </p>

          </div>


        </div>

      </div>


      
      <nav v-if="selectedUserId" class="mt-15 flex-1 space-y-3">

        <RouterLink :to="`/users/${selectedUserId}/todos`" class="relative flex items-center gap-3 py-3 pl-6 pr-4 text-base rounded-r-full transition" :class="route.name === 'user-todos' ? 'bg-white text-[#4F359B]' : 'text-[#6B6B6B]'">

          <span class="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-8 rounded-r-full" :class="route.name === 'user-todos' ? 'bg-[#4F359B]' : 'bg-transparent'"/>

          <span class="w-8 h-8 flex items-center justify-center" :class="route.name === 'user-todos' ? 'text-[#4F359B]' : 'text-[#6B6B6B]'">

            <IconCheckupList :size="20" stroke-width="1.7" />

          </span>

          <span class="font-medium">Todos</span>

        </RouterLink>


        <RouterLink :to="`/users/${selectedUserId}/posts`" class="relative flex items-center gap-3 py-3 pl-6 pr-4 text-base rounded-r-full transition" :class="route.name === 'user-posts' ? 'bg-white text-[#4F359B]' : 'text-[#6B6B6B]'">

          <span class="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-8 rounded-r-full" :class="route.name === 'user-posts' ? 'bg-[#4F359B]' : 'bg-transparent'"/>

          <span class="w-8 h-8 flex items-center justify-center" :class="route.name === 'user-posts' ? 'text-[#4F359B]' : 'text-[#6B6B6B]'">

            <IconNotebook :size="20" stroke-width="1.7" />

          </span>

          <span class="font-medium">Posts</span>

        </RouterLink>


        <RouterLink :to="`/users/${selectedUserId}/gallery`" class="relative flex items-center gap-3 py-3 pl-6 pr-4 text-base rounded-r-full transition" :class="['user-gallery', 'user-album'].includes(route.name) ? 'bg-white text-[#4F359B]' : 'text-[#6B6B6B]'">
          <span class="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-8 rounded-r-full" :class="['user-gallery', 'user-album'].includes(route.name) ? 'bg-[#4F359B]' : 'bg-transparent'"/>

          <span class="w-8 h-8 flex items-center justify-center" :class="['user-gallery', 'user-album'].includes(route.name) ? 'text-[#4F359B]' : 'text-[#6B6B6B]'">

            <IconPhotoHeart :size="20" stroke-width="1.7" />

          </span>

          <span class="font-medium">Albums</span>

        </RouterLink>

      </nav>



      
        <nav v-else>
         <RouterLink to="/" class="relative flex items-center gap-3 py-3 pl-6 pr-4 text-base rounded-r-full transition" :class="route.name === 'home' ? 'bg-white text-[#4F359B]' : 'text-[#6B6B6B]'">

          <span class="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-8 rounded-r-full" :class="route.name === 'home' ? 'bg-[#4F359B]' : 'bg-transparent'"/>

          <span class="w-8 h-8 flex items-center justify-center" :class="route.name === 'home' ? 'text-[#4F359B]' : 'text-[#6B6B6B]'">

            <IconUsers :size="20" stroke-width="1.7" />

          </span>

          <span class="font-medium">Users</span>

         </RouterLink>
         
        </nav>

      
      <div class="mt-auto border-t border-[#D8D9DD] bg-[#F3F4F6]">

        <div class="px-6 py-5 flex items-center justify-center gap-3">

          <img src="/src/assets/image.png" alt="company" class="w-12 h-12 rounded-2xl object-cover bg-white shadow-sm"/>

          <p class="text-xl font-extrabold text-[#26303E] leading-none">
            N2Mobil
          </p>

        </div>

      </div>


    </div>

    <main class="flex-1 px-10 py-8 overflow-y-auto">

      <RouterView />

    </main>

  </div>


  
</template>


