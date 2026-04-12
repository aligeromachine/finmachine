export const API_URL = import.meta.env.DEV ? 'https://127.0.0.1/api' : `/api`;
export const UPLOAD_URL = '/upload/chunks/';
export const CHUNK_SIZE = 1024 * 1024; // 1MB чанки
const SECOND = 1000;
const MINUTE = 60 * SECOND;
const HOUR = 60 * MINUTE;
export const INTERVAL = {
    SECOND,
    SEC_FIVE: 5 * SECOND,
    SEC_TEN: 10 * SECOND,
    SEC_FIFTEEN: 15 * SECOND,
    SEC_TWENTY: 20 * SECOND,
    SEC_TRIRTY: 30 * SECOND,
    MINUTE,
    MIN_FIVE: 5 * MINUTE,
    MIN_TEN: 10 * MINUTE,
    MIN_FIFTEEN: 15 * MINUTE,
    MIN_TWENTY: 20 * MINUTE,
    MIN_TRIRTY: 30 * MINUTE,
    MIN_FIFTY: 50 * MINUTE,
    HOUR,
    DAYS: 24 * HOUR,
    DAY_SEVEN: 7 * 24 * HOUR,
};
