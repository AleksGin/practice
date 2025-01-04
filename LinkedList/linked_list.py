from obj_class import ObjList


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        if self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(next_obj=obj)
            obj.set_prev(prev_obj=self.tail)
            self.tail = obj

    def remove_obj(self) -> None:
        if self.tail is None:
            print("Список пуст - удалять нечего!")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_node = self.tail.get_prev()
            if prev_node:
                prev_node.set_next(next_obj=None)
            self.tail = prev_node

    def get_data(self) -> list | None:
        data = []
        current = self.head
        while current:
            data.append(current.get_data())
            current = current.get_next()
        return data
