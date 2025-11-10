# Kullanıcı Detay İzleme Platformu

Django (REST) + Vue.js ile yazılmıştır.

Kullanıcıları listeler, seçili kullanıcıya ait paylaşımları, albümleri ve görevleri gösterir. 

Backend dockerize edilmiştir.

# 1. Teknolojiler

    Backend: Django, Django REST Framework 
    DB: PostgreSQL 
    Frontend: Vue 3 (Vite)
    API için yardımcı araç olarak: Swagger 


 # 2. Docker Ile Backendi Çalıştırma 

    cd backend
    docker compose up --build


 # 3. Docker Olmadan Backendi Çalıştırma 
    cd backend
    python -m venv venv
    venv\Scripts\activate  (Windows) / source venv/bin/activate (Linux/Mac)
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

# 4. Backend Test Bölümün Çalıştırılması

    Docker ile çalıştırıldıysa
    docker compose exec django-app python manage.py test api

    Docker olmadan çalıştırıldıysa
    python manage.py test api


# 5. Önemli Endpointler
    GET /api/tracked-users/ – kullanıcı listesi
    GET /api/tasks/?user=<id> – kullanıcının görevleri
    GET /api/posts/?user=<id> – kullanıcının postları
    GET /api/albums/?owner=<id> – kullanıcının albümleri
    GET /api/photos/?album=<id> – albüme ait fotoğraflar
