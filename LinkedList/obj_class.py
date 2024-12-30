from typing import Any, Optional


class ObjList:
    def __init__(self, data: Any) -> None:
        self.__data: Any = data
        self.__prev: ObjList | None = None
        self.__next: ObjList | None = None

    def set_data(self, data: Any) -> None:
        self.__data = data

    def get_data(self) -> Any:
        return self.__data

    def set_next(self, next_obj: Optional["ObjList"]) -> None:
        self._check_for_correctness(obj=next_obj)
        self.__next = next_obj

    def get_next(self) -> Optional["ObjList"]:
        return self.__next

    def set_prev(self, prev_obj: Optional["ObjList"]) -> None:
        self._check_for_correctness(obj=prev_obj)
        self.__prev = prev_obj

    def get_prev(self) -> Optional["ObjList"]:
        return self.__prev

    def _check_for_correctness(self, obj) -> None:
        if obj is not None and not isinstance(obj, ObjList):
            raise TypeError("Значение должен быть экземпляром ObjList или None!")
