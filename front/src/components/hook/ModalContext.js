import { createContext, useState, useContext, useCallback } from "react";
import { useDispatch } from "react-redux";
import { store } from "../../services/store";
import { nullRowData } from "../../services/row/state";
import { dateUtils } from "../../utils/func";

// Создаем контекст с начальными значениями
const ModalContext = createContext({
  isModalOpen: false,
  openModal: () => {},
  closeModal: () => {},
  formData: {},
  setForm: () => {},
  onChange: () => {},
  onSet: () => {},
  isEdit: false,
});

// Провайдер для управления состоянием модалки
export const ModalProvider = ({ children }) => {
  const dispatch = useDispatch();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [formData, setForm] = useState({});
  const [isEdit, setEdit] = useState({});

  // eslint-disable-next-line react-hooks/preserve-manual-memoization
  const openModal = useCallback((isEdit = true) => {
    const data = store.getState().rowReducer.formData;
    setForm({ ...formData, ...data });
    setIsModalOpen(!isModalOpen);
    setEdit(isEdit);
  }, []);

  // eslint-disable-next-line react-hooks/preserve-manual-memoization
  const closeModal = useCallback(() => {
    dispatch(nullRowData());
    setIsModalOpen(false);
  }, []);

  const onChange = (e) => {
    setForm({ ...formData, [e.target.name]: e.target.value });
  };

  const onSet = (func) => {
    Object.keys(formData).forEach((key) => {
      if (formData[key] instanceof Date) {
        formData[key] = dateUtils.toReduxFormat(formData[key]);
      }
    });
    dispatch(func({ ...formData }));
    setForm({});
  };

  return (
    <ModalContext.Provider
      value={{
        isModalOpen,
        openModal,
        closeModal,
        formData,
        setForm,
        onChange,
        onSet,
        isEdit,
      }}
    >
      {children}
    </ModalContext.Provider>
  );
};

// Кастомный хук для удобного доступа к контексту
export const useModal = () => {
  return useContext(ModalContext);
};
