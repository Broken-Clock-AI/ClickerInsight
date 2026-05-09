import { useEffect, useRef } from 'react';
import { useGameStore } from './useGameStore';

export const useGameLoop = () => {
  const tick = useGameStore((state) => state.tick);
  const lastTimeRef = useRef<number>(Date.now());
  const requestRef = useRef<number>(0);

  const loop = () => {
    const now = Date.now();
    const deltaTime = (now - lastTimeRef.current) / 1000; // Convert ms to seconds

    // Safety cap: Prevent huge time jumps (e.g., from tab switching) from processing all at once if we want to add more logic later
    // For now, infinite offline progress is fine, but we cap at 1 day to prevent overflow if something goes wrong
    const safeDelta = Math.min(deltaTime, 86400);

    if (safeDelta > 0) {
      tick(safeDelta);
    }

    lastTimeRef.current = now;
    requestRef.current = requestAnimationFrame(loop);
  };

  useEffect(() => {
    requestRef.current = requestAnimationFrame(loop);
    return () => cancelAnimationFrame(requestRef.current);
  }, []); // Empty dependency array means this runs once on mount
};
