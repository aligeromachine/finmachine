# Настройки JWT
import datetime
JWT_SECRET_KEY = 'Mnbvcxzaq1!1!'  # В продакшене используйте сложный ключ
JWT_ALGORITHM = 'HS256'
JWT_ACCESS_TOKEN_LIFETIME = datetime.timedelta(minutes=60)
JWT_REFRESH_TOKEN_LIFETIME = datetime.timedelta(days=7)
