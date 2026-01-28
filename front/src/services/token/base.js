import { apiClient } from '../../utils/requests';
import { getRefreshToken } from '../../utils/storage';

export const tokenReturn = response => {
    if (response.token) return response.token;
    return Promise.reject(response.message);
};

export const tokenRefresh = async () => {
    const refresh = getRefreshToken();
    const response = await apiClient.post('/auth/refresh/', { refresh });
    return tokenReturn(response);
};
