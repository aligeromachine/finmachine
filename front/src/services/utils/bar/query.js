import { apiClient } from '../../../utils/requests';
import { VERSION_URL } from './const';

export const getVersion = async () => {
    const response = await apiClient.get(VERSION_URL);
    if (!response) return Promise.reject('Error response');
    return response;
};
