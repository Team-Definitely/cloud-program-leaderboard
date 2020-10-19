import os
from decouple import config
import django_heroku
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'rest_framework',
    'django_celery_beat', 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

CELERY_BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

USERS_URLS = [
    "https://www.qwiklabs.com/public_profiles/0359de94-0bc6-4fb2-8d7c-08c4d8438591",
    "https://www.qwiklabs.com/public_profiles/901b7979-ff7b-48f1-a9c6-486aa4e8631b",
    "https://www.qwiklabs.com/public_profiles/cc52cc1e-1547-48d9-a8b0-a23f00f22b7c",
    "https://www.qwiklabs.com/public_profiles/4a45f296-be58-4ff1-9a54-b671dbfed387",
    "https://google.qwiklabs.com/public_profiles/035b8972-7d51-4809-8d45-bd0b95b11fd3",
    "https://google.qwiklabs.com/public_profiles/5a6dcb4d-e0a7-4ffa-b559-ff0dd4782075",
    "https://google.qwiklabs.com/public_profiles/4c78d52f-48bb-4120-8a7b-4b7b4f9f62cd",
    "https://google.qwiklabs.com/public_profiles/c2b6f0f3-8a91-4395-b0a5-fd054ecdeb09",
    "https://google.qwiklabs.com/public_profiles/02eb7d6d-eef1-4ac8-95d4-28c8452b032b",
    "https://google.qwiklabs.com/public_profiles/d5260339-2415-4f0b-b97b-590e6a57a0ee",
    "https://www.qwiklabs.com/public_profiles/51b5cb87-411e-47ec-b59e-cf16096ed405",
    "https://www.qwiklabs.com/public_profiles/89f08308-180f-4f2a-bd59-3abf70de31b9",
    "https://google.qwiklabs.com/public_profiles/9271b1a6-8d56-4728-9aec-13c75c7e9630",
    "https://www.qwiklabs.com/public_profiles/de986b02-26ec-4b9e-8b74-dbaa17ec2937",
    "https://www.qwiklabs.com/public_profiles/a15314f2-f989-4db9-a4cc-b9a5de660c61",
    "https://google.qwiklabs.com/public_profiles/1d1bbd29-acb4-4de7-89c2-1d17b427ea44",
    "https://google.qwiklabs.com/public_profiles/57bc3311-dfd8-484f-8a9e-43ea77ba3a34",
    "https://www.qwiklabs.com/public_profiles/383d2c87-23b5-4c3f-89dd-4e54585f1be3",
    "https://google.qwiklabs.com/public_profiles/6bed4e02-8010-4f6b-a737-4b746030b510",
    "https://google.qwiklabs.com/public_profiles/b2e4c3e3-cb31-408e-b4e6-8d1d058bafec",
    "https://www.qwiklabs.com/public_profiles/4ae428bc-de46-44b8-b343-b120b6cd5b2a",
    "https://google.qwiklabs.com/public_profiles/843fdc4d-4f2d-4c69-81d6-d879ff6f5904",
    "https://google.qwiklabs.com/public_profiles/8a95278d-f953-4069-bf1b-791936d66d29",
    "https://www.qwiklabs.com/public_profiles/d9561cf8-0554-4bef-af1b-04d1cc6d49ca",
    "https://google.qwiklabs.com/public_profiles/5c414599-899f-458f-9138-842b33529f5d",
    "https://www.qwiklabs.com/public_profiles/e9796dc2-7842-4c79-a2be-b7acbad9f874",
    "https://google.qwiklabs.com/public_profiles/3bf83140-949c-4d9d-8f83-e12b0e916d0d",
    "https://google.qwiklabs.com/public_profiles/f51a3b3e-3c66-46ea-829f-0a2bcec45d1e",
    "https://google.qwiklabs.com/public_profiles/ce56193a-7a5f-43a0-82b2-75d77d0d2793",
    "https://www.qwiklabs.com/public_profiles/0200907a-ff95-4967-989d-cf9e4411c049",
    "https://www.qwiklabs.com/public_profiles/69c07d8c-d883-4d32-9212-124bf8b69c16",
    "https://google.qwiklabs.com/public_profiles/044a4776-b4e5-4fac-b2b4-802eae1a10e9",
    "https://google.qwiklabs.com/public_profiles/f3115d20-6a95-4966-8579-2782c41f2586",
    "https://google.qwiklabs.com/public_profiles/467e60e6-1fb2-438b-ba0e-99637fad93db",
    "https://www.qwiklabs.com/public_profiles/ad610640-c2b0-4c92-a21c-9480fa054ef3",
    "https://www.qwiklabs.com/public_profiles/6f61fb9b-dd60-48f8-a2ef-beb7cdb7c3bc",
    "https://google.qwiklabs.com/public_profiles/cf584638-20b2-4e2c-a1a0-9be01b202158",
    "https://google.qwiklabs.com/public_profiles/c071a74e-1339-4b3a-a0ef-03f70720a397",
    "https://www.qwiklabs.com/public_profiles/d3d9c2d8-a965-4af1-b352-3c27327f8a26",
    "https://www.qwiklabs.com/public_profiles/6f297015-235e-4905-b16f-ce46d995a0c8",
    "https://www.qwiklabs.com/public_profiles/2b2fa4a0-1b41-4516-a102-367abdfd1a66",
    "https://www.qwiklabs.com/public_profiles/85be354d-5083-487b-9a21-158231528ede",
    "https://www.qwiklabs.com/public_profiles/a97374e4-d9c3-406b-9b2f-50211db4d5a1",
    "https://google.qwiklabs.com/public_profiles/227b1054-796a-42d1-9211-ae5421c69524",
    "https://google.qwiklabs.com/public_profiles/551c9260-509b-43dd-bc1e-55ff7470fa43",
    "https://www.qwiklabs.com/public_profiles/8db9f370-91c7-442b-886d-33e8ecf5bd5e",
    "https://www.qwiklabs.com/public_profiles/7f347e7f-f7f7-47fa-bc8a-bbc50f9361d3",
    "https://www.qwiklabs.com/public_profiles/a2c8c637-2120-42a2-8761-f98660431395",
    "https://www.qwiklabs.com/public_profiles/0bda5e98-0c62-4666-978f-470801a90560",
    "https://google.qwiklabs.com/public_profiles/60177f2a-c7a9-4498-b510-781133b922c3",
    "https://google.qwiklabs.com/public_profiles/b0cf75d9-8df6-41aa-b028-a220decd0c56",
    "https://google.qwiklabs.com/public_profiles/7b73b935-6c78-4e46-b632-e70c17f15a49",
    "https://google.qwiklabs.com/public_profiles/d4014d60-c235-47f3-a271-3e2430fa0670",
    "https://google.qwiklabs.com/public_profiles/d0120c20-be65-4bd4-b265-73de6b39df8f",
    "https://google.qwiklabs.com/public_profiles/4ae428bc-de46-44b8-b343-b120b6cd5b2a",
    "https://www.qwiklabs.com/public_profiles/d1d07de7-75d1-4a8f-8490-5f5cdf86736d",
    "https://www.qwiklabs.com/public_profiles/cd116d42-08f5-46d1-b8fd-0ae617af1fdd",
    "https://google.qwiklabs.com/public_profiles/4c143ac8-9ba5-4513-86dc-78c7f6629a8e",
    "https://www.qwiklabs.com/public_profiles/910be881-c8c2-40a8-a8e7-23af987cf37b",
    "https://www.qwiklabs.com/public_profiles/17a86520-17a0-40d3-b5ee-f0551667b16a",
    "https://google.qwiklabs.com/public_profiles/8a95278d-f953-4069-bf1b-791936d66d29",
    "https://www.qwiklabs.com/public_profiles/3876c5ff-5f35-4aff-8196-8c5137261350",
    "https://google.qwiklabs.com/public_profiles/a47e8661-c05c-49ea-bc2e-8a670eca5484",
    "https://google.qwiklabs.com/public_profiles/79b2df1f-9cdb-4da0-a70c-2e86fda3ca6b",
    "https://google.qwiklabs.com/public_profiles/5d66bd55-8bae-48be-b7c9-b7ee5f22452e",
    "https://google.qwiklabs.com/public_profiles/fc012ada-10c0-49e8-9e72-fb8d249a59a5",
    "https://www.qwiklabs.com/public_profiles/996622d4-612e-4895-aa7d-5a39b394cb75",
    "https://google.qwiklabs.com/public_profiles/8a174e3c-da8e-4e0e-86ef-413e2e73c959",
    "https://google.qwiklabs.com/public_profiles/ab177f6e-7d5b-40c6-a999-4b6ce98c3580",
    "https://www.qwiklabs.com/public_profiles/a2ecc1bb-7303-4b1c-9ed7-5ef9a69e8f37",
    "https://google.qwiklabs.com/public_profiles/8093c0cc-c322-4b53-befb-d6756042f5de",
    "https://www.qwiklabs.com/public_profiles/ab0efe29-3229-481a-aafa-c494e8857b1b",
    "https://www.qwiklabs.com/public_profiles/534f26e5-877c-4e7a-8900-35fab0240b6b",
    "https://www.qwiklabs.com/public_profiles/534f26e5-877c-4e7a-8900-35fab0240b6b",
    "https://www.qwiklabs.com/public_profiles/bae313c9-184e-4ccf-bc13-08013e176977",
    "https://google.qwiklabs.com/public_profiles/b34eb599-346c-4d2d-b569-2bd690d1922c",
    "https://www.qwiklabs.com/public_profiles/369d3c97-fabb-431d-a8be-b99087d088be",
    "https://www.qwiklabs.com/public_profiles/b2089f74-3034-48f5-99ec-8bcaed62a8d0",
    "https://google.qwiklabs.com/public_profiles/e9899dc6-6763-40e4-a2e5-bbb1382ace52",
    "https://google.qwiklabs.com/public_profiles/406ad4b0-fd23-4337-be93-bc78aa31a1bc",
    "https://www.qwiklabs.com/public_profiles/5c075f26-868c-4a7c-8bc0-738e33f62f11",
    "https://www.qwiklabs.com/public_profiles/7b171cad-e5a8-45d2-a808-d55b4ddb7bdb",
    "https://google.qwiklabs.com/public_profiles/f11cd7f8-baff-408b-a2f5-ceffc5cb72d2",
    "https://google.qwiklabs.com/public_profiles/f29ff94b-eed2-4d09-8244-9547bcd7e287",
    "https://google.qwiklabs.com/public_profiles/eeae58e8-d715-4b51-bccd-3d7efcd8b03c",
    "https://google.qwiklabs.com/public_profiles/33f34f1f-7903-46d8-9be8-5fe08601e80b",
    "https://www.qwiklabs.com/public_profiles/4eafdf42-5408-4c4c-8fef-4d72ff97e059",
    "https://www.qwiklabs.com/public_profiles/075aacee-0641-41f1-90d3-5d7c04223b06",
    "https://www.qwiklabs.com/public_profiles/63bde742-f8b1-4638-a3dd-bf896fd1de67",
    "https://www.qwiklabs.com/public_profiles/63bde742-f8b1-4638-a3dd-bf896fd1de67",
    "https://google.qwiklabs.com/public_profiles/e1fb5c9a-86d7-47ea-ba42-1cc59f109b4e",
    "https://qwiklabs.com/public_profiles/be8fe406-0da6-41a3-bf39-b1f4d9137938",
    "https://www.qwiklabs.com/public_profiles/a0c41bd2-2688-4e69-acbd-10956218c241",
    "https://google.qwiklabs.com/public_profiles/0a53acdc-43e8-45d0-8281-27309888e7bc",
    "https://google.qwiklabs.com/public_profiles/0ebd310a-6956-40ce-9207-eb91cf27201f",
    "https://google.qwiklabs.com/public_profiles/a8fc35d7-f4a0-4455-9dc4-43fbfb160a5a",
    "https://www.qwiklabs.com/public_profiles/aa432d2f-4eeb-49be-8682-025289461fa1",
    "https://google.qwiklabs.com/public_profiles/c3688d62-d879-4141-97cc-5c8af9d6d5aa",
    "https://google.qwiklabs.com/public_profiles/645375f6-1b7f-403d-b7d4-069a5e7b1540",
    "https://www.qwiklabs.com/public_profiles/d58122cb-ab53-4bb7-bae1-6d6d41f78a43",
    "https://google.qwiklabs.com/public_profiles/dad44f31-a85c-42ab-95f7-38201b9f837a",
    "https://google.qwiklabs.com/public_profiles/1cb05d89-1486-4413-b470-20a1b0f5183a",
    "https://google-run.qwiklabs.com/public_profiles/52ff2250-4518-435d-8e5f-d5134b2a6f04",
    "https://google.qwiklabs.com/public_profiles/6b0905e5-218f-4b3b-9e2b-dbccbe51f2f3",
    "https://www.qwiklabs.com/public_profiles/c224b973-9c38-458f-baf4-3a73a7107bfb",
    "https://www.qwiklabs.com/public_profiles/6794289c-3142-47bd-ba67-6513cc5212aa",
    "https://www.qwiklabs.com/public_profiles/6794289c-3142-47bd-ba67-6513cc5212aa",
    "https://www.qwiklabs.com/public_profiles/6794289c-3142-47bd-ba67-6513cc5212aa",
    "https://google.qwiklabs.com/public_profiles/11da2a24-3fea-4d41-b972-21d897c7f1a6",
    "https://google.qwiklabs.com/public_profiles/035b8972-7d51-4809-8d45-bd0b95b11fd3",
    "https://www.qwiklabs.com/public_profiles/d42ef34c-61bc-445c-a151-3a2da4ee19a4",
    "https://www.qwiklabs.com/public_profiles/9928cf55-91ec-48f1-b2fa-955248a6f349",
    "https://www.qwiklabs.com/public_profiles/a6ec0bef-cf23-4a11-963a-9ea8d23aa39f",
    "https://google.qwiklabs.com/public_profiles/ed764afc-af2a-4342-966e-ffa8085fe676",
    "https://www.qwiklabs.com/public_profiles/2a640689-a72f-4b08-b5a9-d282a480317d",
    "https://www.qwiklabs.com/public_profiles/f2924243-b348-47d7-b4e8-f2e03f4c2289",
    "https://www.qwiklabs.com/public_profiles/51b5cb87-411e-47ec-b59e-cf16096ed405",
    "https://www.qwiklabs.com/public_profiles/c7f6b33d-f034-4fd1-bc61-f3d8fbc1834e",
    "https://google.qwiklabs.com/public_profiles/1fff8893-36d9-4b78-bcfc-f456a733d12d",
    "https://www.qwiklabs.com/public_profiles/ed713c5f-9a85-45a0-b34a-b1cece1d8ebb",
    "https://www.qwiklabs.com/public_profiles/f7b60814-092f-4b34-a182-a7c10e8c84db",
    "https://google.qwiklabs.com/public_profiles/24a19a03-87b1-4ba6-97fc-db65560ab51f",
    "https://www.qwiklabs.com/public_profiles/4d2efe2a-3558-49b8-a446-b780c8e621fb",
    "https://www.qwiklabs.com/public_profiles/2d5c2f86-fbe3-4059-ad3a-9afe90ae11ae",
    "https://google.qwiklabs.com/public_profiles/bbe35975-f8c1-4b79-b644-7b9bbaa4e2e8",
    "https://www.qwiklabs.com/public_profiles/9e05650a-3460-482c-bb11-93314e68ed10",
    "https://google.qwiklabs.com/public_profiles/8137db04-540a-4097-8ea8-d82b4f25ee7c",
    "https://google.qwiklabs.com/public_profiles/fad1e075-57d1-4fb6-ad87-41d8912b2870",
    "https://www.qwiklabs.com/public_profiles/a54cb999-cf0c-46f4-a778-6383f3d2226d",
    "https://www.qwiklabs.com/public_profiles/90dae592-468b-483a-8fe6-9d49c882305b",
    "https://google.qwiklabs.com/public_profiles/866e8b54-ca87-4710-9280-f92ebce0bf1f",
    "https://www.qwiklabs.com/public_profiles/0f2b3f5a-4f68-401a-9043-a28a850faecd",
    "https://www.qwiklabs.com/public_profiles/11ab2213-11a1-4ad8-a424-38003a85c1f0",
    "https://www.qwiklabs.com/public_profiles/c95962ba-2548-4919-a509-8d65b80e17c0",
    "https://www.qwiklabs.com/public_profiles/cd2a3f21-9097-4fe9-a961-65ef6d2d5a4b",
    "https://google.qwiklabs.com/public_profiles/41dff993-46fb-43a6-9bb8-4267fd44e7d3",
    "https://www.qwiklabs.com/public_profiles/b4629cd9-58c5-4e8d-86eb-bfafc35d2b52",
    "https://google.qwiklabs.com/public_profiles/a1eb9989-b270-4aac-8750-eca4989e04d6",
    "https://google.qwiklabs.com/public_profiles/2e8d065f-4b0c-499b-b6da-7e5b50dd2956",
    "https://google.qwiklabs.com/public_profiles/7144d08e-e771-4f1f-aeb5-8f3a6a108d9f",
    "https://www.qwiklabs.com/public_profiles/bc6aaab4-2acb-4de7-9ebf-99d9f1674879",
    "https://google.qwiklabs.com/public_profiles/78fcd487-e1c4-4c78-b1d5-950110c39abb",
    "https://qwiklabs.com/public_profiles/2957b539-04f7-479d-83c9-c47f3e1c80c6",
    "https://google.qwiklabs.com/public_profiles/b9f55678-b78e-4047-a905-be5e5593ef3d",
    "https://www.qwiklabs.com/public_profiles/fa094dcf-6187-4133-89db-a7093e397860",
    "https://www.qwiklabs.com/public_profiles/fa094dcf-6187-4133-89db-a7093e397860",
    "https://www.qwiklabs.com/public_profiles/1fc4a636-3fbe-4d45-a276-f8ac692550bd",
    "https://www.qwiklabs.com/public_profiles/5e54b082-4848-4632-bbba-dad3ab9874c7"
]


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Cache-Control',
    'X-Requested-With',
]


CELERY_BEAT_SCHEDULE = {
    'generate-report': {
       'task': 'core.tasks.summary',
       'schedule': 1200.0,
    },
     
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


django_heroku.settings(locals())
