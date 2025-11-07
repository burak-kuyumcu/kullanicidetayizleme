import { createRouter, createWebHistory } from 'vue-router'
import userView from '@/views/UserView.vue'
import Todos from '@/views/Todos.vue'
import Gallery from '@/views/Gallery.vue'
import Album from '@/views/Album.vue'
import Posts from '@/views/Posts.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    
    { path: '/', name: 'home', component: userView },
    { path: '/users/:id/todos', name: 'user-todos', component: Todos, props: true },
    { path: '/users/:id/posts', name: 'user-posts', component: Posts, props:true},
    { path: '/users/:id/gallery', name: 'user-gallery', component: Gallery, props:true},
    { path: '/users/:id/gallery/:albumId', name: 'user-album', component: Album, props: true },
   
    
  ],
})

export default router
