import React from 'react';
import { handleDeleteRow } from '../../../components/action/Action';
import { deleteProdRow, getProdRow } from '../../../services/products/request';
import st from './row.module.css';

export const columnsTbl = openModal => {
    const openWithEdit = async id => {
        await getProdRow(id);
        openModal();
    };

    return [
        {
            accessorKey: 'id',
            header: 'Id',
            size: 100,
        },
        {
            accessorKey: 'created',
            header: 'Created',
        },
        {
            accessorKey: 'catalog',
            header: 'Catalog',
        },
        {
            accessorKey: 'title',
            header: 'Title',
        },
        {
            accessorKey: null,
            header: 'Action',
            cell: ({ row }) => (
                <span>
                    <i onClick={() => handleDeleteRow(row.original.id, deleteProdRow)}>
                        <img className={st.iconMl} src={'/static/img/delete.png'} height={24} width={24} />
                    </i>

                    <i onClick={() => openWithEdit(row.original.id)}>
                        <img className={st.iconMl} src={'/static/img/edit.png'} height={24} width={24} />
                    </i>
                </span>
            ),
        },
    ];
};
