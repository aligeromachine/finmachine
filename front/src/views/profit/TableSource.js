import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/HeaderSource";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getSourceTable, setOffset } from "../../services/source/state";

export const TableSource = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getSourceTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const st = useSelector((store) => store.sourceReducer);

  async function onOffset(value) {
    dispatch(setOffset({ offset: value }));
    dispatch(getSourceTable());
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
