import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { apiClient } from '../../../utils/requests';
import { setTokenResponse, getAccessToken, getRefreshToken, delToken } from '../../../utils/storage';
import { initialState } from './model';
import { LOGIN_URL, PROTECTED_URL, LOGOUT_URL, CHANGE_URL, REFRESH_URL } from './const';
import { printObj } from '../../../utils/func';

const tokenReturn = response => {
    if (response.token) {
        printObj(response.token);
        return response.token;
    }
    return Promise.reject(response.message);
};

export const loginThunk = createAsyncThunk('stateToken/loginThunk', async data => {
    const response = await apiClient.post(LOGIN_URL, data);
    return tokenReturn(response);
});

const tokenRefreshRequest = async () => {
    console.log('***tokenRefreshRequest***');
    const refresh = getRefreshToken();
    const response = await apiClient.post(REFRESH_URL, { refresh });
    return tokenReturn(response);
};

export const protectedThunk = createAsyncThunk('stateToken/protectedThunk', async () => {
    console.log('***protectedThunk***');
    const access = getAccessToken(true);
    const response = await apiClient.post(PROTECTED_URL, { access });
    if (response.message == 'Token expired') {
        return await tokenRefreshRequest();
    }
    return tokenReturn(response);
});

export const refreshThunk = createAsyncThunk('stateToken/refreshThunk', async () => {
    return await tokenRefreshRequest();
});

export const logoutThunk = createAsyncThunk('stateToken/logoutThunk', async () => {
    const refresh = getRefreshToken();
    const response = await apiClient.post(LOGOUT_URL, { refresh });
    return response;
});

export const changeThunk = createAsyncThunk('stateToken/changeThunk', async data => {
    const response = await apiClient.post(CHANGE_URL, data);
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
                setTokenResponse(action?.payload);
            })
            .addCase(loginThunk.rejected, state => {
                state.loading = 'failed';
            })

            .addCase(protectedThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(protectedThunk.fulfilled, (state, action) => {
                state.loading = 'idle';
                setTokenResponse(action?.payload);
            })
            .addCase(protectedThunk.rejected, state => {
                state.loading = 'failed';
            })

            .addCase(refreshThunk.pending, state => {
                state.loading = 'loading';
            })
            .addCase(refreshThunk.fulfilled, (state, action) => {
                state.loading = 'idle';
                setTokenResponse(action?.payload);
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
