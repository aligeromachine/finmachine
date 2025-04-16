import { API_URL } from "./const";

export const apiClient = {
  get: async (endpoint) => {
    const response = await fetch(`${API_URL}${endpoint}`);
    if (!response.ok) throw new Error(response.statusText);
    return response.json();
  },
  post: async (endpoint, data) => {
    const token = localStorage.getItem("accessToken");
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
        ...(token ? { authorization: token } : {}),
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error(response.statusText);
    return response.json();
  },
  // Добавьте другие методы по необходимости
};
