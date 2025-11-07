<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/useUserStore'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const todos = ref([])
const userId = computed(() => Number(route.params.id))

const currentUser = computed(() =>
  store.users.find((u) => u.id === userId.value)
)

onMounted(async () => {
  if (!store.users.length) {
    await store.fetchFromAPI()
  }
  await fetchTodos()
})

async function fetchTodos() {
  const res = await fetch(`http://127.0.0.1:8000/api/tasks/?user=${userId.value}`)
  if (!res.ok) return
  todos.value = await res.json()
}


async function toggleTodo(todo) {
  
  const old = todo.is_Done
  todo.is_Done = !old

  const res = await fetch(`http://127.0.0.1:8000/api/tasks/${todo.id}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ is_Done: todo.is_Done }),
  })

  if (!res.ok) {
    
    todo.is_Done = old
  }
}

async function deleteTodo(todo) {
  const res = await fetch(`http://127.0.0.1:8000/api/tasks/${todo.id}/`, {
    method: 'DELETE',
  })
  if (res.ok || res.status === 204) {
    todos.value = todos.value.filter((t) => t.id !== todo.id)
  }
}

function goBack() {
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen px-12 pt-10 font-sans bg-[#F7F9FB]">
    
    <div class="flex items-center gap-3 mb-10">
      <button
        @click="goBack"
        class="w-10 h-10 flex items-center justify-center rounded-full border border-[#D8D9DD] hover:bg-slate-50 transition"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-[#26303E]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <h1 class="text-xl font-semibold text-[#26303E]">Go Home</h1>
    </div>

    
    <div class="space-y-6">
      <label
        v-for="todo in todos"
        :key="todo.id"
        class="flex items-center gap-5 cursor-pointer select-none"
      >
        
        <input
          type="checkbox"
          class="todo-checkbox"
          :checked="todo.is_Done"
          @change="toggleTodo(todo)"
        />

        
        <span
          class="text-[15px] leading-relaxed"
          :class="todo.is_Done ? 'line-through text-[#5C6672]' : 'text-[#26303E]'"
        >
          {{ todo.title }}
        </span>
      </label>

      <p v-if="!todos.length" class="text-[#5C6672] text-sm italic">
        Bu kullanıcıya ait görev bulunmuyor.
      </p>
    </div>
  </div>
</template>

<style scoped>

.todo-checkbox {
  width: 22px;
  height: 22px;
  border: 2px solid #D8D9DD;
  border-radius: 4px;
  accent-color: #4F359B;
  cursor: pointer;
  transition: all 0.2s ease;
}
.todo-checkbox:hover {
  transform: scale(1.08);
}
</style>

