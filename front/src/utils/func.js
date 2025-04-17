export function safeJsonParse(jsonString) {
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
}
