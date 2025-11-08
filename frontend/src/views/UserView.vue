<script setup>
 import { onMounted, computed } from 'vue'
 import { useUserStore } from '@/stores/useUserStore';
 import { useRouter } from 'vue-router';
 import {IconMapPinHeart,IconBuildingSkyscraper,IconWorldShare,} from '@tabler/icons-vue'

 
 const store = useUserStore()
 const router = useRouter()

 onMounted(async() =>{

    if(!store.users.length){
        await store.fetchFromAPI()
    }
 })

 const users = computed(() => store.users)

 function goTodo(user){

    router.push(`/users/${user.id}/todos`)
 }
</script>


<template>
  <div class="min-h-screen bg-slate-50">
    <h1 class="text-2xl font-semibold text-title mb-6">All Users</h1>

    
    <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

      <button v-for="user in users" :key="user.id" @click="goTodo(user)" class="text-left bg-white rounded-2xl border border-border/70 shadow-sm hover:shadow-md transition hover:-translate-y-0.5 focus:outline-none">

        <div class="p-5 flex gap-4">
          
          <div class="w-16 h-16 rounded-full bg-subtitle/10 flex items-center justify-center overflow-hidden" >

            <img v-if="user.url" :src="user.url" class="w-full h-full object-cover" alt="avatar"/>

            <span v-else class="text-lg font-semibold text-title">

              {{ user.name?.[0] || 'U' }}

            </span>

          </div>

         
          <div class="flex-1">
            
            <p class="text-base font-semibold text-title">

              {{ user.name }}

            </p>

            <p class="text-sm text-subtitle">

              {{ user.email || 'email yok' }}

            </p>

            <p class="text-sm text-subtitle">

              {{ user.tel || '' }}

            </p>

          </div>

        </div>


       
        <div class="px-5 pb-5 space-y-3 text-sm text-title/80">
         
          <div class="flex items-start gap-3">

            <div class="mt-1 w-7 h-7 rounded-md bg-primary/10 flex items-center justify-center text-primary">

              <IconMapPinHeart :size="18" stroke-width="1.8" />

            </div>

            <div>

              <p class="text-xs font-semibold text-title mb-0.5">Location</p>
              
              <p class="text-xs text-subtitle leading-snug">

                {{ user.konum || 'Adres bilgisi yok' }}

              </p>

            </div>

          </div>

          
          <div class="flex items-start gap-3">

             <div class="mt-1 w-7 h-7 rounded-md bg-primary/10 flex items-center justify-center text-primary">

              <IconBuildingSkyscraper :size="18" stroke-width="1.8" />

            </div>

            <div>

              <p class="text-xs font-semibold text-title mb-0.5">Company</p>

              <p class="text-xs text-subtitle leading-snug">

                {{ user.company || 'Şirket bilgisi yok' }}

              </p>

            </div>

          </div>

          
          <div class="flex items-start gap-3">

            <div class="mt-1 w-7 h-7 rounded-md bg-primary/10 flex items-center justify-center text-primary">

              <IconWorldShare :size="18" stroke-width="1.8" />

            </div>

            <div>

              <p class="text-xs font-semibold text-title mb-0.5">Website</p>

              <p class="text-xs text-subtitle leading-snug">

                {{ user.web || '—' }}

              </p>

            </div>

          </div>

        </div>

      </button>

    </div>

  </div>
  
</template>