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
  <div class="min-h-screen bg-white">  
    <h1 class="text-2xl font-semibold text-[#26303E] mb-6">
      All users
    </h1>

    <div class="flex flex-wrap gap-6">

      <button v-for="user in users" :key="user.id" @click="goTodo(user)" class="w-full max-w-[420px] bg-white rounded-2xl border border-[#E4E6EC] shadow-sm hover:shadow-md hover:-translate-y-0.5 transition text-left">

        <div class="p-5 flex gap-4">

          <div class="w-16 h-16 rounded-full bg-[#F1ECFF] flex items-center justify-center overflow-hidden">

            <img v-if="user.url" :src="user.url" alt="avatar" class="w-full h-full object-cover"/>

            <span v-else class="text-lg font-semibold text-[#26303E]">
              {{ user.name?.[0] || 'U' }}
            </span>

          </div>

          <div class="flex-1">

            <p class="text-base font-semibold text-[#26303E]">
              {{ user.name }}
            </p>

            <p class="text-sm text-[#5C6672]">
              {{ user.email || 'email yok' }}
            </p>

            <p class="text-sm text-[#5C6672]">
              {{ user.tel || '' }}
            </p>

          </div>

        </div>

        <div class="px-5 pb-5 space-y-3 text-sm text-[#26303E]">

          <div class="flex items-start gap-3">
            
            <div class="mt-1 w-7 h-7 rounded-md bg-[#F1ECFF] flex items-center justify-center text-[#4F359B]">
              <IconMapPinHeart :size="18" stroke-width="1.8" />
            </div>

            <div>

              <p class="text-xs font-semibold text-[#26303E] mb-0.5">Location</p>

              <p class="text-xs text-[#5C6672] leading-snug">
                {{ user.konum || 'Adres bilgisi yok' }}
              </p>

            </div>

          </div>

          <div class="flex items-start gap-3">
            
            <div class="mt-1 w-7 h-7 rounded-md bg-[#F1ECFF] flex items-center justify-center text-[#4F359B]">
              <IconBuildingSkyscraper :size="18" stroke-width="1.8" />
            </div>

            <div>
              <p class="text-xs font-semibold text-[#26303E] mb-0.5">Company</p>

              <p class="text-xs text-[#5C6672] leading-snug">
                {{ user.company || 'Şirket bilgisi yok' }}
              </p>

            </div>
          </div>

          <div class="flex items-start gap-3">
            
            <div class="mt-1 w-7 h-7 rounded-md bg-[#F1ECFF] flex items-center justify-center text-[#4F359B]">
              <IconWorldShare :size="18" stroke-width="1.8" />
            </div>

            <div>

              <p class="text-xs font-semibold text-[#26303E] mb-0.5">Website</p>

              <p class="text-xs text-[#5C6672] leading-snug">
                {{ user.web || '—' }}
              </p>

            </div>

          </div>

        </div>

      </button>

    </div>

  </div>

  
</template>
