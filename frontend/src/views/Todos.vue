<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/useUserStore'
import { IconSquareRoundedArrowLeft } from '@tabler/icons-vue'

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
  <div class="w-full">
   
    <div class="flex items-center gap-3 mb-6">
      <button
        @click="goBack"
        class="flex items-center justify-center text-[#26303E] hover:text-[#4F359B] transition"
        aria-label="go back"
      >
        <IconSquareRoundedArrowLeft class="w-6 h-6" stroke-width="1.7" />
      </button>
      <h1 class="text-xl font-semibold text-[#26303E] leading-none">
        Go Home
      </h1>
    </div>

    
    <div class="mt-20 pl-4 space-y-6">
      <div
        v-for="todo in todos"
        :key="todo.id"
        class="flex items-center gap-3"
      >
        <label class="flex items-center gap-3 cursor-pointer select-none">
          
          <input
            type="checkbox"
            :checked="todo.is_Done"
            @change="toggleTodo(todo)"
            class="sr-only peer"
          />

          
          <span
            class="w-5 h-5 rounded-md border border-[#9CA3AF] flex items-center justify-center
                   transition peer-checked:bg-[#4F359B] peer-checked:border-[#4F359B]"
          >
            
            <svg
              v-if="todo.is_Done"
              xmlns="http://www.w3.org/2000/svg"
              class="w-3 h-3 text-white"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M16.707 5.293a1 1 0 010 1.414l-7.25 7.25a1 1 0 01-1.414 0l-3.5-3.5a1 1 0 111.414-1.414l2.793 2.793 6.543-6.543a1 1 0 011.414 0z"
                clip-rule="evenodd"
              />
            </svg>
          </span>

          <span
            :class="todo.is_Done ? 'text-[#5C6672] line-through' : 'text-[#26303E]'"
            class="text-sm"
          >
            {{ todo.title }}
          </span>
        </label>
      </div>
    </div>
  </div>
</template>


