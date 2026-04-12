export const parseJwt = token => {
    try {
        // JWT состоит из трех частей: header.payload.signature
        // Нам нужна только вторая часть - payload
        const base64Url = token.split('.')[1];
        // Заменяем символы для корректного декодирования base64
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        // Декодируем из base64 и парсим JSON
        const jsonPayload = decodeURIComponent(
            atob(base64)
                .split('')
                .map(function (c) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                })
                .join('')
        );
        return JSON.parse(jsonPayload);
    } catch (e) {
        console.error('Не удалось распарсить токен', e);
        return null;
    }
};

// Функция для получения времени жизни токена
export const getTokenExpirationInfo = token => {
    if (!token) return { error: 'Токен отсутствует' };

    const decoded = parseJwt(token);
    if (!decoded || !decoded.exp) {
        return { error: 'Не удалось найти дату истечения (exp) в токене' };
    }

    const expTimestamp = decoded.exp * 1000; // Переводим секунды в миллисекунды
    const currentTimestamp = Date.now();
    const timeLeftMs = expTimestamp - currentTimestamp;

    return {
        expDate: new Date(expTimestamp).toLocaleString(), // Человеко-читаемая дата
        expiresInMs: timeLeftMs, // Осталось миллисекунд
        expiresInSeconds: Math.round(timeLeftMs / 1000), // Осталось секунд
        expiresInMinutes: Math.round(timeLeftMs / 1000 / 60), // Осталось минут
        isExpired: timeLeftMs <= 0,
    };
};
