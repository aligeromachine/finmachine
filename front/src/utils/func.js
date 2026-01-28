export const safeJsonParse = jsonString => {
    try {
        return {
            success: true,
            data: JSON.parse(jsonString),
        };
    } catch (error) {
        return {
            success: false,
            error: error.message,
        };
    }
};

export const isEmpty = obj => {
    if (!obj) {
        return true;
    }
    return Object.keys(obj).length === 0;
};

export const verifiedDict = () => {
    const queryString = Object.entries(newErrors)
        .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
        .join('&');
    return queryString;
};

export const create_params = (command, offset, limit) => {
    return {
        command,
        offset,
        limit,
    };
};

// Утилиты для работы с датами в Redux
export const dateUtils = {
    // Преобразование Date в строку для хранения в Redux
    toReduxFormat: date => {
        if (!date) return null;
        if (date instanceof Date) {
            return date.toISOString();
        }
        if (typeof date === 'string') {
            return date;
        }
        return null;
    },

    // Преобразование строки обратно в Date для использования в компонентах
    fromReduxFormat: dateString => {
        if (!dateString) return null;
        try {
            return new Date(dateString);
        } catch (error) {
            console.error('Error parsing date:', error);
            return null;
        }
    },

    // Проверка, является ли значение сериализуемым для Redux
    isSerializable: value => {
        const type = typeof value;
        if (value === null || type === 'string' || type === 'number' || type === 'boolean') {
            return true;
        }
        if (type === 'object') {
            if (value instanceof Date) return false;
            if (Array.isArray(value)) {
                return value.every(item => dateUtils.isSerializable(item));
            }
            return Object.values(value).every(item => dateUtils.isSerializable(item));
        }
        return false;
    },
};

// Форматы для отображения
export const dateFormats = {
    display: 'dd-MM-yyyy HH:mm:ss',
    iso: "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'",
    dateOnly: 'yyyy-MM-dd',
    timeOnly: 'HH:mm:ss',
};
