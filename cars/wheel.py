# -*- coding: utf-8 -*-
"""
Representation of Wheel
A car has 0 or several wheels
"""
import logging

logger = logging.getLogger(__name__)


class Wheel:
    """Representation of an wheel

    A or many wheel are associated with a car
    The type of motor can changed after the creation
    This class is not immutable
    """

    def __init__(self, size: int = 1, has_rim: bool = False) -> None:
        """Constructor method for Wheel

        :param size: size of the wheel and need to be >= 1
        :type size: int
        :param has_rim: if the wheel has a rim
        :type has_rim: bool
        """
        self.size: int = size
        self.has_rim: bool = has_rim
        return

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Wheel(size={self.size}, has_rim={self.has_rim})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Wheel):
            logger.warning(
                f"{type(o).__name__} isn't type 'Wheel'. So, will use default __eq__"
            )
            return super().__eq__(o)
        return self.size == o.size and self.has_rim == o.has_rim

    @property
    def size(self) -> int:
        """Getter of size attributes

        :return: size of wheel
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        """Setter of size attributes

        :param new_size: new size of wheel
        :type new_size: int
        """
        assert isinstance(new_size, int), "The size must be an integer"
        assert new_size > 0, "The size need to be > 0"
        self._size: int = new_size
        return

    @property
    def has_rim(self) -> bool:
        """Getter of has_rim attributes

        :return: if the wheel has a rim
        :rtype: bool
        """
        return self._has_rim

    @has_rim.setter
    def has_rim(self, new_has_rim: int) -> None:
        """Setter of has_rim attributes

        :param new_has_rim: indicate if the wheel has a rim
        :type new_has_rim: bool
        """
        assert isinstance(new_has_rim, bool), "The has_rim must be a boolean"
        self._has_rim: bool = new_has_rim
        return
