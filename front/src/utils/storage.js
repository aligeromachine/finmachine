import { safeJsonParse } from "./func";

export const setWithExpiry = (key, value, ttl) => {
  const now = new Date();
  const item = {
    value: value,
    expiry: now.getTime() + ttl,
  };
  localStorage.setItem(key, JSON.stringify(item));
};

export const getWithExpiry = (key) => {
  const itemStr = localStorage.getItem(key);

  if (!itemStr) {
    return null;
  }

  const result = safeJsonParse(itemStr);
  if (!result.success) {
    localStorage.removeItem(key);
    return null;
  }

  const item = result.data;
  const now = new Date();

  if (now.getTime() > item.expiry) {
    localStorage.removeItem(key);
    return null;
  }

  return item.value;
};

export const removeItem = (key) => {
  localStorage.removeItem(key);
};
