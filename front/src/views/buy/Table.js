import React from 'react';
import { BasicTable } from '../../components/table/BasicTable';
import { useModal } from '../../components/hook/ModalContext';
import { columnsTbl } from './column/Header';
import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getBuysTable, setOffset } from '../../services/buys/state';

export const TableBuy = () => {
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getBuysTable());
    }, [dispatch]);

    const { openModal } = useModal();
    const st = useSelector(store => store.buysReducer);

    async function onOffset(value) {
        dispatch(setOffset({ offset: value }));
        dispatch(getBuysTable());
    }

    return (
        <BasicTable
            columns={columnsTbl(openModal)}
            onOffset={onOffset}
            data={st.draw}
            total={st.recordsTotal}
            limit={st.recordsDisplay}
            offset={st.offset}
        />
    );
};
