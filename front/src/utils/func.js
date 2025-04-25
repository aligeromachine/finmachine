export const safeJsonParse = (jsonString) => {
  try {
    return {
      success: true,
      data: JSON.parse(jsonString),
    };
  } catch (error) {
    return {
      success: false,
      error: error.message,
    };
  }
};

export const isEmpty = (obj) => {
  if (!obj) {
    return true;
  }
  return Object.keys(obj).length === 0;
};

export const verifiedDict = () => {
  const queryString = Object.entries(newErrors)
    .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
    .join("&");
  return queryString;
};

export const create_params = (command, offset, limit) => {
  return {
    command,
    offset,
    limit,
  };
};
