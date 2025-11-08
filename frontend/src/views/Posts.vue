<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/useUserStore'
import { IconSquareRoundedArrowLeft, IconSquareRoundedArrowRight, IconSquareRoundedX  } from '@tabler/icons-vue'


const route = useRoute()
const store = useUserStore()
const router = useRouter()

const userId = computed(() => Number(route.params.id))
const posts = ref([])
const showModal = ref(false)
const selectedPost = ref(null)
const comments = ref([])

const currentUser = computed(() =>
  store.users.find((u) => u.id === userId.value)
)

onMounted(async () => {
  if (!store.users.length) {
    await store.fetchFromAPI()
  }
  await fetchPosts()
})

async function fetchPosts() {
  const res = await fetch(`http://127.0.0.1:8000/api/posts/?user=${userId.value}`)
  if (!res.ok) return
  posts.value = await res.json()
}

async function openPost(post) {
  selectedPost.value = post
  showModal.value = true
  await fetchComments(post.id)
}

async function fetchComments(postId) {
  const res = await fetch(`http://127.0.0.1:8000/api/comments/?post=${postId}`)
  if (!res.ok) {
    comments.value = []
    return
  }
  comments.value = await res.json()
}

function closeModal() {
  showModal.value = false
  selectedPost.value = null
  comments.value = []
}

function goBack() {

  router.push('/')
}
</script>

<template>
  <div class="min-h-screen">
    
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

    
    <div class="bg-white rounded-2xl">
      <div v-for="(post, idx) in posts" :key="post.id">
        <div class="flex items-start justify-between gap-3 py-8 px-6">
          
          <div class="max-w-3xl">
            <h2 class="text-lg font-semibold text-slate-900 mb-2">
              {{ post.title || 'Post Title' }}
            </h2>
            <p class="text-slate-500 leading-relaxed line-clamp-3">
              {{ post.content || 'Bu post için içerik girilmemiş.' }}
            </p>
          </div>

          
          <button @click="openPost(post)" class="flex items-center gap-2 text-[#26303E] text-sm font-medium hover:text-[#4F359B] transition">
            <span>See More</span>
            <IconSquareRoundedArrowRight :size="18" stroke-width="2" />
          </button>
        </div>

        
        <div v-if="idx !== posts.length - 1" class="border-t border-slate-100 mx-6"></div>
      </div>

      <p v-if="!posts.length" class="text-slate-400 p-6">
        Bu kullanıcıya ait post yok.
      </p>
    </div>

    
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 px-4">
      <div class="bg-white w-full max-w-5xl h-[520px] rounded-3xl shadow-xl overflow-hidden relative flex">
        
        <div class="w-1/2 p-8 overflow-y-auto">
          <h2 class="text-2xl font-semibold mb-6 text-slate-900">
            {{ selectedPost?.title || 'Post Title' }}
          </h2>
          <p class="text-slate-700 leading-relaxed space-y-3 whitespace-pre-line">
            {{ selectedPost?.content }}
          </p>
        </div>

        
        <div class="w-px bg-slate-200"></div>

        
        <div class="w-1/2 p-8 overflow-y-auto">
          <h3 class="text-lg font-semibold mb-6 text-slate-900">Comments</h3>

          <div v-if="comments.length" class="space-y-5">
            <div v-for="comment in comments" :key="comment.id" class="flex gap-4">
              
              <img v-if="comment.author_avatar" :src="comment.author_avatar" class="w-11 h-11 rounded-full object-cover" alt=""/>
              <div v-else class="w-11 h-11 rounded-full bg-slate-200 flex items-center justify-center text-sm text-slate-600">
                {{ comment.author_name?.[0] || 'U' }}
              </div>

              
              <div class="flex-1">
                <p class="text-sm font-semibold text-slate-900">
                  {{ comment.author_name }}
                </p>
                <p class="text-sm text-slate-600 leading-relaxed">
                  {{ comment.text }}
                </p>
              </div>
            </div>
          </div>

          <p v-else class="text-slate-400 text-sm">
            Bu post için yorum yok.
          </p>
        </div>

        
        <button @click="closeModal" class="absolute top-4 right-4 text-[#5C6672] hover:text-[#4F359B] transition">
          <IconSquareRoundedX :size="22" stroke-width="2" />
        </button>
      </div>
    </div>
  </div>
</template>

