import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { apiClient } from '../../utils/requests';
import { setTokenResponse, getAccessToken, getRefreshToken, delToken } from '../../utils/storage';
import { initialState } from './model';
import { tokenRefresh, tokenReturn } from './base';

export const loginThunk = createAsyncThunk('stateToken/loginThunk', async data => {
    const response = await apiClient.post('/auth/login/', data);
    return tokenReturn(response);
});

export const refreshThunk = createAsyncThunk('stateToken/refreshThunk', async () => {
    const access = getAccessToken();
    if (access) {
        var response = await apiClient.post('/auth/protected/', { access });
        if (response.token) return response.token;
        if (response.message !== 'Token expired') {
            return await tokenRefresh();
        }
    } else {
        return await tokenRefresh();
    }
});

export const logoutThunk = createAsyncThunk('stateToken/logoutThunk', async () => {
    const refresh = getRefreshToken();
    const response = await apiClient.post('/auth/logout/', { refresh });
    return response;
});

export const changeThunk = createAsyncThunk('stateToken/changeThunk', async data => {
    const response = await apiClient.post('/auth/change/', data);
    return tokenReturn(response);
});

export const stateToken = createSlice({
    name: 'stateToken',
    initialState,
    reducers: {},
    extraReducers: builder => {
        builder

            .addCase(loginThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(loginThunk.fulfilled, (state, action) => {
                state.loading = 'idle';
                setTokenResponse(action);
            })
            .addCase(loginThunk.rejected, state => {
                state.loading = 'failed';
            })

            .addCase(refreshThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(refreshThunk.fulfilled, (state, action) => {
                state.loading = 'idle';
                setTokenResponse(action);
            })
            .addCase(refreshThunk.rejected, state => {
                state.loading = 'failed';
            })

            .addCase(logoutThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(logoutThunk.fulfilled, state => {
                state.loading = 'idle';
                delToken();
            })
            .addCase(logoutThunk.rejected, state => {
                state.loading = 'failed';
            })

            .addCase(changeThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(changeThunk.fulfilled, state => {
                state.loading = 'idle';
            })
            .addCase(changeThunk.rejected, state => {
                state.loading = 'failed';
            });
    },
});

export const tokenReducer = stateToken.reducer;
