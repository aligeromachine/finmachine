import { CHUNK_SIZE } from './const';
import { apiClient } from './requests';

export const uploadChunk = async (chunk, sum, index) => {
    const formData = new FormData();
    formData.append('chunk', chunk);
    formData.append('sum', sum);
    formData.append('index', index);

    const response = await apiClient.chunks(formData);
    return response;
};

export const uploadChunks = async (file, sum) => {
    const totalChunks = Math.ceil(file.size / CHUNK_SIZE);

    for (let index = 0; index < totalChunks; index++) {
        const start = index * CHUNK_SIZE;
        const end = Math.min(start + CHUNK_SIZE, file.size);
        const chunk = file.slice(start, end);

        const response = await uploadChunk(chunk, sum, index);
        if (response) {
            const progress = ((index + 1) / totalChunks) * 100;
            console.log(progress);
        }
    }
};
