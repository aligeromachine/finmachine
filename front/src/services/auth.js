import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";

const initialState = {
  token: null,
  loading: "empty",
};

export const loginThunk = createAsyncThunk(
  "dataAuth/loginThunk",
  async (data) => {
    const response = await apiClient.post("/auth/login/", data);

    if (!response.token) return Promise.reject(response.message);

    localStorage.setItem("refreshToken", response.token.access);
    localStorage.setItem("accessToken", response.token.refresh);

    return response.token;
  },
);

export const refreshThunk = createAsyncThunk(
  "dataAuth/refreshThunk",
  async () => {
    const response = await apiClient.post("/auth/protected/", {
      access: localStorage.getItem("accessToken"),
    });

    if (!response.token) {
      if (response.message === "Invalid token") {
        return Promise.reject(response.message);
      }

      if (response.message === "Token expired") {
        const response = await apiClient.post("/auth/refresh/", {
          refresh: localStorage.getItem("refreshToken"),
        });
        if (!response.token) return Promise.reject(response.message);

        return response.token;
      }
    }

    return response.token;
  },
);

export const registerThunk = createAsyncThunk(
  "dataAuth/registerThunk",
  async (data) => {
    const response = await apiClient.post("/auth/register/", data);

    if (!response.token) return Promise.reject(response.message);

    return response.user_id;
  },
);

export const logoutThunk = createAsyncThunk(
  "dataAuth/logoutThunk",
  async () => {
    const response = await apiClient.post("/auth/register/", {
      refresh: localStorage.getItem("refreshToken"),
    });

    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");

    return response;
  },
);

export const changeThunk = createAsyncThunk(
  "dataAuth/changeThunk",
  async (data) => {
    const response = await apiClient.post("/auth/change/", data);

    if (!response.token) return Promise.reject(response.message);

    return response;
  },
);

export const dataAuth = createSlice({
  name: "dataAuth",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder

      .addCase(loginThunk.pending, (state) => {
        state.loading = "loading";
        state.token = null;
      })
      .addCase(loginThunk.fulfilled, (state, action) => {
        state.loading = "idle";
        state.token = action.payload.access;
      })
      .addCase(loginThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(refreshThunk.pending, (state) => {
        state.loading = "loading";
        state.token = null;
      })
      .addCase(refreshThunk.fulfilled, (state, action) => {
        state.loading = "idle";
        state.token = action.payload.access;
      })
      .addCase(refreshThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(registerThunk.pending, (state) => {
        state.loading = "loading";
        state.token = null;
      })
      .addCase(registerThunk.fulfilled, (state) => {
        state.loading = "idle";
      })
      .addCase(registerThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(logoutThunk.pending, (state) => {
        state.loading = "loading";
        state.token = null;
      })
      .addCase(logoutThunk.fulfilled, (state) => {
        state.loading = "idle";
      })
      .addCase(logoutThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(changeThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(changeThunk.fulfilled, (state) => {
        state.loading = "idle";
      })
      .addCase(changeThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export default dataAuth.reducer;
