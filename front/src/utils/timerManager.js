class TimerManager {
    constructor() {
        this.timers = new Map();
    }

    setTimer(id, callback, delay) {
        this.clearTimer(id);
        const timerId = setTimeout(() => {
            callback();
            this.clearTimer(id);
        }, delay);
        this.timers.set(id, timerId);
    }

    clearTimer(id) {
        if (this.timers.has(id)) {
            clearTimeout(this.timers.get(id));
            this.timers.delete(id);
        }
    }

    clearAll() {
        this.timers.forEach(timerId => clearTimeout(timerId));
        this.timers.clear();
    }
}

export const timerManager = new TimerManager();
