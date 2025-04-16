import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { ONE_HOUR, SEVEN_DAYS } from "../utils/const";
import { apiClient } from "../utils/requests";
import { setWithExpiry, getWithExpiry, removeItem } from "../utils/storage";

const initialState = {
  token: null,
  loading: "empty",
};

export const loginThunk = createAsyncThunk(
  "dataAuth/loginThunk",
  async (data) => {
    const response = await apiClient.post("/auth/login/", data);

    if (!response.token) return Promise.reject(response.message);

    setWithExpiry("accessToken", response.token.access, ONE_HOUR);
    setWithExpiry("refreshToken", response.token.refresh, SEVEN_DAYS);

    return response.token;
  },
);

export const refreshThunk = createAsyncThunk(
  "dataAuth/refreshThunk",
  async () => {
    const response = await apiClient.post("/auth/protected/", {
      access: getWithExpiry("accessToken"),
    });

    if (response.token) return response.token;

    if (response.message === "Token expired") {
      const response = await apiClient.post("/auth/refresh/", {
        refresh: getWithExpiry("refreshToken"),
      });
      if (!response.token) return Promise.reject(response.message);

      return response.token;
    }

    return Promise.reject(response.message);
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
    const response = await apiClient.post("/auth/logout/", {
      refresh: getWithExpiry("refreshToken"),
    });

    removeItem("accessToken");
    removeItem("refreshToken");

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
  reducers: {
    loadToken: (state) => {
      state.token = getWithExpiry("access_token");
    },
  },
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
        state.token = null;
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

export const { loadToken } = dataAuth.actions;

export default dataAuth.reducer;
