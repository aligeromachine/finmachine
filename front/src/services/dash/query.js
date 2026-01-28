import { apiClient } from '../../utils/requests';
import { DASH_URL, BASE } from './const';

export const getDash = async () => {
    const response = await apiClient.post(DASH_URL, { command: BASE });
    if (!response) return Promise.reject('Error response');
    return response;
};
