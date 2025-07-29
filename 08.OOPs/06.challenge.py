class Temperature:
    scale ="Celsius"

    @staticmethod
    def to_fahrenheit(c):
        return (c * 9/5) + 32
    @classmethod
    def set_scale(cls, new_scale):
        cls.scale = new_scale
