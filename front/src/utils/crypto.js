const chunkSize = 1 * 1024 * 1024; // 1 МБ

export const Sha256Buf = async buffer => {
    const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hash = hashArray.map(item => item.toString(16).padStart(2, '0')).join('');
    return hash;
};

export const Sha256str = async buffer => {
    const encoder = new TextEncoder();
    return await Sha256Buf(encoder.encode(buffer));
};

export const Sha256File = async file => {
    const buffer = await file.arrayBuffer();
    return await Sha256Buf(buffer);
};
