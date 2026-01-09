import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/HeaderProd";
import { getProdTable, setOffset } from "../../services/products/state";

export const TableProd = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getProdTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const st = useSelector((store) => store.productsReducer);

  async function onOffset(value) {
    dispatch(setOffset({ offset: value }));
    dispatch(getProdTable());
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
