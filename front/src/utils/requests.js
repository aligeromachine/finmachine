import { API_URL, UPLOAD_URL } from './const';
import { getAccessToken } from './storage';
import { refreshToken } from '../services/utils/token/request';

const createHeaders = method => {
    return {
        method: method,
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            Authorization: `Bearer ${getAccessToken(true)}`,
        },
    };
};

const createSimpleHeaders = method => {
    return {
        method: method,
        headers: {
            Authorization: `Bearer ${getAccessToken(true)}`,
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
    chunks: async data => {
        const response = await fetch(`${API_URL}${UPLOAD_URL}`, {
            ...createSimpleHeaders('POST'),
            body: data,
            // Не устанавливаем Content-Type - браузер сам установит с правильным boundary
        });
        if (!response.ok) throw new Error(response.statusText);
        return await response.json();
    },
    // Добавьте другие методы по необходимости
};

export const postRequestCheck = async (url, params) => {
    let response = await apiClient.post(url, params);
    if (response.message == 'Token expired') {
        await refreshToken();
        return await apiClient.post(url, params);
    }
    return response;
};
