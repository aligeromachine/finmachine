import { apiClient } from '../../utils/requests';
import { LOG_URL, ALL } from './const';

export const getLogger = async () => {
    const response = await apiClient.post(LOG_URL, { command: ALL });
    if (!response) return Promise.reject('Error response');
    return response;
};

export const delLogger = async msg => {
    const response = await apiClient.post(LOG_URL, {
        command: `delete_${msg}`,
    });
    if (!response) return Promise.reject('Error response');
    return response;
};
