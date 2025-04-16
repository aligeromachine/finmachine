import React from "react";

export const Form = ({ children, onSubmit }) => {
  return (
    <section>
      <form onSubmit={onSubmit}>{children}</form>
    </section>
  );
};
