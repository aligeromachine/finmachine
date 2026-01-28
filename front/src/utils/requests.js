import { API_URL } from './const';
import { getAccessToken } from './storage';

const createHeaders = method => {
    const token = getAccessToken();
    return {
        method: method,
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
    };
};
export const apiClient = {
    get: async endpoint => {
        const response = await fetch(`${API_URL}${endpoint}`, {
            ...createHeaders('GET'),
        });
        if (!response.ok) throw new Error(response.statusText);
        return await response.json();
    },
    post: async (endpoint, data) => {
        const response = await fetch(`${API_URL}${endpoint}`, {
            ...createHeaders('POST'),
            body: JSON.stringify(data),
        });
        if (!response.ok) throw new Error(response.statusText);
        return await response.json();
    },
    // Добавьте другие методы по необходимости
};
