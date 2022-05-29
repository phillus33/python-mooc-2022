class Task:
    id = 0

    def __init__(self, desc: str, name: str, hours: int):
        self.description = desc
        self.programmer = name
        self.workload = hours
        self.finished = False
        Task.id += 1
        self.id = Task.id
        

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'NOT FINISHED' if self.finished == False else 'FINISHED'}"

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list({order.programmer for order in self.orders})

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        # if id not in [order.id for order in self.orders]:
        raise ValueError("id not found")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("programmer not found")
        return (
            len([item for item in self.finished_orders() if item.programmer == programmer]),
            len([item for item in self.unfinished_orders() if item.programmer == programmer]),
            sum([item.workload for item in self.finished_orders() if item.programmer == programmer]),
            sum([item.workload for item in self.unfinished_orders() if item.programmer == programmer])

        )




if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)