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
  <div class="min-h-screen bg-[#F5F6FA]">
    
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

    
    <div class="rounded-2xl overflow-hidden">
  <div v-for="(post, idx) in posts" :key="post.id" class="py-8 px-6">
  <div class="max-w-3xl">
    <h2 class="text-lg font-semibold text-[#26303E] mb-2">
      {{ post.title || 'Post Title' }}
    </h2>
    <p class="text-[#5C6672] leading-relaxed">
      {{ post.content || 'Bu post için içerik girilmemiş.' }}
    </p>
  </div>

 
  <div class="flex justify-end mt-4">
    <button
      @click="openPost(post)"
      class="flex items-center gap-2 text-[15px] font-semibold text-[#4F359B] hover:text-[#362473] transition"
    >
      <span>See More</span>
      <IconSquareRoundedArrowRight :size="22" stroke-width="2" />
    </button>
  </div>

  
  <div v-if="idx !== posts.length - 1" class="border-t border-slate-200 mt-6"></div>
</div>


  <p v-if="!posts.length" class="text-[#5C6672] text-sm p-6">
    Bu kullanıcıya ait post yok.
  </p>
</div>

    
    <div
      v-if="showModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 px-4"
    >
      <div
        class="bg-white w-full max-w-5xl h-[520px] rounded-3xl shadow-xl overflow-hidden relative flex"
      >
        
        <div class="w-1/2 p-8 overflow-y-auto">
          <h2 class="text-xl font-semibold mb-6 text-[#26303E]">
            {{ selectedPost?.title || 'Post Title' }}
          </h2>
          <p class="text-sm text-[#5C6672] leading-relaxed whitespace-pre-line">
            {{ selectedPost?.content }}
          </p>
        </div>

        
        <div class="w-px bg-[#EEF0F4]"></div>

        
        <div class="w-1/2 p-8 overflow-y-auto">
          <h3 class="text-base font-semibold mb-6 text-[#26303E]">
            Comments
          </h3>

          <div v-if="comments.length" class="space-y-5">
            <div
              v-for="comment in comments"
              :key="comment.id"
              class="flex gap-4"
            >
              <img
                v-if="comment.author_avatar"
                :src="comment.author_avatar"
                class="w-11 h-11 rounded-full object-cover"
                alt=""
              />
              <div
                v-else
                class="w-11 h-11 rounded-full bg-[#E5E7EB] flex items-center justify-center text-sm text-[#5C6672]"
              >
                {{ comment.author_name?.[0] || 'U' }}
              </div>

              <div class="flex-1">
                <p class="text-sm font-semibold text-[#26303E]">
                  {{ comment.author_name }}
                </p>
                <p class="text-sm text-[#5C6672] leading-relaxed">
                  {{ comment.text }}
                </p>
              </div>
            </div>
          </div>

          <p v-else class="text-sm text-[#5C6672]">
            Bu post için yorum yok.
          </p>
        </div>

       
        <button
          @click="closeModal"
          class="absolute top-4 right-4 text-[#5C6672] hover:text-[#4F359B] transition"
        >
          <IconSquareRoundedX :size="22" stroke-width="1.7" />
        </button>
      </div>
    </div>
  </div>
</template>
