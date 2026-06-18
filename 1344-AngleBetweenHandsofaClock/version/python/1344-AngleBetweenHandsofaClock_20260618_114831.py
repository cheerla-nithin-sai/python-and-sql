# Last updated: 6/18/2026, 11:48:31 AM
    def angleClock(self, hour: int, minutes: int) -> float:
        h, m = hour + minutes/60, minutes / 5
        angle = abs(h-m) * 30
        return min(angle, 360-angle)