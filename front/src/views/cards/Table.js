import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getCardsTable, setOffset } from "../../services/cards/state";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCardsTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const st = useSelector((store) => store.cardsReducer);

  async function onOffset(value) {
    dispatch(setOffset({ offset: value }));
    dispatch(getCardsTable());
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
