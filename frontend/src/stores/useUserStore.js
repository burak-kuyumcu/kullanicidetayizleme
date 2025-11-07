import { defineStore } from 'pinia'

const STORAGE_KEY = 'users-data'

export const useUserStore = defineStore('user',{

  state: () => ({
    users: [],

  }),
  actions: {
    loadFromStorage(){
      const saved = localStorage.getItem(STORAGE_KEY)

      if (saved) {
        this.users = JSON.parse(saved)
      }

    },
    saveToStorage(){
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.users))
    },

    async fetchFromAPI() {
      const res = await fetch('http://127.0.0.1:8000/api/tracked-users/')

      if (!res.ok){
        return
      }

      this.users = await res.json()
    },

    async addUserAPI(name){
        const res = await fetch('http://127.0.0.1:8000/api/tracked-users/',{

            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify({name}),
        })

        if (!res.ok){
            return
        }
        const created = await res.json()
        this.users.unshift(created)
        this.saveToStorage()

    },


    async deleteUserAPI(user){

        if(!user?.id){

            this.users = this.users.filter((u) => u!== user)
            this.saveToStorage()
            return
        }

        const res = await fetch( `http://127.0.0.1:8000/api/tracked-users/${user.id}/`,{

            method: 'DELETE',

        })

        if(res.ok || res.status ===204){

            this.users = this.users.filter((u) => u.id !== user.id)
            this.saveToStorage()
        }

    },


    async updateUserAPI(user){

        if(!user?.id){
            return
        }

        const res = await fench(`http://127.0.0.1:8000/api/tracked-users/${user.id}/`,{


            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({name: user.name, email: user.email, tel:user.tel, konum:user.konum, company:user.company, web:user.web}),
        })

        if(!res.ok){
            return
        }

        const updated = await res.json()
        this.users = this.users.map((u) => u.id === updated.id ? updated : u)
        this.saveToStorage()


    },


    removeLocal(index){

        this.users.splice(index,1)
        this.saveToStorage()
    }
  },
})
