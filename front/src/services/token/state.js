import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import {
  setTokenResponse,
  getAccessToken,
  getRefreshToken,
  delAccessToken,
  delRefreshToken,
} from "../../utils/storage";
import { initialState } from "./model";

export const loginThunk = createAsyncThunk(
  "stateToken/loginThunk",
  async (data) => {
    const response = await apiClient.post("/auth/login/", data);

    if (!response.token) return Promise.reject(response.message);

    setTokenResponse(response);

    return response.token;
  },
);

const tokenReturn = (response) => {
  if (response.token) return response.token;
  return Promise.reject(response.message);
};

export const refreshThunk = createAsyncThunk(
  "stateToken/refreshThunk",
  async () => {
    const access = getAccessToken();
    if (access) {
      var response = await apiClient.post("/auth/protected/", { access });
      if (response.token) return response.token;
      if (response.message !== "Token expired") {
        const params = { refresh: getRefreshToken() };
        const response = await apiClient.post("/auth/refresh/", params);
        setTokenResponse(response);
        return tokenReturn(response);
      }
    } else {
      const params = { refresh: getRefreshToken() };
      const response = await apiClient.post("/auth/refresh/", params);
      setTokenResponse(response);
      return tokenReturn(response);
    }
  },
);

export const logoutThunk = createAsyncThunk(
  "stateToken/logoutThunk",
  async () => {
    const response = await apiClient.post("/auth/logout/", {
      refresh: getRefreshToken(),
    });

    delAccessToken();
    delRefreshToken();

    return response;
  },
);

export const changeThunk = createAsyncThunk(
  "stateToken/changeThunk",
  async (data) => {
    const response = await apiClient.post("/auth/change/", data);
    return tokenReturn(response);
  },
);

export const stateToken = createSlice({
  name: "stateToken",
  initialState,
  reducers: {
    setAuthCheck: (state) => {
      state.isAuthChecked = true;
      state.loading = "idle";
    },
  },
  extraReducers: (builder) => {
    builder

      .addCase(loginThunk.pending, (state) => {
        state.loading = "loading";
        state.isAuthChecked = false;
      })
      .addCase(loginThunk.fulfilled, (state, action) => {
        state.loading = "idle";
        state.isAuthChecked = Boolean(action.payload.access);
      })
      .addCase(loginThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(refreshThunk.pending, (state) => {
        state.loading = "loading";
        state.isAuthChecked = false;
      })
      .addCase(refreshThunk.fulfilled, (state, action) => {
        state.loading = "idle";
        state.isAuthChecked = Boolean(action.payload.access);
      })
      .addCase(refreshThunk.rejected, (state) => {
        state.loading = "failed";
      })

      .addCase(logoutThunk.pending, (state) => {
        state.loading = "loading";
        state.isAuthChecked = false;
      })
      .addCase(logoutThunk.fulfilled, (state) => {
        state.loading = "idle";
        state.isAuthChecked = false;
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

export const { setAuthCheck } = stateToken.actions;

export const tokenReducer = stateToken.reducer;
