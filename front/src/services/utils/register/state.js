import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { apiClient } from '../../../utils/requests';
import { initialState } from './model';
import { REGISTER_URL } from './const';

export const registerThunk = createAsyncThunk('stateRegister/registerThunk', async (data, { rejectWithValue }) => {
    const response = await apiClient.post(REGISTER_URL, data);
    if (!response.token) return rejectWithValue(response.message);

    return true;
});

export const stateRegister = createSlice({
    name: 'stateRegister',
    initialState,
    reducers: {
        setRegister: state => {
            state.loading = 'empty';
            state.register = false;
            state.error = '';
        },
    },
    extraReducers: builder => {
        builder

            .addCase(registerThunk.pending, state => {
                state.loading = 'loading';
                state.register = false;
                state.error = '';
            })
            .addCase(registerThunk.fulfilled, (state, action) => {
                state.loading = 'idle';
                state.register = action.payload;
            })
            .addCase(registerThunk.rejected, (state, action) => {
                state.loading = 'failed';
                state.error = action.payload;
            });
    },
});

export const { setRegister } = stateRegister.actions;
export const registerReducer = stateRegister.reducer;
