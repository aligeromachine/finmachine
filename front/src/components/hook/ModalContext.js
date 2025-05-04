import { createContext, useState, useContext, useCallback } from "react";

// Создаем контекст с начальными значениями
const ModalContext = createContext({
  isModalOpen: false,
  openModal: () => {},
  closeModal: () => {},
});

// Провайдер для управления состоянием модалки
export const ModalProvider = ({ children }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = useCallback(() => {
    setIsModalOpen(!isModalOpen);
  }, []);
  const closeModal = useCallback(() => {
    setIsModalOpen(false);
  }, []);

  return (
    <ModalContext.Provider value={{ isModalOpen, openModal, closeModal }}>
      {children}
    </ModalContext.Provider>
  );
};

// Кастомный хук для удобного доступа к контексту
export const useModal = () => {
  return useContext(ModalContext);
};
