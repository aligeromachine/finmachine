import React from 'react';
import { BasicTable } from '../../components/table/BasicTable';
import { useModal } from '../../components/hook/ModalContext';
import { columnsTbl } from './column/HeaderProfit';
import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getProfitTable, setOffset } from '../../services/profit/state';

export const TableProfit = () => {
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProfitTable());
    }, [dispatch]);

    const { openModal } = useModal();
    const st = useSelector(store => store.profitReducer);

    async function onOffset(value) {
        dispatch(setOffset({ offset: value }));
        dispatch(getProfitTable());
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
