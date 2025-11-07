<script setup>
 import { onMounted } from 'vue'
 import { useUserStore } from '@/stores/useUserStore';

 
 const store = useUserStore()

 onMounted(async() =>{

    if(!store.users.length){
        await store.fetchFromAPI()
    }
 })
</script>


<template>
    <div class = "min-h-screen bg-slate-50 p-6">
        <h1 class = "text-2xl font-bold mb-6"> All Users</h1>

        <div class = "grid gap-6 md:grid-cols-2 lg:grid-cols-3">

            <router-link v-for="user in store.users" :key="user.id" :to="`/users/${user.id}/todos`" class="bg.white rounded-2x1 border border-state-100 p-4 flex gap-4 items-start hover:shadow-lg transition-shadow cursor-pointer">
            
            <div class="w-16 h-16 rounded-full bg-slate-200 overflow-hidden flex items-center justify-center">

                <span class="text-xl font-semibold text-slate-600">
                    {{ user.name?.[0] ?? 'U' }}

                </span>

            </div>

            <div class ="flex-1">
                <h2 class="text-lg font-semibold text-slate-800">
                    {{ user.name }}

                </h2>
                
                <p class="text-sm text-slate-500">
                    {{ user.email }}

                </p>

                <p class="text-sm text-slate-500">
                    {{ user.tel}}

                </p>

                <div class="mt-3 space-y-1 text-sm text-slate-600">
                    <div class="flex gap-2 items-center">
                        <span class="text-slate-400">📍</span>
                        <span>{{ user.konum }}</span>

                    </div>

                    <div class="flex-gap-2 items-center">
                        <span class="text-slate-400">🏢</span>
                        <span>{{ user.company }}</span>

                    </div>

                    <div class="flex-gap-2 items-center">
                        <span class="text-slate-400">🌐</span>
                        <span>{{ user.web }}</span>


                    </div>


                </div>




            </div>



            </router-link>

        </div>


    </div>


</template>